# MiniDES

## Objetivo

Contener la implementacion base de MiniDES usada para cifrar mensajes ASCII, transmitirlos por sockets TCP y descifrarlos del otro lado.

## Motivo de la tarea

Esta carpeta corresponde al analisis de MiniDES de `Tar03_Cripto`. El motivo de la practica fue ejecutar el cliente y servidor, observar el efecto avalancha al cifrar caracteres cercanos como `B` y `C`, estudiar las S-boxes, la funcion `f`, las expansiones/permutaciones y verificar manualmente el cifrado de un bloque.

Reporte: [Tar03_Cripto.pdf](../../homeworks/Tar03_Cripto.pdf)

## Archivos

- `des_e.py`: clase `DES` con permutaciones, S-boxes, funcion de ronda y generacion de subclaves.
- `library_e.py`: funciones auxiliares para ASCII/binario, bloques de 8 bits, cifrado y descifrado.
- `server_e.py`: servidor local TCP.
- `client_e.py`: cliente local TCP.
- `leame1o_e.txt`: explicacion original de uso.

## Ejecucion

Abrir dos terminales en esta carpeta.

Servidor:

```bash
cd practices/mini-des
python server_e.py
```

Cliente:

```bash
cd practices/mini-des
python client_e.py
```

El cliente cifra el mensaje antes de enviarlo. El servidor recibe la cadena binaria cifrada, la descifra y permite responder con otro mensaje cifrado.

## Detalles tecnicos

- Host: `127.0.0.1`.
- Puerto: `5001`.
- Bloque: 8 bits.
- Clave maestra por defecto: `1001100111`.
- Subclaves: dos claves de 8 bits derivadas de la clave maestra.
- Estructura: red Feistel de dos rondas.

## Consideraciones

Esta practica es educativa. La clave de 10 bits permite ataques exhaustivos muy rapidos y no ofrece seguridad real.

## Aprendizajes del reporte

- MiniDES ayuda a entender la estructura de cifradores por bloques como DES.
- Las S-boxes aportan sustitucion no lineal.
- La expansion, XOR y permutacion redistribuyen bits para producir confusion y difusion.
- El descifrado reutiliza la misma estructura aplicando las subclaves en orden inverso.
