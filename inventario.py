import csv

# Diccionario global que almacena todos los productos del inventario
inventario = {
    "manzana": {
        "precio": 2000,
        "cantidad": 50,
        "costo_total": 100000
    }
}


def menu():
    # Muestra las opciones disponibles y lee la elección del usuario
    print("""Seleccione la acción a realizar:
        1. Agregar Producto
        2. Mostrar Inventario
        3. Calcular Estadísticas
        4. Buscar Producto
        5. Guardar CSV
        6. Cargar CSV
        7. Actualizar Producto
        8. Eliminar Producto
        9. Salir""")

    accion = input("Digite una opción: ").strip()

    try:
        # Convierte la opción a entero para poder compararla
        accion = int(accion)

        # Llama la función correspondiente según la opción elegida
        if accion == 1:
            agregar_producto()
        elif accion == 2:
            mostrar_inventario()
        elif accion == 3:
            estadisticas()
        elif accion == 4:
            buscar_producto()
        elif accion == 5:
            guardar_csv()
        elif accion == 6:
            cargar_csv()
        elif accion == 7:
            actualizar_producto()
        elif accion == 8:
            eliminar_producto()
        elif accion == 9:
            print("Saliendo del inventario")

    except ValueError:
        # Si el usuario escribe letras en lugar de un número, avisa y vuelve al menú
        print("Ingrese una opción válida")
        volver_menu()


def agregar_producto():
    # Permite agregar un producto nuevo al inventario
    # Si el producto ya existe, avisa sin agregarlo

    global inventario  # necesario para modificar el diccionario global

    inv = True  # controla el bucle — se pone en False cuando termina

    while inv:
        # Pide el nombre, elimina espacios y lo pone en minúsculas para evitar duplicados
        producto = input("Producto: ").strip().lower()

        if producto not in inventario:
            try:
                precio = float(input("Precio: "))    # acepta decimales
                cantidad = int(input("Cantidad: "))  # solo números enteros

                # Calcula cuánto vale el stock completo de ese producto
                costo_total = precio * cantidad

                # Guarda el nuevo producto en el inventario
                inventario[producto] = {
                    "precio": precio,
                    "cantidad": cantidad,
                    "costo_total": costo_total
                }

                inv = False  # sale del bucle
                volver_menu()

            except ValueError:
                # Si el usuario escribe letras donde va un número, avisa y sale
                print("Ingrese un dato válido")
                inv = False
                volver_menu()
        else:
            # El producto ya existe, no se puede agregar dos veces
            print(f"{producto} ya existe.")
            inv = False
            volver_menu()

    return inventario


def mostrar_inventario():
    # Muestra todos los productos del inventario con su precio, cantidad y costo total

    global inventario

    if not inventario:
        # El diccionario está vacío — no hay nada que mostrar
        print("El inventario está vacío")
    else:
        # Recorre cada producto y muestra sus datos en una línea
        for nombre, datos in inventario.items():
            print(f"{nombre} | Precio: {datos['precio']} | Cantidad: {datos['cantidad']} | Costo total: {datos['costo_total']}")

    volver_menu()


def volver_menu():
    # Pregunta al usuario si quiere volver al menú principal o salir del programa

    volver = input("""¿Desea regresar al menú?
        1. Si
        2. Salir

        Digite la opción: """).strip()

    if volver == "1":
        menu()  # vuelve al menú principal
    else:
        print("Saliendo")  # termina el programa


def estadisticas():
    # Calcula y muestra resumen del inventario:
    # - costo total de todo el stock
    # - unidades totales
    # - producto más caro
    # - producto con mayor cantidad

    global inventario

    if not inventario:
        print("El inventario está vacío")
        volver_menu()
    else:
        # Suma el costo_total de todos los productos
        total = sum(datos["costo_total"] for datos in inventario.values())

        # Suma la cantidad de todos los productos
        unidades_totales = sum(datos["cantidad"] for datos in inventario.values())

        # max() recorre las keys del inventario (nombres de productos)
        # key=lambda p: ... le dice a max() por qué valor comparar
        producto_mas_caro = max(inventario, key=lambda p: inventario[p]["precio"])
        precio_max = inventario[producto_mas_caro]["precio"]

        producto_mayor_stock = max(inventario, key=lambda p: inventario[p]["cantidad"])

        print(f"Costo total del inventario: {total}")
        print(f"Cantidad total del inventario: {unidades_totales}")
        print(f"El producto más caro es {producto_mas_caro} con un precio de {precio_max}")
        print(f"El producto con mayor cantidad es {producto_mayor_stock}")

        volver_menu()


