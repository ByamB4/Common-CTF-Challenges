#!/usr/bin/env python
# ./stegb64.py <Steganography Base64>
# Autor: Hector Cuevas Cruz  (hecky)
# Web: http://neobits.org
# Ocultar por un mensaje por la tecnica Esteganorgafia Base64 de hecky http://neobits.org/?p=527
# Programado en Python2.6.6 y compilada con py2exe
# Contacto: hecky@neobits.org    twitter.com/hecky
# Github: www.github.com/hecky/
import sys,random

def main():
	try:
		if sys.argv[1]=="?" or sys.argv[1]=="-?" or sys.argv[1]=="/?" or sys.argv[1]=="-h" or sys.argv[1]=="-help" or sys.argv[1]=="--help":
			options()

		elif sys.argv[1]=="-t" or sys.argv[1]=="-T":
			try:
				archivo = sys.argv[2]
				bin1 = bin_dump(archivo)
				bin2 = bin_dump(ran_char(bin1))
				print b64_rule(bin_file(do_lsb(bin1,bin2)))
 			except IndexError:
				print "Falta ingresar el texto a esconder\n\t\t./stegb64.py -t <texto>"

		elif sys.argv[1]=="-f" or sys.argv[1]=="-F":
			try:
				try :
					archivo = open(sys.argv[2],"rb").read()
					if(len(archivo)>=10000):
						print "Loading..."
					bin1 = bin_dump(archivo)
					bin2 = bin_dump(ran_char(bin1))
					try:
						Salida = open(sys.argv[3],"wb")
						Salida.write(b64_rule(bin_file(do_lsb(bin1,bin2))))
						Salida.close()
						print "Se a ocultado "+sys.argv[2]+" dentro de "+sys.argv[3]
					except IndexError:
						print "Ingresa el nombre del archivo de Salida\n\t\t./stegb64.py -f <archivo> <Salida>"
				except IOError:
					print "No se encontro el archivo "+"\""+sys.argv[2]+"\"."+" Ingresa la ruta del archivo correcto"
				except KeyboardInterrupt:
					print "\nForzaste el cierre del programa\t\t\thttp://neobits.org"
			except IndexError:
				bad_input_f()
			return

		elif sys.argv[1]=="-r" or sys.argv[1]=="-R":
			try:
				print "\n"+bin_file(get_lsb(sys.argv[2]))
			except IndexError:
				print "Falta ingresar el texto stegb64 del cual se recuperara el mensaje\n\t\t./stegb64.py -r <stegb64>"

		elif sys.argv[1]=="-rf" or sys.argv[1]=="-RF":
			try:
				try :
					archivo = bin_file(get_lsb(open(sys.argv[2],"rb").read()))
					try:
						Salida = open(sys.argv[3],"wb")
						Salida.write(archivo)
						Salida.close()
						print "Se a recuperado el mensaje oculto en "+sys.argv[3]
					except IndexError:
						print "Ingresa el nombre del archivo de Salida\n\t\t./stegb64.py -rf <FileStegB64> <Salida>"
				except IOError:
					print "No se encontro el archivo "+"\""+sys.argv[2]+"\"."+" Ingresa la ruta del archivo correcto"
				except KeyboardInterrupt:
					print "\nForzaste el cierre del programa\t\t\thttp://neobits.org"
			except IndexError:
				bad_input_rf()
			return

		else:
			print "Elige una opcion valida\n\tOcultar:\n\t\t./stegb64.py -t <texto>\n\t\t./stegb64.py -f <archivo> <Salida>\n\tRecuperar\n\t\t./stegb64.py -r <stegB64>\n\t\t./stegb64.py -rf <FileStegB64> <Salida>"
	except IndexError:
		options()
	return


def bin_dump(archivo):
	binario1 = ""
	for i in archivo:
		binario1 += bin(ord(i))[2:].zfill(8)
	return binario1

def ran_char(binario1):
	caractalea = ""
	lista = ""
	for j in range(0,len(binario1),1):
		lista = random.sample([67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121],1)
		caractalea += chr(lista[0])
	return caractalea
	
def do_lsb(binario1,binario2):
	dellsb = ""
	bit = ""
	binariofinal = ""
	for l in range(0,len(binario2),8):
		dellsb = binario2[l:l+7]
		bit = binario1[l/8:(l/8)+1]
		binariofinal += dellsb + bit
	return binariofinal

def bin_file(binariofinal):
	final = ""
	for m in range(0,len(binariofinal),8):
		final += chr(int(binariofinal[m:m+8],2))
	return final

def b64_rule(final):
	if (len(sys.argv[2])%3)==0:
		rule = final
	elif (len(sys.argv[2])%3)==2:
		rule = final+"="
	else: #len(sys.argv[2])==1
		rule = final+"=="
	return rule

def get_lsb(archivo):
	bin_lsb = ""
	if (archivo[-1])=="=":
		archivo = archivo[:-1]
		if (archivo[-1])=="=":
			archivo = archivo[:-1]
		for i in archivo:
			bin_lsb += bin(ord(i))[2:].zfill(8)[-1]
	else:
		archivo = archivo
		for i in archivo:
			bin_lsb += bin(ord(i))[2:].zfill(8)[-1]
	return bin_lsb

def options():
	print "\t./stegb64.py\t\tEsteganografia Base64\n\nPrograma esteganografico que dada una cadena de texto o un archivo binario, lo oculta (LSB) en una cadena simulando ser Base64\n\n\tOcultar:\n\t\tUn texto e imprimirlo en pantalla\n\t\t\t./stegb64.py -t <texto>\n\t\tUn archivo binario y guardarlo en archivo salida\n\t\t\t./stegb64.py -f <archivo> <Salida>\n\n\tRecuperar:\n\t\tDe un texto stegB64 e imprimirlo en pantalla\n\t\t\t./stegb64.py -r <stegB64>\n\t\tApartir de un archivo stegB64 y formar una salida\n\t\t\t./stegb64.py -rf <FileStegB64> <Salida>\n\n\n<<Por hecky>>   @hecky\nhttp://neobits.org   hecky@neobits.org"
	return

def bad_input_f():
	print"Faltan Argumentos, revisa la sintaxis:\n\n\t\tOcultar un archivo binario y guardarlo en archivo salida\n\t\t./stegb64.py -f <archivo> <Salida>\n"
	return

def bad_input_rf():
	print"Faltan Argumentos, revisa la sintaxis:\n\n\t\tOcultar un archivo binario y guardarlo en archivo salida\n\t\t./stegb64.py -f <archivo> <Salida>\n"
	return

if __name__ == "__main__":
	main()
