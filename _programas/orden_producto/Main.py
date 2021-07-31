if __name__ == "__main__":
    import os
    os.system("cls")

from Orden import Orden
from Productos import Productos



producto1 = Productos("abrigo", 50)
producto2 = Productos("camisa", 100)
producto3 = Productos("pantalon", 100)
producto4 = Productos("zapatos", 100)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden2 = Orden(productos2)


orden2.agregarProducto(producto4)
orden2.agregarProducto(producto3)

print(orden1)
print(f'Total: {orden1.calcularTotal()}')
print()
print(orden2)
print(f'Total: {orden2.calcularTotal()}')
print()
