import os
os.system('cls')


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def __str__(self):
        return "reemplazado"


    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} - {self.edad}')


class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo






