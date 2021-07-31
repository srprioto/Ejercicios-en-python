class Punto:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # redefino operador aritmetico supa para recibir una estructura distinta
    def __add__(self, other):
        return self.x + other.x, self.y + other.y



p1 = Punto(3, 4)
p2 = Punto(5, 6)

# la suma de estos elementos no se puede hacer con suma tradicional
# para eso redefinimos el coportamiento del operador suma
print(p1 + p2)

