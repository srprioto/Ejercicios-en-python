import os
os.system('cls')

from Cuadrado import Cuadrado

class Main:
    def __init__(self):
        cuadrado1 = Cuadrado(5, "azul")
        print(cuadrado1.ancho)
        print(cuadrado1.alto)
        print(cuadrado1.color)
        print(cuadrado1.calcularArea())

        print(Cuadrado.mro())


        


Main()


