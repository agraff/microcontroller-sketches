int switchPin = 10;
int ledPin = 13;

void setup() {
  pinMode(switchPin, INPUT);
  pinMode(ledPin, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(switchPin) == HIGH) {
    digitalWrite(ledPin, HIGH);
    Serial.write(1);
  } else {
    digitalWrite(ledPin, LOW);
    Serial.write(0);
  }
  delay(100);
}

