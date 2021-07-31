import os
os.system('cls')

class Aritmetica:
    
    def __init__(self, nro1, operador, nro2):
        self.nro1 = nro1
        self.operador = operador
        self.nro2 = nro2

    def calcular(self):
        if self.operador == "+":
            return self.nro1 + self.nro2
        elif self.operador == "-":
            return self.nro1 - self.nro2
        elif self.operador == "*":
            return self.nro1 * self.nro2
        elif self.operador == "/":
            return self.nro1 / self.nro2
        else:
            print("algo salio mal")


nro1 = int(input("ingresa el numero 1: "))
op = input("ingresa un operador: ")
nro2 = int(input("ingresa el numero 2: "))

aritm = Aritmetica(nro1, op, nro2)
print(f'''
----------
{aritm.calcular()} 
----------
''')
