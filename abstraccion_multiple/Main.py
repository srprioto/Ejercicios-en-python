import os
os.system('cls')

from Rectangulo import Rectangulo
from Cuadrado import Cuadrado

class Main:

    def __init__(self):

        print("Cuadrado".center(50, "-"))
        cuad = Cuadrado(5, "azul")
        print(f"Area del cuadrado: {cuad.area()}")
        print(cuad)

        print()

        print("Cuadrado".center(50, "-"))
        rect = Rectangulo(6, 5, "rojo")        
        print(f"Area del rectangulo: {rect.area()}")
        print(rect)
        



Main()