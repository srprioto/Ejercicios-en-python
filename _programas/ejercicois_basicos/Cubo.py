import os
os.system('cls')

class Cubo:

    def __init__(self, ancho, alto, prof):
        self.a = ancho
        self.h = alto
        self.p = prof


    def calcular(self):
        # ancho * alto * profundidad
        return self.a * self.h * self.p

ancho = int(input("ancho: "))
alto = int(input("alto: "))
prof = int(input("profundidad: "))

cubo = Cubo(ancho, alto, prof)
print(f"volumen: {cubo.calcular()}")