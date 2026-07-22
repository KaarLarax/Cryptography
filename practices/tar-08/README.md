# TAR-08

Practica de integracion entre interrupciones externas, comunicacion Bluetooth por `SoftwareSerial` y pantalla OLED en NodeMCU ESP8266.

## Motivo de la tarea

El reporte `Tar08_Cripto` busca demostrar la ventaja de usar una ISR frente al polling tradicional. La interrupcion atiende un boton en tiempo real, mientras el `loop` mantiene la comunicacion Bluetooth y la retroalimentacion visual en OLED.

Reporte: [Tar08_Cripto.pdf](../../homeworks/Tar08_Cripto.pdf)

## Proyecto

- `Tar08-Bluetooh-ISR-Oled/`: firmware completo de la practica.

## Requisitos

- PlatformIO.
- NodeMCU ESP8266.
- Pantalla OLED SSD1306.
- Modulo Bluetooth serial, por ejemplo HC-05/HC-06.
- Boton o senal externa para disparar la interrupcion.
