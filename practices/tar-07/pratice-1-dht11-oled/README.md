# TAR-07 Practica 1: DHT11 con OLED

## Objetivo

Leer temperatura y humedad con un sensor DHT11 y mostrar las mediciones en una pantalla OLED SSD1306.

## Motivo dentro de TAR-07

Esta practica representa la medicion de variables discretas/cuantizadas: el DHT11 entrega lecturas digitales de temperatura y humedad que el microcontrolador valida y despliega en tiempo real.

Reporte: [Tar07_Cripto.pdf](../../../homeworks/Tar07_Cripto.pdf)

## Hardware

- NodeMCU ESP8266.
- Sensor DHT11 conectado al pin `D5`.
- Pantalla OLED SSD1306 128x64 por I2C.

## Conexion sugerida

| Componente | Pin/modulo | NodeMCU |
| --- | --- | --- |
| DHT11 | DATA | D5 |
| DHT11 | VCC | 3V3 |
| DHT11 | GND | GND |
| OLED | SCL | D1 |
| OLED | SDA | D2 |
| OLED | VCC | 3V3 |
| OLED | GND | GND |

## Archivos

- `src/main.cpp`: inicializa DHT11, Serial y OLED; luego actualiza temperatura y humedad.
- `platformio.ini`: incluye `DHT sensor library`, `Adafruit Unified Sensor`, `Adafruit SSD1306` y `Adafruit GFX Library`.

## Ejecucion

```bash
cd practices/tar-07/pratice-1-dht11-oled
pio run
pio run --target upload
pio device monitor
```

## Resultado esperado

La pantalla muestra primero un mensaje de presentacion. Despues lee el DHT11 y actualiza:

```text
Temperatura: <valor> C
Humedad: <valor> %
```

Si la lectura falla, la OLED muestra `Error al detectar el sensor DHT11`.

## Nota

El codigo contiene un `delay(100000)` despues del mensaje inicial, por lo que tarda alrededor de 100 segundos antes de entrar al ciclo de lecturas.
