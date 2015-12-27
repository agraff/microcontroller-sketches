int firstSwitchPin = 8;
int lastSwitchPin = 12;
int ledPin = 13;
int PUSHED = LOW;

void setup() {
  for (int pin = firstSwitchPin; pin <= lastSwitchPin; pin++) {
    pinMode(pin, INPUT_PULLUP);
  }
  
  pinMode(ledPin, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  int pinsState = 0;
  
  for (int pin = lastSwitchPin; pin >= firstSwitchPin; pin--) {
    pinsState = pinsState << 1;
    
    if (digitalRead(pin) == PUSHED) {
      pinsState += 1;
    }
  }

  serialWrite(pinsState);

  if (pinsState > 0) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

  delay(100);
}

void serialWrite(int value) {
  bool useBinary = true; // set false to help with debugging
  
  if (useBinary) {
    Serial.write(value);
  } else {
    Serial.print(value);
  }
}

