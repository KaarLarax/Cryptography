# Practice 2 Arduino: PWM

## Objetivo

Generar una senal PWM en el pin `D2` de la NodeMCU ESP8266 y observar el incremento gradual del valor analogico escrito.

## Hardware

- NodeMCU ESP8266.
- LED con resistencia o modulo compatible conectado a `D2`.
- Cable USB.

## Archivos

- `src/main.cpp`: configura `D2` como salida y escribe valores PWM de `0` a `254`.
- `platformio.ini`: configuracion PlatformIO para `nodemcuv2`.

## Ejecucion

```bash
cd practices/class-practice/practice-2-arduino
pio run
pio run --target upload
pio device monitor
```

## Resultado esperado

El pin `D2` incrementa su ciclo de trabajo gradualmente. En el monitor serial se imprime el valor PWM actual a `9600` baudios.
