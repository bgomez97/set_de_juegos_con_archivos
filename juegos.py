import tictactoeModificado
import hangman
import reversegam
import json

def agregar_datos(nombre,opcion):
	if opcion == '1':
		juego_eleguido = 'ahorcado'
	elif opcion == '2':
		juego_eleguido = 'ta-te-ti'
	elif opcion == '3':
		juego_eleguido = 'otello'
	
	if nombre in datos:
		datos[nombre].append(juego_eleguido)
	else:
		datos[nombre] = [juego_eleguido]
	
# def guardar_json():
# 	json.dump(datos)


def main(args):
	sigo_jugando = True
	while sigo_jugando:
		
		print('''
		Elegí con qué juego querés jugar:
		1.- Ahorcado
		2.- Ta-TE-TI
		3.- Otello
		4.- Salir''')

		opcion = input()
		if opcion == '1':
			nombre = input("Ingrese su nombre\n")
			agregar_datos(nombre,'1')
			hangman.main()
		elif opcion == '2':
			nombre = input("Ingrese su nombre\n")
			agregar_datos(nombre,'2')
			tictactoeModificado.main()
		elif opcion == '3':
			nombre = input("Ingrese su nombre\n")
			agregar_datos(nombre,'3')
			reversegam.main()
		elif opcion == '4':
			sigo_jugando = False

datos = {}

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
