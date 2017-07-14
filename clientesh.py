# Este programa realiza una simulacion de clientes
import os
#libreria para generar una pausa en el programa
print('Clientes 1.0')

sel=99

clientes = ['caro','ivette']

while(sel!=0):
	print(' ')
	print('*******************************')
	print('*      Menu de Opciones:      *')
	print('*                             *')
	print('*  1 Agregar un cliente       *')
	print('*  2 Eliminar clientes        *')
	print('*  3 Ver un cliente           *')
	print('*  4 Ver todos los clientes   *')
	print('*  5 Actualizar un cliente    *')
	print('*  0 Salir                    *')
	print('*******************************')
	print(' ')
	
	sel=int(input('Ingrese el numero de la opcion del menu que desea ejecutar: '))
	
	
	if sel == 1:
		print(' ')
		print('Ha elegido la opcion de agregar un cliente')
		a=input('Ingrese el nombre del cliente que desea agregar: ')
		clientes.append(a)
		print('El cliente: ',a,' a sido añadido correctamente')
		print(' ')
		os.system('pause') 

	elif sel==2:
		print(' ')
		print('Ha elegido la opcion de eliminar un cliente')
		print(' ')
		if len(clientes)>0:
			sel2=99
			while sel2!=3:
				print(' ')
				print('Lista de clientes:')
				for i in range(len(clientes)):
					print('Cliente ',i,' : ', clientes[i])
				print(' ')
				print('Menu de opciones de eliminacion de cliente')
				print('1 Eliminar cliente por indice')
				print('2 Eliminar cliente por nombre')
				print('3 Regresar al menu principal sin eliminar a un cliente')
				print(' ')
				sel2=int(input('Ingrese el numero de la opcion del menu que desea ejecutar: '))
				if sel2==1:
					print(' ')
					indice=int(input('Ingrese el numero del cliente que desea eliminar: '))
					if indice<len(clientes):
						print('El cliente: ',clientes[indice],' ha sido eliminado correctamente')
						clientes.pop(indice)
					else:
						print('No existe ningun cliente con dicho indice')
				elif sel2==2:
					clienteeliminado=input('Ingrese el nombre del cliente que desea eliminar: ')
					if clientes.count(clienteeliminado)>0:
						print ('Se ha eliminado exitosamente a ',clienteeliminado)
						clientes.remove(clienteeliminado)
					else:
						print('El nombre que usted tecleo no se encuentra en la lista')
					print(' ')
				elif sel2==3:
					print('Ha elegido salir al menu principal')
				else:
					print('opcion no valida, intente de nuevo con una opcion del menu')	
		else:
			print('La lista de clientes se encuentra vacia, por favor inserte algun cliente antes de intentar eliminar')
		print('')
		os.system('pause')	
			 
		
	elif sel==3:
		if len(clientes)>0:
			print(' ')
			print('Ha elegido la opcion de ver un cliente')
			print(' ')
			buscarc=int(input('ingrese el numero de cliente que desea buscar: '))
			if buscarc<len(clientes):
				print('El cliente con el indice ',buscarc,' es: ',clientes[buscarc])
				print(' ')
			else:
				print('No existe ningun cliente con ese numero')
				print(' ')
		else:
			print('La lista de clientes se encuentra vacia, por favor inserte algun cliente')
			print(' ')
		os.system('pause') 
		
	elif sel==4:
		print(' ')
		print('Ha elegido la opcion de ver todos los clientes')
		print(' ')
		if len(clientes)>0:
			for i in range(len(clientes)):
				print('Cliente ',i,' : ', clientes[i])
			print(' ')
		else:
			print('La lista de clientes se encuentra vacia, por favor inserte algun cliente')
		os.system('pause')
	elif sel==5:
		if len(clientes)>0:
			print('Ha elegigo la opcion de actualizar un cliente')
			act=int(input('Ingrese el numero del cliente que desea actualizar: '))
			if act<len(clientes):
				print('Actualmente el cliente con ese indice es: ',clientes[act])
				nuevo=input('Ingrese el nuevo nombre del cliente: ')
				print('El cliente ',act,' : ',clientes[act],' ha sido actualizado por el nombre: ',nuevo)
				clientes[act]=nuevo
			else:
				print('No existe ningun cliente con dicho indice')
		else:
			print('La lista de clientes se encuentra vacia, por favor inserte algun cliente')
		os.system('pause') 
		
	elif sel==0:
		print(' ')
		print('Gracias por utilizar el programa, Adios')
		os.system('pause') 
	
	else:
		print(' ')
		print("Opcion no valida, por favor teclee una opcion del menu")
		os.system('pause') 
		