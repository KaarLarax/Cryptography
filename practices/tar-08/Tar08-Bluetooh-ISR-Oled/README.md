# TAR-08: Bluetooth, ISR y OLED

## Objetivo

Usar una interrupcion externa para disparar el envio de un mensaje por Bluetooth y mostrar estados/mensajes en una pantalla OLED.

## Motivo de la tarea

La practica integra tres ideas: respuesta inmediata a eventos externos mediante ISR, comunicacion Bluetooth bidireccional con un telefono Android y visualizacion clara del estado en OLED. El reporte destaca que la ISR debe ser breve y solo activar una bandera `volatile` para evitar bloqueos o reinicios por watchdog.

Reporte: [Tar08_Cripto.pdf](../../../homeworks/Tar08_Cripto.pdf)

## Hardware

- NodeMCU ESP8266.
- Pantalla OLED SSD1306 128x64 por I2C.
- Modulo Bluetooth serial.
- Boton o entrada externa conectada a `D7`.

## Pines usados

| Funcion | Pin NodeMCU |
| --- | --- |
| Interrupcion externa | D7 |
| Bluetooth RX/TX por `SoftwareSerial` | D5, D6 |
| OLED SCL | D1 |
| OLED SDA | D2 |

## Funcionamiento

1. La OLED muestra una pantalla inicial de la practica.
2. Se inicializa `SoftwareSerial` a `9600` baudios.
3. El pin `D7` se configura como `INPUT_PULLUP`.
4. La interrupcion se dispara en flanco de bajada (`FALLING`).
5. Cuando ocurre la interrupcion, el firmware muestra el estado en OLED y envia `Hola Carlos...` por Bluetooth.
6. Si llega texto por Bluetooth, se lee hasta salto de linea y se muestra en OLED.

## Ejecucion

```bash
cd practices/tar-08/Tar08-Bluetooh-ISR-Oled
pio run
pio run --target upload
pio device monitor
```

## Resultado esperado

Al activar la entrada en `D7`, la pantalla indica que la interrupcion fue activada y el telefono/dispositivo Bluetooth recibe el mensaje. Cuando el telefono envia texto, la OLED lo muestra temporalmente.

## Consideraciones

- El pin `D7` usa resistencia pull-up interna; el boton debe llevar el pin a GND para producir el flanco de bajada.
- Revisar el cruce RX/TX entre el ESP8266 y el modulo Bluetooth.
- Si una pulsacion envia varios mensajes, se debe al rebote mecanico del boton; una mejora seria agregar debounce por `millis()` o por hardware.
