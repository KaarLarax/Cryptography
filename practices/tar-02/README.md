# TAR-02: Cifrado Vigenere A-Q

## Objetivo

Implementar un cifrado tipo Vigenere usando un alfabeto restringido de 17 letras: `A` a `Q`. Cada letra se transforma a un valor numerico (`A = 0`, `B = 1`, ..., `Q = 16`) y se cifra mediante suma modular.

## Motivo de la tarea

El reporte `Tar02_Cripto` plantea dos aprendizajes: reforzar estructuras de datos y funciones en Python, y aplicar esos conceptos para construir un cifrador derivado de lo visto en clase. La practica busca comprobar que el cifrado y descifrado de Vigenere funcionan con aritmetica modulo 17 y con la clave de prueba `HIJADE`.

Reporte: [Tar02_Cripto.pdf](../../homeworks/Tar02_Cripto.pdf)

## Archivos

- `main.py`: contiene las funciones de padding de clave, cifrado y descifrado.

## Funcionamiento

El algoritmo extiende la clave sobre las letras del texto con `_pad_key`. Los caracteres alfabeticos se cifran con:

```text
c = (m + k) mod 17
```

Para descifrar se invierte la operacion:

```text
m = (c - k) mod 17
```

Los caracteres no alfabeticos se conservan en su posicion y no consumen caracteres de la clave.

## Uso

El archivo define funciones, pero no incluye una interfaz por consola. Se puede probar desde una sesion interactiva de Python:

```bash
cd practices/tar-02
python
```

```python
from main import cifrar, descifrar

mensaje = "HOLA"
clave = "ABC"
cifrado = cifrar(mensaje, clave)
print(cifrado)
print(descifrar(cifrado, clave))
```

## Consideraciones

- El alfabeto esperado es `A-Q`; si se ingresan letras fuera de ese rango, el codigo igualmente calcula con base `A`, pero el resultado queda reducido modulo 17.
- Es una practica educativa de cifrado clasico, no un mecanismo seguro para informacion real.

## Casos del reporte

- `EL ANFIBIO CODIFICA LA BIBLIA` con clave `HIJADE`.
- `PON ALGODONCILLO EN LA ALMOHADILLA` con clave `HIJADE`.
