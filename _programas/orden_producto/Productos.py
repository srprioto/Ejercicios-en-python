if __name__ == "__main__":
    import os
    os.system("cls")

class Productos:

    contador_productos = 0

    def __init__(self, nombre, precio):
        Productos.contador_productos += 1
        self._id_producto = Productos.contador_productos
        self._nombre = nombre
        self._precio = precio

    
    @property
    def precio(self):
        return self._precio


    def __str__(self):
        return f"Id_producto: {self._id_producto} - Nombre: {self._nombre} - Precio: {self._precio}"

    


if __name__ == "__main__":
    producto1 = Productos("camisa", 100)
    producto2 = Productos("camisa", 100)
    print(producto1)
    print(producto2)
