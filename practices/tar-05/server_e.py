import socket
import des_e
import library_e

#Esto servirá como "servidor" para nuestra implementación.

def Main():
    host = "127.0.0.1"
    port = 5001
    #necesario para iniciar el servidor
    mySocket = socket.socket()
    mySocket.bind((host,port))

    print("Esperando conexión.....")
    #escucha a un usuario p/conectar
    mySocket.listen(2)
    #obtener la información de conexión del usuario
    conn, addr = mySocket.accept()
    print ("Conexión desde: " + str(addr))

    while True:
            #Recibir la respuesta del otro usuario
            data = conn.recv(1024).decode()
            print("Recibido del cliente = " + data)
            #descifrando el mensaje del otro usuario
            decryptedMessage = library_e.decrypt(data)
            if not data:
                    break
            print ("Mensaje descifrado = " + str(decryptedMessage))
            print("\n")
            message = input("Introduzca el mensaje que desea cifrar -> ")
            #cifrando el mensaje usando DES
            finalEncryptedMessage = library_e.encrypt(message)
            print("Mensaje cifrado = " + finalEncryptedMessage)
            #Imprime la "clásica" barra de carga.
            library_e.sending()
            #enviando el msj
            conn.send(finalEncryptedMessage.encode())
 
    conn.close()
     
if __name__ == '__main__':
    Main()





