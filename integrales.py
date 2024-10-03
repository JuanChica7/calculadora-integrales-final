import sympy as sp

def calcular_integral(expresion, variable, limite_inferior=None, limite_superior=None):
    # Convertir la expresión a una expresión simbólica
    x = sp.symbols(variable)
    funcion = sp.sympify(expresion)
    
    # Calcular la integral indefinida
    integral_indefinida = sp.integrate(funcion, x)
    
    if limite_inferior is not None and limite_superior is not None:
        # Calcular la integral definida
        integral_definida = sp.integrate(funcion, (x, limite_inferior, limite_superior))
        return integral_definida
    else:
        return integral_indefinida


expresion = input("Ingrese la expresión a integrar: ")
variable = input("Ingrese la variable de integración: ")
limite_inferior = input("Ingrese el límite inferior (deje en blanco si es una integral indefinida): ")
limite_superior = input("Ingrese el límite superior (deje en blanco si es una integral indefinida): ")

if limite_inferior and limite_superior:
    resultado = calcular_integral(expresion, variable, float(limite_inferior), float(limite_superior))
else:
    resultado = calcular_integral(expresion, variable)

print("El resultado de la integral es:", resultado, "+ C")