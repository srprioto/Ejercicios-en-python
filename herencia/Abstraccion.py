import os
os.system('cls')

from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass



class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho * self.alto)



r = Rectangulo(3, 5)
print(r.area())
print(r.perimetro())