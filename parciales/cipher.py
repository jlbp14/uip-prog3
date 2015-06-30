Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def menu():
	op=0
	while (op!=5):
		print ("1. Introducir un texto")
		print ("2. Cifrar texto")
		print ("3. Descifrar texto")
		print ("4. Imprimir texto")
		print ("5. Salir")
		op = int (input ("Elije una opcion: "))
		
		if (op==1):
			introducir ()
		if (op==2):
			cifrar ()
		if (op==3):
			descifrar ()
		if (op==4):
			imprimir ()
		if (op==4):
			salir ()

>>> def intoducir ():
	print ("Introducir un texto")

	
>>> def cifrar ():
	print ("Cifrar texto")

	
>>> def descifrar ():
	print ("Descifrar texto")

	
>>> def imprimir ():
	print ("Imprimir texto")

	
>>> def salir ():
	print ("Salir")

	
>>> menu()
1. Introducir un texto
2. Cifrar texto
3. Descifrar texto
4. Imprimir texto
5. Salir
Elije una opcion: 5
>>> def introducir ():
	lista[agua, botella]

	
>>> menu()
1. Introducir un texto
2. Cifrar texto
3. Descifrar texto
4. Imprimir texto
5. Salir
Elije una opcion: 1
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    menu()
  File "<pyshell#0>", line 12, in menu
    introducir ()
  File "<pyshell#18>", line 2, in introducir
    lista[agua, botella]
NameError: name 'lista' is not defined
>>> 
	
