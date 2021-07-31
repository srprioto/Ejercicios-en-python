if __name__ == "__main__":
    import os
    os.system("cls")

from Empleado import Empleado
from Gerente import Gerente

def imprimirDetalles(objeto):
    print(objeto)
    print(objeto.mostrar_detalles())
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(f"Departamento: {objeto.departamento}")
    print()
    
empleado = Empleado('Renato', 5000)
imprimirDetalles(empleado)

gerente = Gerente("Renzo", 6000, "sistemas")
imprimirDetalles(gerente)

