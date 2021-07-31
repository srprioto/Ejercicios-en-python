archivo = open("prueba.txt", "r")

archivo2 = open("copia.txt", "a", encoding="utf8")
archivo2.write(archivo.read())

archivo.close()
archivo2.close()