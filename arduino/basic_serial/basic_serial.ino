int switchPin = 10;
int ledPin = 13;
int PUSHED = LOW;

void setup() {
  pinMode(switchPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(switchPin) == PUSHED) {
    digitalWrite(ledPin, HIGH);
    serialWrite(1);
  } else {
    digitalWrite(ledPin, LOW);
    serialWrite(0);
  }
  delay(100);
}

void serialWrite(int value) {
  bool useBinary = true;
  
  if (useBinary) {
    Serial.write(value);
  } else {
    Serial.print(value);
  }
}

