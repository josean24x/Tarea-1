def gestor_tareas():
    tareas = []
    
    def mostrar_menu():
        print("\n=== Gestor de Tareas ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

    def ver_tareas():
        if not tareas:
            print("\nNo hay tareas pendientes.")
        else:
            print("\nTareas pendientes:")
            for i, tarea in enumerate(tareas, 1):
                estado = "✓" if tarea['completada'] else " "
                print(f"{i}. [{estado}] {tarea['descripcion']}")

    def agregar_tarea():
        descripcion = input("\nIngrese la descripción de la tarea: ")
        if descripcion.strip():  # Verifica que no esté vacía
            tareas.append({
                'descripcion': descripcion,
                'completada': False
            })
            print("Tarea agregada exitosamente.")
        else:
            print("Error: La descripción no puede estar vacía.")

    def marcar_completada():
        ver_tareas()
        if tareas:
            try:
                indice = int(input("\nIngrese el número de la tarea a marcar como completada: ")) - 1
                if 0 <= indice < len(tareas):
                    tareas[indice]['completada'] = True
                    print("Tarea marcada como completada.")
                else:
                    print("Error: Número de tarea inválido.")
            except ValueError:
                print("Error: Por favor ingrese un número válido.")

    def eliminar_tarea():
        ver_tareas()
        if tareas:
            try:
                indice = int(input("\nIngrese el número de la tarea a eliminar: ")) - 1
                if 0 <= indice < len(tareas):
                    tarea_eliminada = tareas.pop(indice)
                    print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
                else:
                    print("Error: Número de tarea inválido.")
            except ValueError:
                print("Error: Por favor ingrese un número válido.")

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == '1':
            ver_tareas()
        elif opcion == '2':
            agregar_tarea()
        elif opcion == '3':
            marcar_completada()
        elif opcion == '4':
            eliminar_tarea()
        elif opcion == '5':
            print("\n¡Gracias por usar el Gestor de Tareas!")
            break
        else:
            print("\nError: Por favor seleccione una opción válida (1-5)")

# Ejecutar el gestor de tareas
if __name__ == "__main__":
    gestor_tareas()
