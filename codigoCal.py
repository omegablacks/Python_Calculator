import os

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: No se puede dividir entre cero"
    return x / y

def calculator():
    print("Bienvenido a la calculadora de Jezael Ropero (ID: 1151920)")

    while True:
        print("\nSeleccione la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Limpiar")
        print("6. Salir")

        choice = input("Ingrese la opción (1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if choice == '1':
                print("Resultado:", add(num1, num2))
            elif choice == '2':
                print("Resultado:", subtract(num1, num2))
            elif choice == '3':
                print("Resultado:", multiply(num1, num2))
            elif choice == '4':
                print("Resultado:", divide(num1, num2))
        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Tablero limpiado.")
        elif choice == '6':
            print("¡Gracias por usar la calculadora!")
            break
        else:
            print("Opción inválida")

calculator()

