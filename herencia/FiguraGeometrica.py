from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):

    def __init__(self, alto, ancho):

        if 0 < ancho < 10:
            self._alto = alto
        else:
            self._alto = 0
        
        if 0 < alto < 10:
            self._ancho = ancho
        else:
            self._ancho = 0

    
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho


    @abstractmethod
    def calcularArea(self):
        pass
    

    def __str__(self):
        return f"FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]"