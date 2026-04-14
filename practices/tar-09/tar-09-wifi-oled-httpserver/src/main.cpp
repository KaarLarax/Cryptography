#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Arduino.h>
#include <ESP8266WebServer.h>
#include <ESP8266WiFi.h>
#include "secrets.h" // libreria para proteccion de variables
#include "WebPage.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

const String WIFI_SSID = WIFI_SSID_SECRET;
const String WIFI_PASSWORD = WIFI_PASSWORD_SECRET;

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire);
ESP8266WebServer server(80);

void clear_display(Adafruit_SSD1306 &display) {
    display.clearDisplay();
    display.setCursor(0, 0);
}

void drawCenteredText(const char *topLine, const char *bottomLine) {
    display.clearDisplay();
    display.setTextColor(WHITE);
    display.setTextSize(2);
    display.setCursor(10, 12);
    display.println(topLine);
    display.setTextSize(1);
    display.setCursor(18, 40);
    display.println(bottomLine);
    display.display();
}

void showGearsLogo() {
    display.clearDisplay();
    display.setTextColor(WHITE);

    display.drawCircle(34, 28, 12, WHITE);
    display.drawCircle(34, 28, 4, WHITE);
    display.drawLine(34, 12, 34, 6, WHITE);
    display.drawLine(34, 40, 34, 46, WHITE);
    display.drawLine(18, 28, 12, 28, WHITE);
    display.drawLine(46, 28, 52, 28, WHITE);
    display.drawLine(24, 18, 20, 14, WHITE);
    display.drawLine(44, 38, 48, 42, WHITE);
    display.drawLine(24, 38, 20, 42, WHITE);
    display.drawLine(44, 18, 48, 14, WHITE);

    display.setTextSize(2);
    display.setCursor(64, 16);
    display.println("GEARS");
    display.setTextSize(1);
    display.setCursor(64, 42);
    display.println("Logo activo");
    display.display();
}

void showHaloLogo() {
    display.clearDisplay();
    display.setTextColor(WHITE);

    display.drawCircle(38, 24, 14, WHITE);
    display.drawCircle(38, 24, 11, WHITE);
    display.drawLine(18, 36, 58, 36, WHITE);
    display.drawLine(22, 34, 12, 26, WHITE);
    display.drawLine(18, 36, 10, 40, WHITE);
    display.drawLine(58, 34, 68, 26, WHITE);
    display.drawLine(58, 36, 68, 40, WHITE);

    display.setTextSize(2);
    display.setCursor(68, 16);
    display.println("HALO");
    display.setTextSize(1);
    display.setCursor(68, 42);
    display.println("Logo activo");
    display.display();
}

void setup() {
    Serial.begin(9600);
    Serial.println();

    // Pantalla inicializacion
    if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        Serial.println("No se encontro la OLED");
        while (true)
            ;
    }

    drawCenteredText("Tar-09", "WIFI HTTP SERVER");
    delay(3000);

    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    clear_display(display);

    display.print("Connecting");
    display.display();
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    clear_display(display);
    display.print("Connected, IP address: ");
    display.println(WiFi.localIP());
    display.display();
    server.on("/", HTTP_GET, []() {
        server.send(200, "text/html", HTML_CONTENT);
    });

    server.on("/gears", HTTP_GET, []() {
        showGearsLogo();
        server.send(200, "text/plain", "GEARS mostrado en OLED");
    });

    server.on("/halo", HTTP_GET, []() {
        showHaloLogo();
        server.send(200, "text/plain", "HALO mostrado en OLED");
    });

    server.begin();
    Serial.println("HTTP server started");
}

void loop() {
    server.handleClient();
}