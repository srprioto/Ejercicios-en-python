import os
os.system("clear")

# from excepcion import NumerosIdenticos




resultado = None
a = 10
b = 0


try:

    resultado = a/b

except Exception as e:
    print(f"ocurrio el error {e}")



print(resultado)
print("siguiente")
