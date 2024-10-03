from sympy import symbols, diff

def calcular_derivada(expresion, variable):
    x = symbols(variable)
    derivada = diff(expresion, x)
    return derivada

def main():
    expresion = input("Ingrese la expresión a derivar: ")
    variable = input("Ingrese la variable respecto a la cual desea derivar: ")
    
    derivada = calcular_derivada(expresion, variable)
    
    print("La derivada de la expresión respecto a la variable", variable, "es:", derivada)

if __name__ == "__main__":
    main()



