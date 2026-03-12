import sys

class DES:
	def __init__(self):

		self.key = "1001100111" # observe que la clave es de 10 bits
		#sbox 0 provista
		self.s0 = [[1, 0, 3, 2],
					[3, 2, 1, 0],
					[0, 2, 1, 3],
					[3, 1, 3, 2]]
		#sbox 1 provista
		self.s1 = [[0, 1, 2, 3],
				     [2, 0, 1, 3],
				     [3, 0, 1, 0],
				     [2, 1, 0, 3]]

	#ingresa como una clave de 4bits (llamada binary)
	#el 1r y último indice resulta en el indice de la fila
	#el 2o y 3r indice resulta en el indice de la columna
	def getSboxEntry(self, binary,sbox):

		#el 1o y último indice indican el indice de la fila de la sbox
		row = binary[0] + binary[3]
		#el 2o y 3r indice indican el indice de la columna de la sbox
		col = binary[1] + binary[2]
		# convierte de una cadena binaria a un entero p/ambos
		row = int(row,2)
		col = int(col,2)
		if sbox == 0:
			binary = bin(self.s0[row][col])[2:]
			#asegura que no sea un binario de longitud 1 
			if len(binary) == 1:
				binary = "0" + binary
			return binary
		else:
			binary = bin(self.s1[row][col])[2:]
			#asegura que no sea un binario de longitud 1
			if len(binary) == 1:
				binary = "0" + binary
			return binary

	#expande la clave de 4 a 8 bits 
	def fFunction(self,key, k):
		#paso de expansión 
		expansion = key[3]+key[0]+key[1]+key[2]+key[1]+key[2]+key[3]+key[0]

		#hace XOR c/el 8o bit de la clave c/el 8o bit de la del generator de valor k
		XOR = bin((int(expansion,2)^int(k,2)))[2:]
		XOR = self.padding(XOR,8)

		left = XOR[:4]
		right = XOR[4:]

		#llama la fcn S p/obtener la entradas desde la sboxes
		S0 = self.getSboxEntry(left, 0)
		S1 = self.getSboxEntry(right, 1)

		#las concatena juntas
		p4 = S0 + S1

		#las permuta en el orden 2431 (nuevo número de 4 bits)
		p4 = p4[1]+p4[3]+p4[2]+p4[0]

		return p4

    # Dale una clave de 10 bits.
    # Permuta en el orden dado: 3, 5, 2, 7, 4, 10, 1, 9, 8, 6.
    # Divide la clave en una izquierda y una derecha.
    # Desplaza ambas claves a la izquierda (es decir, giras una vez a la izquierda y mueves la parte delantera a la trasera).
    # Combina los números y permuta con el orden para crear k1.
    # Vuelve a desplazar a la izquierda y combina los números sin permutar para crear k2.
	def kValueGenerator(self, key):
		#permuacion inicial 
		newKey = key[2] + key[4] + key[1] + key[6] + key[3] + key[9] + key[0] + key[8] + key[7] + key[5]
		#dividiendo la clave en la primera y segunda mitad
		left = newKey[0:5]
		right = newKey[5:]
		#desplazando la primera clave hacia la izquierda
		leftShift = left[1:] + left[0]
		#desplazando la segunda clave hacia la izquierda
		rightShift = right[1:] + right[0]

		#Creando k1 combinando los desplazamientos y la permutación
		k1 = leftShift + rightShift
		k1Permuted = k1[5] + k1[2] + k1[6] + k1[3] + k1[7] + k1[4] + k1[9] + k1[8]

		#Realizar un segundo desplazamiento a la izquierda en la primera clave
		leftShiftTwice = leftShift[1:] + leftShift[0]
		#Realizar un segundo desplazamiento a la izquierda en la segunda clave
		rightShiftTwice = rightShift[1:] + rightShift[0]

		#creando k1 combinando los nuevos turnos y permutando
		k2 = leftShiftTwice + rightShiftTwice
		k2Permuted = k2[5] + k2[2] + k2[6] + k2[3] + k2[7] + k2[4] + k2[9] + k2[8]

		#regresa k1 y k2
		return(k1Permuted,k2Permuted)

	#permuta la clave original según el orden dado 2 6 3 1 4 8 5 7
	def initialPermutation(self,key):
		newKey = key[1] + key[5] + key[2] + key[0] + key[3] + key[7] + key[4] + key[6]
		return newKey

	#Permuta el cifrado de nuevo a la permutación original
	def reversePermutation(self,key):
		newKey = key[3] + key[0] + key[2] + key[4] + key[6] + key[1] + key[7] + key[5]
		return newKey

    #Función que agrega relleno para garantizar que el binario tenga la longitud correcta. 
    #Por ejemplo, si se busca un binario de 4 bits y se obtiene 101, se convierte en 0101.
	def padding(self,string,length):
		if len(string) == length:
			return string
		while(len(string) < length):
			string = "0" + string
		return string

	#se ejecuta a través de una ronda de cifrado
	#el string @param es la clave de 8 bit 
	def Encryption(self,string):
		#pasa por una permutación inicial
		permString = self.initialPermutation(string)
		#se divide en dos cadenas de 4 bits, A y B
		left = permString[0:4]
		right = permString[4:]
		k1,k2 = self.kValueGenerator(self.key)

		firstFOutput = self.fFunction(right,k1)

		#hace XOR entre A y F(B,K1)
		firstXOR = bin((int(left,2)^int(firstFOutput,2)))[2:]
		firstXOR = self.padding(firstXOR, 4)
		secondFOutput = self.fFunction(firstXOR,k2)

		#hace XOR entre B y F(XOR(A,F(B,K1)),K2)
		secondXOR = bin((int(right,2)^int(secondFOutput,2)))[2:]
		secondXOR = self.padding(secondXOR, 4)
		output = secondXOR + firstXOR
		
		#invertir la permutación inicial
		output = self.reversePermutation(output)
		return output


	#pasa por una ronda de descifrado
	def Decryption(self,string):
		#pasa por una permutación inicial
		permString = self.initialPermutation(string)
		#se divide en dos cadenas de 4 bits, A y B
		left = permString[0:4]
		right = permString[4:]
		k1,k2 = self.kValueGenerator(self.key)

		firstFOutput = self.fFunction(right,k2)

		#hace XOR entre A y F(B,K1)
		firstXOR = bin((int(left,2)^int(firstFOutput,2)))[2:]
		firstXOR = self.padding(firstXOR, 4)
		secondFOutput = self.fFunction(firstXOR,k1)

		#hace XOR entre B y F(XOR(A,F(B,K1)),K2)
		secondXOR = bin((int(right,2)^int(secondFOutput,2)))[2:]
		secondXOR = self.padding(secondXOR, 4)
		output = secondXOR + firstXOR

		#invertir la permutación inicial
		output = self.reversePermutation(output)
		return output