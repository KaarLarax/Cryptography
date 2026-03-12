import socket
import des_e
import sys
from time import sleep
import library_e

# Esto servirá como "cliente" para nuestra implementación.
def Main():
        host = "127.0.0.1"
        port = 5001
        #necesario para conectarse al servidor
        mySocket = socket.socket()
        mySocket.connect((host,port))
        
        message = input("Introduzca el mensaje que desea cifrar -> ")
        #cifrando el mensaje usando DES
        finalEncryptedMessage = library_e.encrypt(message)
        print("Mensaje cifrado = " + finalEncryptedMessage)

        #hace q' la comunicación continúe para siempre
        while message != 'q':

                #Imprime la "clásica" barra de carga.
                library_e.sending()

                #cifrado del mensaje
                finalEncryptedMessage = library_e.encrypt(message)
                #envío del mensaje
                mySocket.send(finalEncryptedMessage.encode())
                #Recibir la respuesta del otro usuario
                data = mySocket.recv(1024).decode()
                print("Recibido del servidor = " + data)
                #descifrando el mensaje del otro usuario
                decryptedMessage = library_e.decrypt(data)
                if not data:
                        break
                print ("Mensaje descifrado = " + str(decryptedMessage))
                print("\n")
                #configurando el mensaje de nuevo...
                message = input("Introduzca el mensaje que desea cifrar -> ")
                finalEncryptedMessage = library_e.encrypt(message)
                print("Mensaje cifrado = " + finalEncryptedMessage)
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
