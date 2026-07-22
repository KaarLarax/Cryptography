# TAR-06 Practica 1: LED integrado

## Objetivo

Controlar una salida digital en la NodeMCU ESP8266 usando el LED integrado de la placa.

## Motivo dentro de TAR-06

Esta practica funciona como el "Hola mundo HW": verificar que PlatformIO compila, carga el firmware y controla correctamente una salida fisica.

Reporte: [Tar06_Cripto.pdf](../../../homeworks/Tar06_Cripto.pdf)

## Funcionamiento

El programa configura `LED_BUILTIN` como salida. En el `loop`, cambia su estado cada segundo:

1. Enciende el LED.
2. Espera 1 segundo.
3. Apaga el LED.
4. Espera 1 segundo.

## Archivos

- `src/main.cpp`: logica principal del parpadeo.
- `platformio.ini`: configuracion para `nodemcuv2` con framework Arduino.

## Ejecucion

```bash
cd practices/tar-06/practice-1
pio run
pio run --target upload
```

## Resultado esperado

El LED integrado de la placa cambia de estado aproximadamente cada segundo.
