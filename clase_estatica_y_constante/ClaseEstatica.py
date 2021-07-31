import os
os.system('cls')

class Main:
    
    variable_clase = "valor de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodoEstatico():
        print(f"desde metodo estatico - {Main.variable_clase}")

    
    @classmethod
    def metodoClase(cls):
        print(cls.variable_clase)

    
    def metodoInstancia(self):
        self.metodoClase()
        self.metodoEstatico()


Main.metodoClase()

objeto = Main("variable instancia")
objeto.metodoClase()
objeto.metodoInstancia()