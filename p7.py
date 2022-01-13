from os import listdir

# load one file
#filename = 'txt_sentoken/neg/cv000_29416.txt'
# open the file as read only
#file = open(filename, 'r')
# read all text
#text = file.read()
# close the file
#file.close()

# ruta del las opniniones
path_positivas = 'txt_sentoken/pos/'
path_negativas = 'txt_sentoken/neg/'


def leer_opinion_positivas(path):
	dirs = listdir(path)	# Leemos los archivos en el directorio
	f = open('positivas.txt', 'w')
	for filename in dirs:	# Iteramos archivo por archivo
		print("Ruta completa", path+filename)
		print("Leido %s \n" % filename)	# Imprimimos
		# Abrimos el archivo en modo lectura
		file = open(path + filename, 'r')
		# Leemos el textop
		text = file.read()
		print(text)
		f.write(text)
		# Cerramos el archivo
		file.close()
		print("-------------------\n")
	f.close()
def leer_opinion_negativas(path):
	dirs = listdir(path)	# Leemos los archivos en el directorio
	f = open('negativas.txt', 'w')
	for filename in dirs:	# Iteramos archivo por archivo
		print("Ruta completa", path+filename)
		print("Leido %s \n" % filename)	# Imprimimos
		# Abrimos el archivo en modo lectura
		file = open(path + filename, 'r')
		# Leemos el textop
		text = file.read()
		print(text)
		f.write(text)
		# Cerramos el archivo
		file.close()
		print("-------------------\n")
	f.close()
print("--------OPNINIONES POSITIVAS---------\n")
leer_opinion_positivas(path_positivas)

print("--------OPNINIONES NEGATIVAS---------\n")
leer_opinion_negativas(path_negativas)
