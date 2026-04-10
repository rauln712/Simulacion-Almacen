from simulacion import *
import json
import os

ruta_actual = os.path.dirname(__file__)
ruta_json = os.path.join(ruta_actual, "productos_almacen_volumen.json")

with open(ruta_json, "r", encoding="utf-8") as archivo:
    almacen = json.load(archivo)

def menu():
    while True:
        print("\n========== MENU DEL ALMACEN ==========")
        print("1. Agregar producto")
        print("2. Retirar producto")
        print("3. Verificar disponibilidad de un producto")
        print("4. Ver estado del almacen")
        print("5. Transferir producto entre estanterias")
        print("6. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad: "))
            precio = float(input("Introduce el precio: "))
            estanteria = input("Introduce la estanteria: ")

            resultado = agregar_producto(almacen, nombre, cantidad, precio, estanteria)
            print(resultado)

        elif opcion == "2":
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad a retirar: "))

            resultado = retirar_producto(almacen, nombre, cantidad)
            print(resultado)

        elif opcion == "3":
            nombre = input("Introduce el nombre del producto: ")

            resultado = verificar_disponibilidad(almacen, nombre)
            print(resultado)

        elif opcion == "4":
            estado_almacen(almacen)

        elif opcion == "5":
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad a transferir: "))
            estanteria_origen = input("Introduce la estanteria de origen: ")
            estanteria_destino = input("Introduce la estanteria de destino: ")

            resultado = transferir_producto(
                almacen,
                nombre,
                cantidad,
                estanteria_origen,
                estanteria_destino
            )
            print(resultado)

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida. Intenta otra vez.")

if __name__ == "__main__":
    menu()