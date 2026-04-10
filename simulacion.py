#Gestor de productos dentro de un almacen
#Voy a crear un a función que me ayude a buscar un producto entre todos los que tenemos y que asi no tengo que copiar y pegar codigo dentro de cada método porque es algo que haré de forma habitual

def buscar_producto(almacen, nombre):
    for estanteria in almacen:
        for producto in almacen[estanteria]:
            if producto["nombre"] == nombre:
                return producto
    return None
#Gestion de Entrada de productos al almacen
def agregar_producto(almacen,nombre,cantidad,precio,estanteria):

    if estanteria not in almacen:
        return "La estanteria no existe"
    if cantidad <= 0:
        return "La cantidad debe ser mayor a 0"
    if precio <= 0:
        return "El precio debe ser mayor a 0"
    
    producto_existente = buscar_producto(almacen, nombre)
    if producto_existente:
        return "El producto ya existe en el almacen"   
    else:
        nuevo_producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        almacen[estanteria].append(nuevo_producto)
        return f"El producto {nombre} ha sido agregado a la estanteria {estanteria}"
#Gestion de salida de productos del almacen
def retirar_producto(almacen, nombre, cantidad):
    if cantidad <= 0:
        return "No existe stock suficiente para ese producto"
    producto = buscar_producto(almacen, nombre)
    if producto:
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    return f"Se han retirado {cantidad} unidades de {nombre}"
                else:
                    return "No existe stock suficiente para ese producto"
#Verificar la disponibilidad de un producto
def verificar_disponibilidad(almacen, nombre):
    producto = buscar_producto(almacen, nombre)
    if producto:
        return f"El producto {nombre} tiene {producto['cantidad']} unidades disponibles"
    else:
        return "El producto no se encuentra en el almacen"
    
#Verificar el estado del almacen
def estado_almacen(almacen):
    valor_total = 0
    print("\n============= Estado del Almacen =============")
    for estanteria, lista_productos in almacen.items():
        print(f"\nEstanteria: {estanteria}")
        cantidad_estanteria = 0
        valor_total = 0
        if len(lista_productos) == 0:
            print("No hay productos en esta estanteria")
        else:
            for producto in lista_productos:
                print(f"  - {producto['nombre']}: {producto['cantidad']} unidades, ${producto['precio']:.2f} cada una")
                valor_total += producto['cantidad'] * producto['precio']
    valor_total_almacen += valor_total
    print(f"VALOR TOTAL DEL ALMACÉN: {valor_total_almacen:.2f} €")

#Transferiri productos entre estanterias
def transferir_producto(almacen, nombre, cantidad, estanteria_origen, estanteria_destino):
    if estanteria_destino not in almacen or estanteria_origen not in almacen:
        return "Alguna de las estanterias no existe"
    if cantidad <= 0:
        return "La cantidad debe ser mayor a 0"
    if estanteria_origen == estanteria_destino:
        return "No se puede transferir a la misma estanteria"
    producto_origen = buscar_producto(almacen, nombre)
    if producto_origen is None:
        return f"El producto {nombre} no se encuentra en la estanteria {estanteria_origen} de origen"
    if producto_origen["cantidad"] < cantidad:
        return (f"No hay suficiente cantidad de {nombre} en la estanteria {estanteria_origen} para transferir"
                f" Existen {producto_origen['cantidad']} unidades disponibles")
    
#Ahora voy a comprobar si el producto ya existe en la estanteria de destino, sumando la cantidad si ya existe o creando un nuevo producto si no existe
    producto_destino = buscar_producto(almacen, nombre)
    if producto_destino:
        producto_destino["cantidad"] += cantidad
    else:
        nuevo_producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": producto_origen["precio"]
        }
        almacen[estanteria_destino].append(nuevo_producto)
    producto_origen["cantidad"] -= cantidad
    if producto_origen["cantidad"] == 0:
        almacen[estanteria_origen].remove(producto_origen)
    return f"Se han transferido {cantidad} unidades de {nombre} desde la estanteria {estanteria_origen} a la estanteria {estanteria_destino}"