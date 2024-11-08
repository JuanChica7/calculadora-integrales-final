from sympy import symbols, integrate, simplify, sympify, latex
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

def integracion_por_partes(u, dv):
    x = symbols('x')
    du = u.diff(x)
    v = integrate(dv, x)
    resultado = u * v - integrate(du * v, x)
    resultado = simplify(resultado)
    return resultado

def obtener_funciones():
    u_str = funcion_u.get()
    dv_str = funcion_dv.get()

    u = sympify(u_str)
    dv = sympify(dv_str)

    return u, dv

def calcular_integracion():
    u, dv = obtener_funciones()
    resultado = integracion_por_partes(u, dv)
    resultado_label.config(text="El resultado es: {}".format(resultado)+ " + C")
    paso_a_paso_boton.pack(pady=10)

def ver_paso_a_paso():
    u, dv = obtener_funciones()
    paso_a_paso(u, dv)

def paso_a_paso(u, dv):
    paso_a_paso_ventana = tk.Toplevel(ventana)
    paso_a_paso_ventana.title("Paso a Paso")
    paso_a_paso_ventana.geometry("600x800")
    paso_a_paso_ventana.configure(bg="lightgreen")

    x = symbols('x')
    du = u.diff(x)
    v = integrate(dv, x)
    resultado_intermedio = u * v - integrate(du * v, x)
    resultado_intermedio = simplify(resultado_intermedio)

    paso_label_1 = tk.Label(paso_a_paso_ventana, text="Paso 1: Identificar u y dv", font=("Verdana", 12), bg="lightgreen")
    paso_label_1.pack(pady=10)

    u_label = tk.Label(paso_a_paso_ventana, text="u = {}".format(u), font=("Verdana", 12), bg="lightgreen")
    u_label.pack()

    dv_label = tk.Label(paso_a_paso_ventana, text="dv = {}".format(dv), font=("Verdana", 12), bg="lightgreen")
    dv_label.pack()

    paso_label_2 = tk.Label(paso_a_paso_ventana, text="Paso 2: Calcular du y v", font=("Verdana", 12), bg="lightgreen")
    paso_label_2.pack(pady=10)

    du_label = tk.Label(paso_a_paso_ventana, text="du = {}".format(du), font=("Verdana", 12), bg="lightgreen")
    du_label.pack()

    v_label = tk.Label(paso_a_paso_ventana, text="v = {}".format(v), font=("Verdana", 12), bg="lightgreen")
    v_label.pack()

    paso_label_3 = tk.Label(paso_a_paso_ventana, text="Paso 3: Aplicar la fórmula de integración por partes", font=("Verdana", 12), bg="lightgreen")
    paso_label_3.pack(pady=10)

    formula_label = tk.Label(paso_a_paso_ventana, text="∫u dv = uv - ∫v du", font=("Verdana", 12), bg="lightgreen")
    formula_label.pack()

    paso_label_4 = tk.Label(paso_a_paso_ventana, text="Paso 4: Calcular el primer término", font=("Verdana", 12), bg="lightgreen")
    paso_label_4.pack(pady=10)

    primer_termino = u * v
    primer_termino_label = tk.Label(paso_a_paso_ventana, text="Primer término (uv) = {}".format(primer_termino), font=("Verdana", 12), bg="lightgreen")
    primer_termino_label.pack()

    paso_label_5 = tk.Label(paso_a_paso_ventana, text="Paso 5: Calcular el segundo término", font=("Verdana", 12), bg="lightgreen")
    paso_label_5.pack(pady=10)

    segundo_termino = integrate(v * du, x)
    segundo_termino_label = tk.Label(paso_a_paso_ventana, text="Segundo término (∫v du) = {}".format(segundo_termino), font=("Verdana", 12), bg="lightgreen")
    segundo_termino_label.pack()

    paso_label_6 = tk.Label(paso_a_paso_ventana, text="Paso 6: Obtener el resultado final", font=("Verdana", 12), bg="lightgreen")
    paso_label_6.pack(pady=10)

    resultado_final = primer_termino - segundo_termino
    resultado_final_label = tk.Label(paso_a_paso_ventana, text="Resultado final = Primer término - Segundo término", font=("Verdana", 12), bg="lightgreen")
    resultado_final_label.pack()

    resultado_label = tk.Label(paso_a_paso_ventana, text="El resultado final es: {}".format(resultado_final), font=("Verdana", 12), bg="lightgreen")
    resultado_label.pack(pady=10)

# def dudass():
#     url = "https://marcoenfermeria2.weebly.com/integrales-2.html"
#     webbrowser.open(url)

ventana = tk.Tk()
ventana.title("Cálculo de Integración por Partes")
ventana.geometry("1000x800")
ventana.configure(bg="lightgreen")

menu = """
TEN EN CUENTA LA REGLA ILATE:

"""
menu_label = tk.Label(ventana, text=menu, font=("Verdana", 14), bg="lightgreen")
menu_label.pack(pady=10)

fondo_img = Image.open("ilate.png")
fondo_img = fondo_img.resize((350, 350))
fondo_img = ImageTk.PhotoImage(fondo_img)
fondo_label = tk.Label(ventana, image=fondo_img, bg="lightgreen")
fondo_label.pack(pady=10)

funcion_u_label = tk.Label(ventana, text="Función u(x):", font=("Verdana", 14), bg="lightgreen")
funcion_u_label.pack(pady=5)
funcion_u = tk.Entry(ventana, font=("Verdana", 12), width=40)
funcion_u.pack(pady=5)

funcion_dv_label = tk.Label(ventana, text="Función dv(x):", font=("Verdana", 14), bg="lightgreen")
funcion_dv_label.pack(pady=5)
funcion_dv = tk.Entry(ventana, font=("Verdana", 12), width=40)
funcion_dv.pack(pady=5)

calcular_boton = tk.Button(ventana, text="Calcular Integración", font=("Verdana", 14), command=calcular_integracion, bg='sky blue', fg='black')
calcular_boton.pack(pady=5)

paso_a_paso_boton = tk.Button(ventana, text="Ver Paso a Paso", font=("Verdana", 14), command=ver_paso_a_paso, bg='sky blue', fg='black')

# dudas = tk.Button(ventana, text="SI TIENES DUDAS DA CLICK", font=("Verdana", 14), command=dudass, bg='sky blue', fg='black')
# dudas.pack(pady=5)

resultado_label = tk.Label(ventana, text="", font=("Verdana", 14), bg="lightgreen")
resultado_label.pack(pady=10)

ventana.mainloop()
