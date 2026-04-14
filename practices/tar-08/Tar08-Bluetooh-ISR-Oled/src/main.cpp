#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Arduino.h>
#include <SoftwareSerial.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define PIN_INTE D7

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire);
SoftwareSerial miBT(D5, D6);

volatile bool isConfirmed = false;

void IRAM_ATTR isr() {
    isConfirmed = true;
}

void setup() {
    Serial.begin(9600);

    // Pantalla inicializacion
    if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        Serial.println("No se encontro la OLED");
        while (true)
            ;
    }
    display.clearDisplay();
    display.setCursor(0, 0);
    display.setTextColor(WHITE);
    display.setTextSize(1);
    display.println("Tar-08");
    display.println("Practica: ISR con Bluetooth y Oled");
    display.display();
    delay(3000);

    // Serial BT
    miBT.begin(9600);

    // Interrupcion
    pinMode(PIN_INTE, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(PIN_INTE), isr, FALLING);
}

void loop() {
    // Interrupcion
    Serial.println(isConfirmed);
    if (isConfirmed) {
        display.clearDisplay();
        display.setCursor(0, 0);
        display.display();
        isConfirmed = false;
        display.println("Interrupcion Activada");
        display.println("Enviando mensaje...");
        display.display();
        miBT.println("Hola Carlos...");
        delay(2000);
        display.clearDisplay();
        display.setCursor(0, 0);
        display.display();
    }

    // Mensaje BT
    if (miBT.available()) {
        display.clearDisplay();
        display.setCursor(0, 0);
        display.display();
        display.println("Mesaje desde el telefono:");
        display.println("Leyendo mensaje");
        display.println(miBT.readStringUntil('\n'));
        display.display();
        delay(2000);
    }
}