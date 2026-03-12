#include <Arduino.h>
#include <ESP8266WiFi.h>

// Replace with your network credentials
const char* ssid = "espai13-10";
const char* password = "1234567890";

void setup() {
    Serial.begin(9600);
    delay(10);

    // Set WiFi to station mode (client) and disconnect from an AP if connected
    WiFi.mode(WIFI_STA);
    WiFi.disconnect();
    delay(100);

    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println();
    Serial.println("WiFi connected");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}

void loop() {
    // Your main code loop goes here
    delay(2000);
    Serial.println("Still connected...");
}