def guardar_csv(incluir_header=True):
    # Guarda el inventario actual en un archivo CSV
    # incluir_header=True significa que por defecto escribe la fila de encabezado

    global inventario

    if not inventario:
        # No tiene sentido guardar un archivo vacío
        print("El inventario está vacío, no hay nada que guardar.")
        volver_menu()
        return  # sale de la función sin hacer nada más

    # Pide el nombre del archivo y le agrega la extensión .csv automáticamente
    ruta = input("Nombre del archivo (sin extensión): ").strip() + ".csv"

    try:
        # Abre (o crea) el archivo en modo escritura
        # newline="" evita líneas en blanco extra en Windows
        # encoding="utf-8" permite tildes y ñ
        with open(ruta, "w", newline="", encoding="utf-8") as f:

            # DictWriter escribe filas como diccionarios
            # fieldnames define el orden y nombres de las columnas
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])

            if incluir_header:
                # Escribe la primera fila: nombre,precio,cantidad
                writer.writeheader()

            # Recorre el inventario y escribe una fila por cada producto
            for nombre, datos in inventario.items():
                writer.writerow({
                    "nombre": nombre,
                    "precio": datos["precio"],
                    "cantidad": datos["cantidad"]
                })

        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        # El archivo está abierto en otro programa (ej: Excel) o la carpeta es de solo lectura
        print(f"Error: no tienes permisos para escribir en '{ruta}'.")
    except OSError as e:
        # Cualquier otro error del sistema: ruta inválida, disco lleno, etc.
        print(f"Error al guardar el archivo: {e}")

    volver_menu()


def cargar_csv():
    # Carga productos desde un archivo CSV al inventario
    # Valida el encabezado, cada fila, y pregunta si sobrescribir o fusionar

    global inventario

    # Pide el nombre del archivo y le agrega .csv automáticamente
    ruta = input("Nombre del archivo (sin extensión): ").strip() + ".csv"

    # pendiente

    volver_menu()


def buscar_producto():
    # Busca un producto por nombre y muestra sus datos si existe

    global inventario

    producto = input("Producto: ").strip().lower()

    # .get() devuelve None si el producto no existe, sin lanzar error
    busqueda = inventario.get(producto)

    if busqueda:
        # El producto existe → muestra sus datos
        print(f"{producto} | Precio: {busqueda['precio']} | Cantidad: {busqueda['cantidad']} | Costo total: {busqueda['costo_total']}")
    else:
        # El producto no existe en el inventario
        print(f"'{producto}' no existe en el inventario.")

    volver_menu()
    return inventario


def eliminar_producto():
    # Elimina un producto del inventario por nombre

    global inventario

    print(inventario)  # muestra el inventario actual antes de eliminar
    producto = input("\nDigite producto a eliminar: ").strip().lower()

    if producto in inventario:
        del inventario[producto]  # elimina la key y todos sus datos
        print(f"'{producto}' eliminado.")
        print(inventario)  # muestra el inventario actualizado
    else:
        print(f"'{producto}' no encontrado.")

    volver_menu()


def actualizar_producto():
    # Actualiza el precio y cantidad de un producto existente
    # También recalcula el costo_total automáticamente

    global inventario

    print(inventario)  # muestra el inventario actual antes de actualizar
    producto = input("\nDigite producto a actualizar: ").strip().lower()

    # .get() devuelve None si no existe, evitando KeyError
    if inventario.get(producto):
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            costo_total = precio * cantidad

            # .update() reemplaza solo las keys indicadas, deja el resto igual
            inventario[producto].update({
                "precio": precio,
                "cantidad": cantidad,
                "costo_total": costo_total
            })

            print(f"{producto} | Precio: {inventario[producto]['precio']} | Cantidad: {inventario[producto]['cantidad']} | Costo total: {inventario[producto]['costo_total']}")
            volver_menu()

        except ValueError:
            # El usuario escribió letras donde iba un número
            print("Ingrese un dato válido")
            volver_menu()
    else:
        print(f"{producto} no existe en el inventario.")
        volver_menu()


# Punto de entrada del programa — arranca el menú principal
menu()
