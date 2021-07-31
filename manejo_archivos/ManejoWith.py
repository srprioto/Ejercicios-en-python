class ManejoWith:

    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print("obtener recurso".center(50, "-"))
        self.archivo = open(self.nombre, 'r')
        return self.archivo

    def __exit__(self, tipo_excep, valor_excep, traza_error):
        print("Cerrar recurso".center(50, "-"))
        if self.archivo:
            self.archivo.close()