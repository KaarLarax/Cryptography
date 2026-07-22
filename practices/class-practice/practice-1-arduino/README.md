# Practice 1 Arduino: Conexion WiFi

## Objetivo

Conectar una NodeMCU ESP8266 a una red WiFi en modo estacion (`WIFI_STA`) y mostrar el estado de conexion por el monitor serial.

## Hardware

- NodeMCU ESP8266.
- Cable USB.
- Red WiFi configurada en el codigo.

## Archivos

- `src/main.cpp`: inicializa Serial, configura WiFi, espera conexion e imprime la IP asignada.
- `platformio.ini`: proyecto PlatformIO para `nodemcuv2`.

## Configuracion

Las credenciales estan declaradas en `src/main.cpp`:

```cpp
const char* ssid = "espai13-10";
const char* password = "1234567890";
```

Cambiar esos valores antes de cargar el firmware si se usara otra red.

## Ejecucion

```bash
cd practices/class-practice/practice-1-arduino
pio run
pio run --target upload
pio device monitor
```

## Resultado esperado

El monitor serial muestra la red objetivo, puntos mientras conecta, el mensaje `WiFi connected`, la IP local y luego `Still connected...` cada 2 segundos.
