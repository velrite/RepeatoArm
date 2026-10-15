// RepeatoArm security alarm: HC-SR04 proximity alarm with LEDs, buzzer and a reset button.
// Transcribed from the code printed in the thesis (section 3.2); whitespace restored, logic unchanged.
// NOT VERIFIED: byte-for-byte match with the file that was flashed to the board.

//Define pins for the ultrasonic sensor
const int trigPin = 9;
const int echoPin = 10;
//Define pins for the LEDs
const int ledPins[] = {2, 3, 4, 5};
//Define pin for the buzzer
const int buzzerPin = 6;
//Define pin for the push button
const int buttonPin = 7;

//Variables to store the duration and distance
long duration;
int distance;

//Variables for the state of the system
bool alarmActive = false;
unsigned long alarmStartTime = 0;

void setup() {
  //Initialize the serial communication
  Serial.begin(9600);
  //Initialize the ultrasonic sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  //Initialize the LED pins
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  //Initialize the buzzer pin
  pinMode(buzzerPin, OUTPUT);
  //Initialize the button pin
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  //Check if the reset button is pressed
  if (digitalRead(buttonPin) == LOW) {
    alarmActive = false;
    alarmStartTime = 0;
    resetAlarm();
  }
  //Measure the distance
  distance = measureDistance();
  //Check if the distance is less than 50 cm
  if (distance < 50 && !alarmActive) {
    alarmActive = true;
    alarmStartTime = millis();
    activateAlarm();
  }
  //If the alarm is active, check if 5 seconds have passed
  if (alarmActive && millis() - alarmStartTime >= 5000) {
    alarmActive = false;
    resetAlarm();
  }
  delay(100); //Small delay to avoid bouncing
}

int measureDistance() {
  //Send a 5 microsecond pulse to the trig pin  (comment as printed; the code below sends 10 microseconds)
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  //Measure the pulse duration on the echo pin
  duration = pulseIn(echoPin, HIGH);
  //Calculate the distance in centimeters
  distance = duration * 0.034 / 2;
  return distance;
}

void activateAlarm() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(ledPins[i], HIGH);
  }
  tone(buzzerPin, 1000); //Emit a beep sound
}

void resetAlarm() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(ledPins[i], LOW);
  }
  noTone(buzzerPin); //Stop the beep sound
}
