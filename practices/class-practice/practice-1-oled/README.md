# Practice 1 OLED

## Objetivo

Inicializar una pantalla OLED SSD1306 por I2C y mostrar un mensaje simple desde una NodeMCU ESP8266.

## Hardware

- NodeMCU ESP8266.
- Pantalla OLED SSD1306 de 128x64.
- Conexion I2C.

## Archivos

- `src/main.cpp`: configura la pantalla en la direccion `0x3C` y escribe texto.
- `platformio.ini`: dependencias de `Adafruit SSD1306` y `Adafruit GFX Library`.

## Conexion sugerida

| OLED | NodeMCU ESP8266 |
| --- | --- |
| VCC | 3V3 |
| GND | GND |
| SCL | D1 |
| SDA | D2 |

## Ejecucion

```bash
cd practices/class-practice/practice-1-oled
pio run
pio run --target upload
pio device monitor
```

## Resultado esperado

La OLED muestra:

```text
Hola mundo. :)
Desde la NodeMCU 8266
```

Si la pantalla no se detecta, el monitor serial imprime `OLED no encontrada` y el programa se detiene.
