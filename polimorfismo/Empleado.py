if __name__ == "__main__":
    import os
    os.system("cls")

class Empleado:
    
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]"

    def mostrar_detalles(self):
        return self.__str__()


