# Registrar productos con su nombre, precio y cantidad en un programa simple.
# Calcular operaciones básicas como total de unidades y costo aproximado.
# Aplicar fundamentos de programación: entrada de datos, variables, operaciones matemáticas y salidas en consola.
# Diccionario vacío donde se guardarán los productos
inventario = {}

# Variable que controla el bucle
inv = True

while inv:

    # Pide el nombre del producto, elimina espacios y capitaliza la primera letra
    nombre = input("Nombre del producto: ").strip().capitalize()

    try:

        # Pide el precio y lo convierte a decimal
        precio = float(input("Precio: "))

        # Pide la cantidad y la convierte a entero
        cantidad = int(input("Cantidad: "))

        # Calcula el costo total multiplicando precio por cantidad
        costo_total = precio * cantidad

        # Guarda el producto en el diccionario con su precio y cantidad
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}

        # Muestra el resumen del producto ingresado
        print(f"{nombre} Precio: {precio} Cantidad: {cantidad} Costo total: {costo_total}")

        # Cambia inv a False para salir del bucle
        inv = False

    except ValueError:

        # Si el usuario ingresa letras en precio o cantidad, muestra este mensaje
        # y el bucle se repite para pedir los datos de nuevo
        print("Ingrese un dato válido")
