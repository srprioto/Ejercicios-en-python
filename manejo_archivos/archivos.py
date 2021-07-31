try:
    archivo = open('prueba.txt', 'a', encoding='utf-8')
    archivo.write("texto linea gran tamaño 1\n")
    archivo.write("adios\n")

except Exception as e:
    print(e)
finally:
    archivo.close()
