# Practicas de clase

Esta carpeta contiene ejercicios introductorios con NodeMCU ESP8266 usando PlatformIO y framework Arduino.

## Indice

| Carpeta | Descripcion |
| --- | --- |
| `practice-1-arduino/` | Conexion del ESP8266 a una red WiFi y reporte por Serial. |
| `practice-1-oled/` | Inicializacion de pantalla OLED SSD1306 y mensaje en pantalla. |
| `practice-2-arduino/` | Salida PWM en pin `D2` con valores crecientes. |

## Requisitos generales

- PlatformIO.
- NodeMCU ESP8266 (`nodemcuv2`).
- Cable USB de datos.
- Monitor serial a `9600` baudios cuando la practica imprime datos.

## Comandos PlatformIO

Ejecutar dentro de la carpeta de cada practica:

```bash
pio run
pio run --target upload
pio device monitor
```
