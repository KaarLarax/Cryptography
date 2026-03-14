#include <Arduino.h>
#include <DHT.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define DHTPIN D5
#define DHTTYPE DHT11

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);
DHT dht(DHTPIN, DHTTYPE);
void setup() {
  dht.begin();
  Serial.begin(9600);

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("OLED no encontrada");
    for(;;);
  }

  display.clearDisplay();

  display.setTextSize(1);
  display.setCursor(0,10);

  display.println("Hola Carlos!");
  display.println("ESP8266");
  display.println("Sensor de teperatura y humedad");
  display.println("TAR-07 practica 1");

  display.display();
  delay(100000);
}

void loop() {
  // Lectura de temperaturas.
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  Serial.println("entra");
  // Mostrar en pantalla
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  if (isnan(temp) || isnan(hum)) {
    display.println("Error al detectar el sensor DHT11");
    display.display();
    return;
  }
  display.print("Temperatura: ");
  display.print(temp);
  display.println(" C");
  display.print("Humedad: ");
  display.print(hum);
  display.println(" %");
  display.display();
}