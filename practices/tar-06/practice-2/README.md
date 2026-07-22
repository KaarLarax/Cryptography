# TAR-06 Practica 2: PWM en D2

## Objetivo

Generar una salida PWM en el pin `D2` de la NodeMCU ESP8266 para variar gradualmente la intensidad de un LED o la salida de un actuador compatible.

## Motivo dentro de TAR-06

El reporte menciona modificar el codigo base para usar un LED externo en `D2`. Esta practica extiende esa manipulacion usando `analogWrite`, de modo que no solo se enciende/apaga la salida, sino que se observa una variacion gradual.

Reporte: [Tar06_Cripto.pdf](../../../homeworks/Tar06_Cripto.pdf)

## Hardware

- NodeMCU ESP8266.
- LED con resistencia o modulo conectado a `D2`.

## Funcionamiento

El programa configura `D2` como salida y recorre valores de `0` a `1022` con `analogWrite`, haciendo una pausa de 10 ms entre cambios.

## Ejecucion

```bash
cd practices/tar-06/practice-2
pio run
pio run --target upload
```

## Resultado esperado

La salida en `D2` cambia progresivamente. Si se conecta un LED, se observa una variacion gradual de brillo.
