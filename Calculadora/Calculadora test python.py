def calculadora():
    print("=== Calculadora Simple ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    while True:
        try:
            # Solicitar la operación
            opcion = input("\nSeleccione una operación (1-5): ")

            # Verificar si el usuario quiere salir
            if opcion == '5':
                print("¡Gracias por usar la calculadora!")
                break

            # Verificar que la opción sea válida
            if opcion not in ['1', '2', '3', '4']:
                print("Error: Por favor seleccione una opción válida (1-5)")
                continue

            # Solicitar los números
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            # Realizar la operación seleccionada
            if opcion == '1':
                resultado = num1 + num2
                operacion = '+'
            elif opcion == '2':
                resultado = num1 - num2
                operacion = '-'
            elif opcion == '3':
                resultado = num1 * num2
                operacion = '*'
            elif opcion == '4':
                if num2 == 0:
                    print("Error: No se puede dividir entre cero")
                    continue
                resultado = num1 / num2
                operacion = '/'

            # Mostrar el resultado
            print(f"\n{num1} {operacion} {num2} = {resultado}")

        except ValueError:
            print("Error: Por favor ingrese números válidos")
        except Exception as e:
            print(f"Error: {e}")

# Ejecutar la calculadora
calculadora()
