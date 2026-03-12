import des_e
from time import sleep
import sys 

#Función que convierte binario a ascii
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

#Función que convierte ASCII a binario
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

#Función a la que se le da una cadena de longitud n 
# y una longitud especificada m 
# y devuelve una lista de subcadenas de longitud m
def splitIntoGroups(string,length):
    results = []
    loc = 0
    temp = ""
    while(loc < len(string)):
        temp += string[loc]
        loc += 1
        if loc % length == 0:
            results.append(temp)
            temp = ""
    return results

#Función que toma el binario cifrado 
# y lo convierte en texto descifrado.
def decrypt(message):
    #llama a la clase DES
    toy = des_e.DES()
    #dividir el binario en fragmentos de 8 bits (necesarios para la clase DES)
    entries = splitIntoGroups(message,8)
    decryptedMessages = []
    #descifrar cada fragmento (chunk) individual
    for i in range(len(entries)):
        decryption = toy.Decryption(entries[i])
        decryptedMessages.append(decryption)
    #concatenar los descifrados
    decryptedMessage ="".join(decryptedMessages)
    #pasar de binario a ASCII
    decryptedMessage = text_from_bits(decryptedMessage)
    return decryptedMessage

#Función que toma un texto ASCII 
# y lo convierte en binario cifrado.
def encrypt(message):
    #llama a la clase DES
    toy = des_e.DES()
    #convertir el ascii a binario
    binary = text_to_bits(message)
    #dividir el binario en fragmentos de 8 bits (necesarios para la clase DES)

    entries = splitIntoGroups(binary,8)

    encryptedEntries = []
    #cifrar cada fragmento (chunk) individual
    for i in range(len(entries)):
        encryptedMessage = toy.Encryption(entries[i])
        encryptedEntries.append(encryptedMessage)
    #concatenar los cifrados
    finalEncryptedMessage = "".join(encryptedEntries)
    return finalEncryptedMessage

#Función que imprime una "clásica" barra 
# de carga para enviar los mensajes.
def sending():
    print("\Enviando ",end = "")
    for j in range(5):
        sleep(0.4)
        print(".", end = "")
        sys.stdout.flush()
    print(' ENVIADO')