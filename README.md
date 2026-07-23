# Criptografia

Repositorio de practicas y proyecto final de la materia de Criptografia. El contenido esta organizado por carpetas para separar ejercicios de algoritmos criptograficos en Python, practicas de IoT con ESP8266/NodeMCU y el proyecto final de casa inteligente con cifrado.

## Estructura

```text
.
├── practices/
│   ├── tar-02/                  # Cifrado Vigenere con alfabeto A-Q
│   ├── tar-05/                  # MiniDES, sockets y fuerza bruta
│   ├── mini-des/                # Variante/base de MiniDES cliente-servidor
│   ├── class-practice/          # Practicas introductorias de clase
│   ├── tar-06/                  # LED digital y PWM con ESP8266
│   ├── tar-07/                  # DHT11/OLED y divisor de voltaje
│   ├── tar-08/                  # Bluetooth, interrupciones y OLED
│   └── tar-09/                  # Servidor HTTP WiFi que controla OLED
├── homeworks/                   # Reportes entregables en PDF/DOCX
└── final project/               # Proyecto final Smart Home Cripto
```

Los reportes de `homeworks/` se usaron como fuente para documentar el motivo de cada practica: objetivos, planteamiento del problema, metodologia y conclusiones.

## Requisitos generales

- Python 3 para las practicas criptograficas.
- PlatformIO para las practicas con ESP8266/NodeMCU.
- NodeMCU ESP8266 para las practicas embebidas.
- Monitor serial configurado normalmente a `9600` baudios, salvo que una practica indique otra velocidad.
- Flutter y PlatformIO para el proyecto final.

## Practicas documentadas

- [Practicas](practices/README.md)
- [TAR-02: Vigenere A-Q](practices/tar-02/README.md)
- [TAR-03: MiniDES](practices/mini-des/README.md)
- [TAR-05: MiniDES, sockets y fuerza bruta](practices/tar-05/README.md)
- [Practicas de clase](practices/class-practice/README.md)
- [TAR-06](practices/tar-06/README.md)
- [TAR-07](practices/tar-07/README.md)
- [TAR-08](practices/tar-08/README.md)
- [TAR-09](practices/tar-09/README.md)
- [Proyecto final](https://github.com/KaarLarax/smart-home-cripto)

## Reportes PDF

- [Tar01_Cripto.pdf](homeworks/Tar01_Cripto.pdf)
- [Tar02_Cripto.pdf](homeworks/Tar02_Cripto.pdf)
- [Tar03_Cripto.pdf](homeworks/Tar03_Cripto.pdf)
- [tar05_Cripto.pdf](homeworks/tar05_Cripto.pdf)
- [Tar06_Cripto.pdf](homeworks/Tar06_Cripto.pdf)
- [Tar07_Cripto.pdf](homeworks/Tar07_Cripto.pdf)
- [Tar08_Cripto.pdf](homeworks/Tar08_Cripto.pdf)
- [Tar09_Cripto.pdf](homeworks/Tar09_Cripto.pdf)

## Comandos frecuentes

Para Python:

```bash
python main.py
python server_e.py
python client_e.py
```

Para PlatformIO, ejecutar dentro de la carpeta de cada proyecto:

```bash
pio run
pio run --target upload
pio device monitor
```

## Notas de seguridad

Las implementaciones como Vigenere y MiniDES son educativas. No deben usarse para proteger informacion real. En las practicas de WiFi o Firebase, las credenciales deben mantenerse fuera del repositorio mediante archivos locales de secretos.
