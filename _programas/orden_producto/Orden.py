if __name__ == "__main__":
    import os
    os.system("cls")

from Productos import Productos

class Orden:
    
    contador_orden = 0

    def __init__(self, productos):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._productos = list(productos)

    def agregarProducto(self, producto):
        self._productos.append(producto)

    
    def calcularTotal(self):
        total = 0

        for producto in self._productos:
            total += producto.precio
        return total


    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '\n'

        return f'Orden: {self._id_orden} - Productos: \n{productos_str}'

    
if __name__ == '__main__':
    producto1 = Productos("asdfasdf", 50)
    producto2 = Productos("camisa", 100)
    productos1 = [producto1, producto2]

    orden1 = Orden(productos1)

    print(orden1)