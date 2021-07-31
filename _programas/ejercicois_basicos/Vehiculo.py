import os
os.system('cls')

class Vehiculo:
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"color: {self.color} - ruedas {self.ruedas}"



class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f"{super().__str__()} - velocidad {self.velocidad} km/hr"



class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} - tipo {self.tipo}"


vehiculo1 = Vehiculo("rojo", 4)
coche1 = Coche("azul", 6, 60)
bicicleta1 = Bicicleta("verde", 2, "urbana")

print(vehiculo1)
print(coche1)
print(bicicleta1)