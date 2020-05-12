import json
import tictactoeModificado
import hangman
import reversegam
import os
import PySimpleGUI as sg


def agregar_datos(nombre,opcion):
	if opcion == '1':
		juego_eleguido = 'ahorcado'
	elif opcion == '2':
		juego_eleguido = 'ta-te-ti'
	elif opcion == '3':
		juego_eleguido = 'otello'

	# archivo = open("datos.json","r")
	# datos = json.load(archivo)
	# datos[nombre].append(juego_eleguido)
	if nombre in datos:
		datos[nombre].append(juego_eleguido)
	else:
		datos[nombre] = [juego_eleguido]

def guardar_json():
	# archivo = open("datos.json","a")
	# json.dump(datos,archivo)
	# archivo.close()

	# datos_organizados = set(datos)
	# datos = [datos_organizados.copy()]
	with open('datos.json', 'w') as my_file:
		json.dump(datos, my_file, indent=4)



def main(args):
	sigo_jugando = True
	while sigo_jugando:
		layout = [
			[sg.Text('Elegí con qué juego querés jugar:'),sg.Radio('Ahorcado!', "RADIO1"), sg.Radio('TA-TE-TI', "RADIO1"),sg.Radio('Otello', "RADIO1")],
			[sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]

		]

		window = sg.Window('Juegos', layout)
		event, values = window.read()
		window.close()
		
		# print('''
		# Elegí con qué juego querés jugar:
		# 1.- Ahorcado
		# 2.- Ta-TE-TI
		# 3.- Otello
		# 4.- Salir''')

		# opcion = input()
		# opcion = values

		layout_input = [
			[sg.Text("Ingrese su nombre")],
			[sg.InputText()],
			[sg.Submit(tooltip='Click to submit this form'),sg.Cancel()]
		]

		if values[0]:
			# nombre = input("Ingrese su nombre\n")
			window = sg.Window('Juegos', layout_input)
			event, values = window.read()
			window.close()
			if event == "Cancel":
				break
			agregar_datos(values[0],'1')
			hangman.main()
		elif values[1]:
			# nombre = input("Ingrese su nombre\n")
			window = sg.Window('Juegos', layout_input)
			event, values = window.read()
			window.close()
			if event == "Cancel":
				break
			agregar_datos(values[0],'2')
			tictactoeModificado.main()
		elif values[2]:
			# nombre = input("Ingrese su nombre\n")
			window = sg.Window('Juegos', layout_input)
			event, values = window.read()
			window.close()
			if event == "Cancel":
				break
			agregar_datos(values[0],'3')
			reversegam.main()
		elif event == "Cancel":
			print(datos)
			guardar_json()
			window.close()
			sigo_jugando = False
			break
 

# with open('datos.json','r') as archivo:
#     datos = json.load(archivo)
datos = {}
archivo = open("datos.json")
datos = json.load(archivo)
archivo.close()

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
