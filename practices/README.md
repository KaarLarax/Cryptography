# Practicas

Esta carpeta agrupa las practicas desarrolladas durante el curso. Hay dos tipos principales:

- Practicas de criptografia en Python, enfocadas en cifrados clasicos, MiniDES y ataques por fuerza bruta.
- Practicas embebidas con ESP8266/NodeMCU usando PlatformIO, sensores, OLED, Bluetooth, WiFi y servidor HTTP.

## Indice

| Carpeta | Tema | Tecnologia principal |
| --- | --- | --- |
| `tar-02/` | Cifrado Vigenere con alfabeto restringido A-Q | Python |
| `mini-des/` | TAR-03: analisis de MiniDES con sockets | Python |
| `tar-05/` | MiniDES, cliente-servidor TCP y fuerza bruta | Python |
| `class-practice/` | Ejercicios introductorios de clase | PlatformIO, ESP8266 |
| `tar-06/` | Salida digital y PWM | PlatformIO, ESP8266 |
| `tar-07/` | Lectura de sensores con OLED | PlatformIO, ESP8266 |
| `tar-08/` | Bluetooth, interrupcion externa y OLED | PlatformIO, ESP8266 |
| `tar-09/` | WiFi y servidor HTTP para mostrar logos en OLED | PlatformIO, ESP8266 |

## Reportes

| Tarea | Reporte PDF |
| --- | --- |
| Tar01 | [Tar01_Cripto.pdf](../homeworks/Tar01_Cripto.pdf) |
| Tar02 | [Tar02_Cripto.pdf](../homeworks/Tar02_Cripto.pdf) |
| Tar03 | [Tar03_Cripto.pdf](../homeworks/Tar03_Cripto.pdf) |
| Tar05 | [tar05_Cripto.pdf](../homeworks/tar05_Cripto.pdf) |
| Tar06 | [Tar06_Cripto.pdf](../homeworks/Tar06_Cripto.pdf) |
| Tar07 | [Tar07_Cripto.pdf](../homeworks/Tar07_Cripto.pdf) |
| Tar08 | [Tar08_Cripto.pdf](../homeworks/Tar08_Cripto.pdf) |
| Tar09 | [Tar09_Cripto.pdf](../homeworks/Tar09_Cripto.pdf) |

## Flujo recomendado

1. Abrir la carpeta de la practica.
2. Leer su `README.md`.
3. Revisar `src/main.cpp` o los archivos `.py` segun corresponda.
4. Ejecutar localmente o cargar al microcontrolador.
5. Comparar el resultado con el comportamiento esperado documentado.

## Convenciones

Los proyectos PlatformIO mantienen la estructura estandar:

- `platformio.ini`: tarjeta, framework y dependencias.
- `src/main.cpp`: programa principal.
- `include/`, `lib/`, `test/`: carpetas estandar generadas por PlatformIO.

Los proyectos Python se ejecutan desde su propia carpeta para que los imports locales funcionen correctamente.

## Relacion con reportes

Los archivos de `homeworks/` explican el motivo academico de cada tarea:

- `Tar01`: ejercicios del capitulo 1 sobre cifrados clasicos, AES, contrasenas y aritmetica modular. No tiene carpeta de codigo asociada.
- `Tar02`: practica de Python y Vigenere con alfabeto A-Q.
- `Tar03`: analisis de MiniDES, efecto avalancha, S-boxes, funcion de ronda y cifrado manual.
- `Tar05`: ataque de fuerza bruta sobre MiniDES y analisis de escalabilidad.
- `Tar06`: introduccion a Arduino Uno R4 WiFi/PlatformIO, adaptada a NodeMCU ESP8266.
- `Tar07`: medicion de variables discretas y continuas con DHT11, OLED y divisor de voltaje.
- `Tar08`: Bluetooth e interrupciones de hardware con retroalimentacion OLED.
- `Tar09`: servidor HTTP embebido por WiFi y comparacion con una arquitectura IoT en la nube.
