# TAR-07: Variables continuas y discretas

Practicas con sensores analogicos/digitales y pantalla OLED SSD1306 en NodeMCU ESP8266.

## Motivo de la tarea

El reporte `Tar07_Cripto` se centra en medir variables discretas y continuas. La parte discreta se trabaja con el DHT11, que entrega temperatura y humedad como datos digitales ya procesados. La parte continua se aborda con un divisor de voltaje conectado a `A0`, cuidando las limitaciones del ADC de 10 bits de la ESP8266.

Reporte: [Tar07_Cripto.pdf](../../homeworks/Tar07_Cripto.pdf)

## Indice

| Carpeta | Tema |
| --- | --- |
| `pratice-1-dht11-oled/` | Lectura de temperatura y humedad con DHT11, mostrada en OLED. |
| `practice-2-volt-divisor/` | Lectura analogica de un divisor de voltaje y visualizacion en OLED. |

## Requisitos

- PlatformIO.
- NodeMCU ESP8266.
- Pantalla OLED SSD1306 128x64 por I2C.
- Librerias Adafruit declaradas en cada `platformio.ini`.

## Comandos

```bash
pio run
pio run --target upload
pio device monitor
```
