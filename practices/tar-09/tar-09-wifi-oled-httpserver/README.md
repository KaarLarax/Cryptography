# TAR-09: WiFi OLED HTTP Server

## Objetivo

Crear un servidor HTTP en una NodeMCU ESP8266 conectada a WiFi para controlar lo que se muestra en una pantalla OLED SSD1306 desde una pagina web.

## Motivo de la tarea

La practica demuestra una arquitectura cliente-servidor local: la NodeMCU escucha en el puerto `80`, el telefono Android abre un dashboard web y los botones envian comandos asincronos con `fetch()`. El reporte tambien analiza una evolucion hacia IoT global, donde el microcontrolador sincroniza estado con Firebase y el dashboard puede hospedarse fuera de la placa.

Reporte: [Tar09_Cripto.pdf](../../../homeworks/Tar09_Cripto.pdf)

## Hardware

- NodeMCU ESP8266.
- Pantalla OLED SSD1306 128x64 por I2C.
- Red WiFi.

## Pines sugeridos

| OLED | NodeMCU |
| --- | --- |
| SCL | D1 |
| SDA | D2 |
| VCC | 3V3 |
| GND | GND |

## Archivos

- `src/main.cpp`: inicializa OLED, conecta WiFi, levanta `ESP8266WebServer` y define rutas HTTP.
- `lib/WebPage/WebPage.h`: pagina HTML/CSS/JS embebida con botones `GEARS` y `HALO`.
- `platformio.ini`: configuracion de PlatformIO y dependencias.
- `secrets.h`: archivo local requerido para credenciales WiFi. No esta versionado.

## Configuracion de credenciales

Crear un archivo `include/secrets.h` o un `secrets.h` accesible por el include path de PlatformIO con este contenido:

```cpp
#pragma once

#define WIFI_SSID_SECRET "nombre_de_tu_wifi"
#define WIFI_PASSWORD_SECRET "password_de_tu_wifi"
```

No commitear credenciales reales.

## Rutas HTTP

| Ruta | Metodo | Accion |
| --- | --- | --- |
| `/` | GET | Devuelve la pagina web con botones. |
| `/gears` | GET | Dibuja el logo GEARS en la OLED. |
| `/halo` | GET | Dibuja el logo HALO en la OLED. |

## Ejecucion

```bash
cd practices/tar-09/tar-09-wifi-oled-httpserver
pio run
pio run --target upload
pio device monitor
```

Cuando el monitor serial/OLED muestre la IP, abrir en el navegador:

```text
http://<ip-del-esp8266>/
```

## Resultado esperado

La pagina muestra dos botones. Al presionar `GEARS` o `HALO`, el navegador envia una peticion al ESP8266 y la OLED actualiza el dibujo correspondiente.

## Consideraciones

- El servidor escucha en el puerto `80`.
- La OLED usa direccion I2C `0x3C`.
- La pagina web se sirve desde memoria de programa como cadena constante.
- La version embebida funciona dentro de la misma red local. Para acceso desde internet, el reporte propone una arquitectura con Firebase, autenticacion y dashboard externo.
