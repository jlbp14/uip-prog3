Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def agregar ():
	print ("agregar a la lista")

	
>>> def opcion_b ():
	print ("Eliminar de la lista")

	
>>> def opcion_c ():
	print ("Ver la lista")

	
>>> def opcion_d ():
	print ("Salir")

	
>>> def menu():
	op=0
	while (op!=4):
		print ("1. Agregar")
		print ("2. Eliminar")
		print ("3. Ver")
		print ("4. Salir")
		op = int (raw_input ("Elije una opcion: "))
		if (op==1):
			agregar ()
		if (op==2):
			opcion_b ()
		if (op==3):
			opcion_c ()
		if (op==4):
			opcion_d ()


>>> 
