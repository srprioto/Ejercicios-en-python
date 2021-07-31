from ManejoWith import ManejoWith

with ManejoWith('prueba.txt') as archivo:
    print(archivo.read())