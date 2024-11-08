import sympy as sp
import tkinter as tk
from tkinter import messagebox


def calcular_derivada():
    variables = ingresarvar.get()
    variables = variables.replace(" ", "")
    variables = sp.symbols(variables)

    funcion_textual = funcion.get()
    try:
        f = sp.sympify(funcion_textual)
    except Exception as e:
        messagebox.showerror("Error", f"Error al convertir la función: {e}")
        return

    resultados = f"Función original: f({', '.join([str(var) for var in variables])}) = {f}\n\n"
    resultados += "Paso 1: Se define la función y se identifican las variables.\n"
    resultados += f"    Función: {f}\n"
    resultados += f"    Variables: {', '.join([str(var) for var in variables])}\n\n"

    for var in variables:
        resultados += f"Paso 2: Se calcula  con respecto a {var}.\n"
        resultados += f"    Regla utilizada: d(f) / d({var})\n"

        derivadaparcial = sp.diff(f, var)
        
        resultados += "Paso 3: Se aplican las reglas de diferenciación.\n"
        resultados += f"    Resultado : {derivadaparcial}\n\n"
        resultados += f"Derivada parcial respecto a {var} (df/d{var}): {derivadaparcial}\n\n"

    textoresultado.config(state=tk.NORMAL)
    textoresultado.delete(1.0, tk.END)
    textoresultado.insert(tk.END, resultados)
    textoresultado.config(state=tk.DISABLED)


ventana = tk.Tk()
ventana.title("Cálculo de Derivadas Parciales")
ventana.geometry("600x400")


tk.Label(ventana, text="Ingresa las variables de la funcion:").pack(pady=5)
ingresarvar = tk.Entry(ventana)
ingresarvar.pack(pady=5)


tk.Label(ventana, text="Ingresa la función a derivar:").pack(pady=5)
funcion = tk.Entry(ventana)
funcion.pack(pady=5)


botoncal = tk.Button(ventana, text="Calcular Derivada Parcial", command=calcular_derivada)
botoncal.pack(pady=10)


textoresultado = tk.Text(ventana, height=10, width=70, state=tk.DISABLED)
textoresultado.pack(pady=10)


fondo = 'lightgreen'  
ventana.configure(bg=fondo)


ventana.mainloop()

#integrantes
#juan avila
#miguel bahamon
#juan manuel chica
#jhon cortes
#alejandro cuellar
#julian narvaez
#diego romero 
#juan santanilla 
#karen velasco
#kevin solarte 