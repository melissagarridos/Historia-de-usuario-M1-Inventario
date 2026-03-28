from funciones import agregar_producto,mostrar_inventario,estadisticas,buscar_producto,guardar_csv,cargar_csv,actualizar_producto,eliminar_producto,volver_menu

def menu():

    inv = True

    while inv:
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
            match accion:
                case 1:
                    agregar_producto()
                case 2:
                    mostrar_inventario()
                case 3:
                    estadisticas()
                case 4:
                    buscar_producto()
                case 5:
                    guardar_csv()
                case 6:
                    cargar_csv()
                case 7:
                    actualizar_producto()
                case 8:
                    eliminar_producto()
                case 9:
                    print("Saliendo")
                    exit(0)
                case _:
                    print("Ingrese una opción válida")

        except ValueError:
            # Si el usuario escribe letras en lugar de un número, avisa y vuelve al menú
            print("Ingrese una opción válida")


 # termina el programa

# Punto de entrada del programa — arranca el menú principal
menu()
