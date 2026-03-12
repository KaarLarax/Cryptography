#include <Arduino.h>

void setup() {
    pinMode(D2, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    // put your main code here, to run repeatedly:
    for (int i = 0; i < 255; i++) {
        analogWrite(D2, i);
        Serial.println(i);
        delay(100);
    }
}