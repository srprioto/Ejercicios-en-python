import os
os.system("clear")

from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as Cp

opcion = None

while opcion != 4:
    try:
        
        print("Opciones:")
        print("1.- Agregar pelicula")
        print("2.- Listar peliculas")
        print("3.- Eliminar peliculas")
        print("4.- Salir")
        opcion = int(input("escoge opcion: "))

        if opcion == 1:
            nombre_pelicula = input('Nombre pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            print(pelicula)
            Cp.agregar_peliculas(nombre_pelicula)
            os.system("clear")
            print("se agrego correctamente\n")

        elif opcion == 2:
            os.system("clear")
            Cp.listar_peliculas()

        elif opcion == 3:
            os.system("clear")
            Cp.eliminar_peliculas()

    except Exception as e:
        print(f"Ocurrio un error {e}")
        opcion = None

else:
    print("salir")


