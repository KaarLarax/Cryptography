#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Arduino.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64


Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
    Serial.begin(9600);
    while (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        Serial.println("OLED no encontrada");
        delay(1000);
    }

    display.clearDisplay();
    display.setTextColor(SSD1306_WHITE); // Importante si no lo pones tu pantalla no muestra nada
    display.setTextSize(1);
    display.setCursor(0, 0);

    display.println("Hola Carlos y Angy!");
    display.println("ESP8266");
    display.println("Lectura de voltaje");
    display.println("TAR-07 practica 2");

    display.display();
    delay(5000);
}

void loop() {
    static float val = 0.0f;
    static int input = 0;
    // Lectura de entrada
    input = int(analogRead(A0));
    val = 1.00f * input * (3.3 / 1023.0);

    // Impresion de valores de lectura
    display.clearDisplay();
    display.setCursor(0, 0);
    display.print("Valor: ");
    display.println(input);
    display.print("Voltaje: ");
    display.println(val);
    display.display();

    delay(3000);
}