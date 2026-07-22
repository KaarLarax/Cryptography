# TAR-05: MiniDES, sockets y fuerza bruta

## Objetivo

Implementar un cifrado educativo tipo DES simplificado, usarlo para comunicar cliente y servidor por sockets TCP, y demostrar por fuerza bruta por que una clave de 10 bits es insegura.

## Motivo de la tarea

El reporte `tar05_Cripto` parte de la vulnerabilidad central de MiniDES: una clave de 10 bits solo produce `2^10 = 1024` combinaciones. La practica busca recuperar la clave usada, medir el tiempo del ataque, discutir la complejidad `O(2^n)` y relacionar el tamano de llave con algoritmos reales como DES y AES.

Reporte: [tar05_Cripto.pdf](../../homeworks/tar05_Cripto.pdf)

## Archivos

- `des_e.py`: implementacion de MiniDES con red Feistel de dos rondas, S-boxes, permutaciones y generacion de subclaves.
- `library_e.py`: utilidades para convertir ASCII/binario, partir bloques de 8 bits, cifrar y descifrar mensajes completos.
- `server_e.py`: servidor TCP en `127.0.0.1:5001`.
- `client_e.py`: cliente TCP que se conecta al servidor y envia mensajes cifrados.
- `brute_force_attack.py`: prueba todas las claves posibles de 10 bits hasta encontrar la que descifra el texto conocido.
- `leame1o_e.txt`: notas originales de ejecucion y referencias.

## Como funciona MiniDES

MiniDES trabaja con bloques de 8 bits y una clave maestra de 10 bits. La clave fija por defecto es:

```text
1001100111
```

Durante el cifrado:

1. El texto ASCII se convierte a binario.
2. El binario se divide en bloques de 8 bits.
3. Cada bloque pasa por una permutacion inicial.
4. Se ejecutan dos rondas Feistel usando subclaves de 8 bits.
5. Se aplica la permutacion inversa.
6. Los bloques cifrados se concatenan.

El descifrado usa la misma estructura, pero aplica las subclaves en orden inverso.

## Ejecucion cliente-servidor

Abrir dos terminales dentro de esta carpeta.

Terminal 1:

```bash
cd practices/tar-05
python server_e.py
```

Terminal 2:

```bash
cd practices/tar-05
python client_e.py
```

El cliente pide un mensaje, lo cifra en binario y lo envia al servidor. El servidor muestra el texto cifrado recibido, lo descifra y permite responder con otro mensaje cifrado.

Para terminar la conversacion desde el cliente, escribir `q`.

## Ataque de fuerza bruta

El archivo `brute_force_attack.py` cifra mensajes de prueba y recorre todas las claves posibles:

```bash
cd practices/tar-05
python brute_force_attack.py
```

Como la clave tiene 10 bits, el espacio total es:

```text
2^10 = 1024 claves
```

El objetivo de esta prueba es comprobar que un atacante puede recuperar la clave rapidamente cuando el espacio de busqueda es pequeno.

En el reporte se documenta la recuperacion de la clave `1001100111`, equivalente a `615` en decimal, en menos de un segundo.

## Aprendizajes

- Relacion entre tamano de clave y resistencia a fuerza bruta.
- Uso de una red Feistel para cifrado y descifrado.
- Conversion de mensajes ASCII a bloques binarios.
- Envio de informacion cifrada sobre TCP.

## Consideraciones

MiniDES es un algoritmo didactico. No debe usarse para proteger informacion real.
