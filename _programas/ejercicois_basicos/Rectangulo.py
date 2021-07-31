import os
os.system('cls')

class Rectangulo:

    def __init__(self, b, h):
        self.base = b
        self.altura = h

    def calcular(self):
        # restangulo A = b*h
        return self.base * self.altura

    

base = int(input('Ingresa base: '))
altura = int(input('Ingresa altura: '))

rect = Rectangulo(base, altura)
print(f"area rectangulo: {rect.calcular()}")


