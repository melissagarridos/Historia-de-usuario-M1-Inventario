import csv  

# Diccionario global donde se guarda todo el inventario
# Cada producto es una clave y su valor es otro diccionario con sus datos
inventario = {
    "manzana": {"precio": 2000, "cantidad": 50, "costo_total": 100000},
    "pera": {"precio": 1000, "cantidad": 50, "costo_total": 50000},
    "jugo": {"precio": 2000, "cantidad": 50, "costo_total": 100000},
    "empanada": {"precio": 2500, "cantidad": 10, "costo_total": 250000}
}

def volver_menu():
    # Muestra un menú para decidir si continuar o salir del programa
    # Retorna True si el usuario quiere seguir
    # Termina el programa si elige salir

    volver = input("""¿Desea regresar al menú?
        1. Si
        2. Salir

        Digite la opción: """).strip()

    if volver == "1":
        return True
    elif volver == "2":
        print("Saliendo")
        exit(0)  # detiene completamente el programa
    else:
        print("Opción inválida, intente de nuevo.")

def agregar_producto():
    # Permite agregar un nuevo producto al inventario
    # Verifica que no exista antes de agregarlo

    global inventario

    producto = input("Producto: ").strip().lower()  # limpia y normaliza el nombre

    if producto not in inventario:
        try:
            # pide los datos al usuario
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            # calcula automáticamente el costo total
            costo_total = precio * cantidad

            # guarda el producto dentro del diccionario
            inventario[producto] = {
                "precio": precio,
                "cantidad": cantidad,
                "costo_total": costo_total
            }

        except ValueError:
            # si el usuario escribe letras en vez de números
            print("Ingrese un dato válido")

    else:
        print(f"{producto} ya existe.")

    if volver_menu():
        return

def mostrar_inventario():
    # Recorre todo el inventario y muestra cada producto con sus datos

    global inventario

    if not inventario:
        print("El inventario está vacío")
    else:
        for nombre, datos in inventario.items():
            print(f"{nombre} | Precio: {datos['precio']} | Cantidad: {datos['cantidad']} | Costo total: {datos['costo_total']}")

    volver_menu()

def estadisticas():
    # Calcula información general del inventario:
    # total dinero, total unidades, producto más caro y con más cantidad

    global inventario

    if not inventario:
        print("El inventario está vacío")
    else:
        # suma todos los costos
        total = sum(datos["costo_total"] for datos in inventario.values())

        # suma todas las cantidades
        unidades_totales = sum(datos["cantidad"] for datos in inventario.values())

        # encuentra el producto más caro
        producto_mas_caro = max(inventario, key=lambda p: inventario[p]["precio"])
        precio_max = inventario[producto_mas_caro]["precio"]

        # encuentra el producto con mayor cantidad
        producto_mayor_stock = max(inventario, key=lambda p: inventario[p]["cantidad"])

        print(f"Costo total del inventario: {total}")
        print(f"Cantidad total del inventario: {unidades_totales}")
        print(f"El producto más caro es {producto_mas_caro} con un precio de {precio_max}")
        print(f"El producto con mayor cantidad es {producto_mayor_stock}")

    volver_menu()

def guardar_csv(incluir_header=True):
    # Guarda todo el inventario en un archivo CSV (formato tipo Excel)

    with open("inventario.csv","w",encoding='utf-8') as f:
        writer = csv.writer(f)

        # escribe los nombres de las columnas
        writer.writerow(["producto", "precio", "cantidad", "costo_total"])

        # escribe cada producto como una fila
        for producto, datos in inventario.items():
            writer.writerow([
                producto,
                datos["precio"],
                datos["cantidad"],
                datos["costo_total"]
            ])

    print("Archivo CSV creado")
    volver_menu()

def cargar_csv():
    # Lee el archivo CSV y carga los datos en el inventario
    # Si el producto ya existe, lo actualiza

    global inventario

    try:
        with open("inventario.csv", "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)  # cada fila se convierte en diccionario

            # recorre cada fila del archivo
            for fila in lector:
                try:
                    # limpia y convierte los datos
                    producto = fila["producto"].strip().lower()
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])

                    # verifica si el producto ya existe
                    if producto in inventario:
                        print(f"{producto} ya existe, se actualiza")

                    # guarda o actualiza el producto
                    inventario[producto] = {
                        "precio": precio,
                        "cantidad": cantidad,
                        "costo_total": precio * cantidad
                    }

                except ValueError:
                    # si una fila tiene datos incorrectos
                    print(f"Error en datos de la fila: {fila}")

        print("Listo, se cargó el CSV")

    except FileNotFoundError:
        # si el archivo no existe
        print("El archivo no existe")

    
    volver_menu()

def buscar_producto():
    # Busca un producto en el inventario por su nombre

    global inventario

    producto = input("Producto: ").strip().lower()

    # obtiene el producto sin lanzar error si no existe
    busqueda = inventario.get(producto)

    if busqueda:
        print(f"{producto} | Precio: {busqueda['precio']} | Cantidad: {busqueda['cantidad']} | Costo total: {busqueda['costo_total']}")
    else:
        print(f"'{producto}' no existe en el inventario.")

    volver_menu()
    return inventario

def eliminar_producto():
    # Elimina un producto del inventario si existe

    global inventario

    print(inventario)
    producto = input("\nDigite producto a eliminar: ").strip().lower()

    if producto in inventario:
        del inventario[producto]  # elimina completamente la entrada
        print(f"'{producto}' eliminado.")
        print(inventario)
    else:
        print(f"'{producto}' no encontrado.")

    volver_menu()

def actualizar_producto():
    # Permite modificar precio y cantidad de un producto existente
    # Recalcula automáticamente el costo total

    global inventario

    print(inventario)
    producto = input("\nDigite producto a actualizar: ").strip().lower()

    if inventario.get(producto):
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            # recalcula el costo total
            costo_total = precio * cantidad

            # actualiza solo los valores necesarios
            inventario[producto].update({
                "precio": precio,
                "cantidad": cantidad,
                "costo_total": costo_total
            })

            print(f"{producto} actualizado correctamente")

        except ValueError:
            print("Ingrese un dato válido")
    else:
        print(f"{producto} no existe en el inventario.")

    volver_menu()