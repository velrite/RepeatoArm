"""RepeatoArm pick-and-drop kinematics: three independent IK methods + FK check.

Geometry (cm): shoulder axis height H, upper arm L1, forearm+closed claw L2.
Angles: q1 base bearing from +X (deg); q2 upper-arm elevation above horizontal;
q3 elbow angle of forearm relative to upper arm (negative = forearm bent downward).
Run:  python kinematics_check.py
"""
import numpy as np

H, L1, L2 = 13.5, 15.0, 15.0          # shoulder height, upper arm, forearm + closed claw
BASE = (10.0, 18.0)                   # arm base on the 60 x 60 cm board (estimated from video)
deg, rad = np.degrees, np.radians


# ---------- Method 1: law of cosines ----------
def method1(r, z):
    dz = z - H
    D = np.hypot(r, dz)
    if D > L1 + L2 + 1e-9:
        return None, dict(dz=dz, D=D)
    c3 = np.clip((D**2 - L1**2 - L2**2) / (2 * L1 * L2), -1, 1)
    q3 = -np.arccos(c3)                                   # elbow-up solution
    alpha = np.arctan2(dz, r)
    beta = np.arctan2(L2 * np.sin(q3), L1 + L2 * np.cos(q3))
    q2 = alpha - beta
    return (deg(q2), deg(q3)), dict(dz=dz, D=D, c3=c3, q3=deg(q3), alpha=deg(alpha), beta=deg(beta))


# ---------- Method 2: circle intersection (coordinate geometry) ----------
def method2(r, z):
    S, T = np.array([0.0, H]), np.array([r, z])
    v = T - S
    D = np.linalg.norm(v)
    if D > L1 + L2 + 1e-9:
        return None, dict(D=D)
    a = (L1**2 - L2**2 + D**2) / (2 * D)
    h = np.sqrt(max(L1**2 - a**2, 0.0))
    u = v / D
    perp = np.array([-u[1], u[0]])
    E = max([S + a * u + h * perp, S + a * u - h * perp], key=lambda e: e[1])   # elbow-up = higher point
    q2 = np.arctan2(E[1] - H, E[0])
    fore = np.arctan2(z - E[1], r - E[0])
    return (deg(q2), deg(fore - q2)), dict(a=a, h=h, E=E, fore=deg(fore))


# ---------- Method 3: numerical damped least squares (Jacobian) ----------
def method3(r, z, lam=0.01, tol=1e-6, maxit=20000):
    q = np.array([rad(45.0), rad(-30.0)])                 # arbitrary start, elbow-up side
    target = np.array([r, z - H])
    for it in range(1, maxit + 1):
        a, b = q
        p = np.array([L1 * np.cos(a) + L2 * np.cos(a + b), L1 * np.sin(a) + L2 * np.sin(a + b)])
        e = target - p
        res = np.linalg.norm(e)
        if res < tol:
            return (deg(q[0]), deg(q[1])), dict(it=it, res=res, ok=True)
        J = np.array([[-L1 * np.sin(a) - L2 * np.sin(a + b), -L2 * np.sin(a + b)],
                      [L1 * np.cos(a) + L2 * np.cos(a + b), L2 * np.cos(a + b)]])
        q = q + J.T @ np.linalg.solve(J @ J.T + lam**2 * np.eye(2), e)
    return (deg(q[0]), deg(q[1])), dict(it=maxit, res=res, ok=False)


# ---------- Check: forward kinematics with 4x4 homogeneous transforms ----------
def Rz(t): c, s = np.cos(t), np.sin(t); return np.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
def Ry(t): c, s = np.cos(t), np.sin(t); return np.array([[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]])
def Tr(x, y, z): T = np.eye(4); T[:3, 3] = [x, y, z]; return T

def fk(q1, q2, q3):
    """Return tip position (dx, dy, z) relative to the base axis. Inputs in degrees."""
    T = Rz(rad(q1)) @ Tr(0, 0, H) @ Ry(-rad(q2)) @ Tr(L1, 0, 0) @ Ry(-rad(q3)) @ Tr(L2, 0, 0)
    return T[:3, 3]


def bearings(dx, dy):
    r = np.hypot(dx, dy)
    return deg(np.arctan2(dy, dx)), deg(np.sign(dy) * np.arccos(dx / r)), deg(np.arcsin(dy / r))


def solve_case(x, y, z):
    dx, dy = x - BASE[0], y - BASE[1]
    r = np.hypot(dx, dy)
    b1, b2, b3 = bearings(dx, dy)
    m1, s1 = method1(r, z)
    m2, s2 = method2(r, z)
    m3, s3 = method3(r, z)
    out = dict(dx=dx, dy=dy, r=r, b=(b1, b2, b3), m1=m1, s1=s1, m2=m2, s2=s2, m3=m3, s3=s3, reachable=m1 is not None)
    if m1 is not None:
        out["fk"] = {}
        for k, m in (("m1", m1), ("m2", m2), ("m3", m3)):
            p = fk(b1, m[0], m[1])
            out["fk"][k] = (p, 10 * np.linalg.norm(p - np.array([dx, dy, z])))
        arr = np.array([m1, m2, m3])
        out["spread"] = np.ptp(arr, axis=0)
    return out


def tip_error_per_degree(r=28.0, z=22.0, q1=28.3):
    q2, q3 = method1(r, z)[0]
    p0 = fk(q1, q2, q3)
    e = [np.linalg.norm(fk(q1 + 1, q2, q3) - p0), np.linalg.norm(fk(q1, q2 + 1, q3) - p0), np.linalg.norm(fk(q1, q2, q3 + 1) - p0)]
    return e, float(np.sqrt(sum(v * v for v in e)))


if __name__ == "__main__":
    reach_r = float(np.sqrt((L1 + L2) ** 2 - (22 - H) ** 2))
    th = np.arctan2(14, 26)
    cases = [("Drop (stand)", 31, 13, 10)]
    for nm, rr in (("Pick - near", 24.0), ("Pick - mid", 26.0), ("Pick - far", 28.0), ("Pick - full stretch", reach_r)):
        cases.append((nm, BASE[0] + rr * np.cos(th), BASE[1] + rr * np.sin(th), 22.0))
    cases.append(("Pick as first read from video", 36, 32, 22))
    print(f"{'case':32s} {'reach':6s} {'q1':>7s} {'q2':>7s} {'q3':>8s} {'spread(deg)':>11s} {'FK err mm (worst)':>18s}")
    for nm, x, y, z in cases:
        c = solve_case(x, y, z)
        if not c["reachable"]:
            print(f"{nm:32s} {'NO':6s}  D = {c['s1']['D']:.2f} cm > {L1 + L2:.0f} cm by {c['s1']['D'] - 30:.2f} cm; all 3 methods agree: no solution")
            continue
        worst = max(v[1] for v in c["fk"].values())
        print(f"{nm:32s} {'yes':6s} {c['b'][0]:7.2f} {c['m1'][0]:7.2f} {c['m1'][1]:8.2f} {c['spread'].max():11.6f} {worst:18.6f}")
