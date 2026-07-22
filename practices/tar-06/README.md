# TAR-06: Introduccion a PlatformIO y ESP8266

Practicas basicas de salida digital y PWM con NodeMCU ESP8266.

## Motivo de la tarea

El reporte `Tar06_Cripto` plantea una introduccion al Arduino Uno R4 WiFi y al uso de VS Code con PlatformIO. En la implementacion del repositorio, la actividad se adapto a NodeMCU ESP8266 para practicar la configuracion del entorno, la compilacion/carga del firmware, la lectura del pinout y la manipulacion de salidas digitales.

Reporte: [Tar06_Cripto.pdf](../../homeworks/Tar06_Cripto.pdf)

## Indice

| Carpeta | Tema |
| --- | --- |
| `practice-1/` | Parpadeo del LED integrado. |
| `practice-2/` | Salida PWM en `D2`. |

## Requisitos

- PlatformIO.
- NodeMCU ESP8266.
- Cable USB.

## Comandos

Entrar a la carpeta de la practica y ejecutar:

```bash
pio run
pio run --target upload
pio device monitor
```
