import math # Necesario para la raíz cuadrada

def resolver_cuadratica(a, b, c):
    """
    Calcula las raíces de una ecuación cuadrática (ax^2 + bx + c = 0).
    Retorna un mensaje con el resultado.
    """
    
    if a == 0:
        return "Error: El coeficiente 'a' no puede ser cero (no es una ecuación cuadrática)."

    # Cálculo del Discriminante (Delta): b^2 - 4ac
    discriminante = (b**2) - (4 * a * c)

    # Caso 1: Dos raíces reales y distintas (Discriminante > 0)
    if discriminante > 0:
        
        raiz_discriminante = math.sqrt(discriminante)
        
        x1 = (-b + raiz_discriminante) / (2 * a)
        x2 = (-b - raiz_discriminante) / (2 * a)
        
        # El :.2f formatea el número a dos decimales
        return f"Dos raíces reales: x1 = {x1:.2f} y x2 = {x2:.2f}"
    
    # Caso 2: Una única raíz real (Discriminante = 0)
    elif discriminante == 0:
        
        x = -b / (2 * a)
        
        return f"Una única raíz real: x = {x:.2f}"
        
    # Caso 3: Discriminante negativo (No hay raíces reales)
    else:
        return "El discriminante es negativo. No existen raíces reales."

# ---
# Ingreso de datos por parte del usuario
# ---

print("-" * 40)
print("Resolución de Ecuación Cuadrática (ax² + bx + c = 0)")
print("-" * 40)

try:
    # 1. Pedir el valor de 'a' y convertirlo a float
    a = float(input("Ingrese el coeficiente 'a': "))
    
    # 2. Pedir el valor de 'b' y convertirlo a float
    b = float(input("Ingrese el coeficiente 'b': "))
    
    # 3. Pedir el valor de 'c' y convertirlo a float
    c = float(input("Ingrese el coeficiente 'c': "))
    
    print("-" * 40)
    # Llamar a la función con los valores ingresados y mostrar el resultado
    resultado_final = resolver_cuadratica(a, b, c)
    print(resultado_final)
    
except ValueError:
    # Captura el error si el usuario ingresa algo que no es un número (ej: una letra)
    print("-" * 40)
    print("Error: Ingrese solo valores numéricos válidos (enteros o decimales).")