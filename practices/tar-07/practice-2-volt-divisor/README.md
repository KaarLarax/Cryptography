# TAR-07 Practica 2: Divisor de voltaje con OLED

## Objetivo

Leer una entrada analogica en `A0`, convertirla a voltaje aproximado y mostrar el valor en una pantalla OLED SSD1306.

## Motivo dentro de TAR-07

Esta practica representa la medicion de una variable continua mediante un divisor de voltaje. El objetivo no es solo leer `A0`, sino entender que el valor analogico se aproxima con el ADC de 10 bits de la ESP8266 y que el rango electrico real depende de la placa.

Reporte: [Tar07_Cripto.pdf](../../../homeworks/Tar07_Cripto.pdf)

## Hardware

- NodeMCU ESP8266.
- Divisor de voltaje o senal analogica compatible con `A0`.
- Pantalla OLED SSD1306 128x64 por I2C.

## Conexion sugerida

| Componente | NodeMCU |
| --- | --- |
| Salida del divisor | A0 |
| Tierra comun | GND |
| OLED SCL | D1 |
| OLED SDA | D2 |
| OLED VCC | 3V3 |
| OLED GND | GND |

## Funcionamiento

El programa lee:

```cpp
input = int(analogRead(A0));
val = 1.00f * input * (3.3 / 1023.0);
```

Luego muestra en la OLED el valor crudo del ADC y el voltaje calculado.

## Ejecucion

```bash
cd practices/tar-07/practice-2-volt-divisor
pio run
pio run --target upload
pio device monitor
```

## Resultado esperado

Cada 3 segundos la pantalla actualiza:

```text
Valor: <lectura ADC>
Voltaje: <voltaje>
```

## Consideraciones

Verificar el rango permitido por `A0` en la placa usada. Algunas placas NodeMCU aceptan hasta 3.3 V en `A0`, pero el ESP8266 interno trabaja con un rango menor.
