print  ('programa para administrar carteras de clientes')
menu=6
clientes = []
while menu!=0:
	print (' ')
	print (' menu de opciones')
	print ('1 agregar un cliente')
	print ('2 eliminar clientes')
	print ('3 ver un cliente')
	print ('4 ver todos los clientes')
	print ('5 actualizar un cliente')	
	print ('0 salir')
	print (' ')

	menu = int(input('seleccione una opcion del menu, por favor:')) 
	
	if menu == 1:
		print ('Agregar clientes ')
		a = input('agregar nombre del cliente: ')
		clientes.append(a) 
		print('se añadido el cliente: ',a)
		print (' ')
		
	elif menu == 2:
		print ('Eliminar clientes')
		
	elif menu == 3:
		print ('Visualizar un cliente')
		buscarc = int(input('ingrese el numero de cliente, por favor:'))
		print (clientes[buscarc])

	elif menu == 4:
		print ('Visualizar todos los clientes')
		print (' ')
		for i in range(len(clientes)):
			print ('cliente ',i,' : ', clientes[i])
		print (' ')
	
	elif menu == 5:
		print ('actualizar un cliente')
		act=int(input ('ingrese el numero de cliente que desea actualizar: '))
		nuevo=input ('ingrese el nuevo nombre de cliente: ')
		clientes[act]=nuevo
		
	elif menu == 0:
	    print ('Adios')
	else: 
	    print ('opcion no valida')
