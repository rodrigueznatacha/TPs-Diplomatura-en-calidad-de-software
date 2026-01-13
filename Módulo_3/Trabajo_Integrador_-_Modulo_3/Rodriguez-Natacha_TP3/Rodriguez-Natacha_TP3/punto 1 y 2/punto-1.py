def es_primo(numero):
    # 1. Casos especiales
    if numero <= 1:
        return False
    
    if numero == 2:
        return True
    
    if numero % 2 == 0:
        return False
    # 2. Bucle para verificar divisores 
    limite = int(numero**0.5) + 1 # Sumamos 1 para que el rango incluya la raíz.
    
    for divisor in range(3, limite, 2): 

        if numero % divisor == 0:
            return False # Encontró un divisor entonces no es primo
            
    return True
# 1. Solicitar al usuario un número entero positivo 
try:
    numero_ingresado = int(input("Ingrese un número entero positivo: "))
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.") # Manejo de errores 

else:
    resultado = es_primo(numero_ingresado)
    
    print("-" * 30)
    print(f"Número ingresado: {numero_ingresado}")

    if resultado:
        print(f"El número {numero_ingresado} es primo.")
    else:
        print(f"El número {numero_ingresado} no es primo.")