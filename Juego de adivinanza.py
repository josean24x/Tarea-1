import random
import time

def juego_adivinanza():
    puntuacion_total = 0
    mejor_puntuacion = float('inf')

    def seleccionar_dificultad():
        print("\n=== Niveles de Dificultad ===")
        print("1. Fácil (1-50, 10 intentos)")
        print("2. Medio (1-100, 7 intentos)")
        print("3. Difícil (1-200, 5 intentos)")
        
        while True:
            try:
                nivel = int(input("\nSeleccione nivel (1-3): "))
                if nivel in [1, 2, 3]:
                    return nivel
                print("Por favor, seleccione un nivel válido (1-3)")
            except ValueError:
                print("Por favor, ingrese un número válido")

    def configurar_juego(nivel):
        if nivel == 1:
            return 50, 10, 100  # rango_max, intentos, puntos_base
        elif nivel == 2:
            return 100, 7, 200
        else:
            return 200, 5, 300

    def calcular_puntuacion(intentos_restantes, tiempo_usado, puntos_base):
        puntos_tiempo = max(0, 50 - int(tiempo_usado))  # Bonus por rapidez
        return (intentos_restantes * puntos_base // 10) + puntos_tiempo

    def jugar_ronda():
        nivel = seleccionar_dificultad()
        rango_max, intentos, puntos_base = configurar_juego(nivel)
        numero_secreto = random.randint(1, rango_max)
        intentos_restantes = intentos
        
        print(f"\nTienes {intentos_restantes} intentos para adivinar un número entre 1 y {rango_max}")
        print("¡Comienza el juego!")
        
        tiempo_inicio = time.time()
        
        while intentos_restantes > 0:
            try:
                adivinanza = int(input(f"\nIntentos restantes {intentos_restantes}. Ingresa tu número: "))
                
                if adivinanza < 1 or adivinanza > rango_max:
                    print(f"El número debe estar entre 1 y {rango_max}")
                    continue
                
                if adivinanza == numero_secreto:
                    tiempo_usado = time.time() - tiempo_inicio
                    puntuacion = calcular_puntuacion(intentos_restantes, tiempo_usado, puntos_base)
                    print(f"\n¡Felicitaciones! ¡Has adivinado el número en {intentos - intentos_restantes + 1} intentos!")
                    print(f"Tiempo usado: {tiempo_usado:.1f} segundos")
                    print(f"Puntuación de la ronda: {puntuacion}")
                    return puntuacion
                
                if adivinanza < numero_secreto:
                    print("El número es mayor")
                else:
                    print("El número es menor")
                
                intentos_restantes -= 1
                
            except ValueError:
                print("Por favor, ingresa un número válido")
        
        print(f"\n¡Game Over! El número era {numero_secreto}")
        return 0

    while True:
        print("\n=== Juego de Adivinanza ===")
        print("1. Jugar nueva ronda")
        print("2. Ver puntuación total")
        print("3. Ver mejor puntuación")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == '1':
            puntuacion_ronda = jugar_ronda()
            puntuacion_total += puntuacion_ronda
            if puntuacion_ronda > 0 and puntuacion_ronda < mejor_puntuacion:
                mejor_puntuacion = puntuacion_ronda
                print("¡Nueva mejor puntuación!")
        
        elif opcion == '2':
            print(f"\nPuntuación total: {puntuacion_total}")
        
        elif opcion == '3':
            if mejor_puntuacion == float('inf'):
                print("\nAún no hay mejor puntuación registrada")
            else:
                print(f"\nMejor puntuación: {mejor_puntuacion}")
        
        elif opcion == '4':
            print("\n¡Gracias por jugar!")
            break
        
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 4")

# Ejecutar el juego
if __name__ == "__main__":
    juego_adivinanza()
