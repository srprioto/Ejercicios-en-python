import os
os.system('cls')

class Persona:

    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas
    
    def __init__(self, nombre, edad):
        
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} - {self.nombre} - {self.edad}]'
    

persona1 = Persona("renato", 20)
persona2 = Persona("luna", 20)
persona3 = Persona("renzo", 20)


print(persona1)
print(persona2)
print(persona3)
print()
Persona.generar_siguiente_valor()
persona4 = Persona("shurita", 20)
print(persona4)
