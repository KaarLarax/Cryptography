#include <Arduino.h>

void setup() {
  // put your setup code here, to run once:
  pinMode(D2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i < 1023; i++) {
    analogWrite(D2, i);
    delay(10);
  }
}