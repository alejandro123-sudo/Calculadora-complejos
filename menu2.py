import tkinter as tk
from tkinter import messagebox
import math

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Números Complejos")
ventana.geometry("450x650") 
ventana.config(bg="#eb9191")

# Encabezado
encabezado = tk.Label(
    ventana,
    text="FACULTAD DE INGENIERÍA - UNAM",
    bg="#b30000",
    fg="black",
    font=("Arial", 14, "bold"),
    pady=8
)
encabezado.pack(fill="x")

titulo = tk.Label(
    ventana,
    text="Calculadora de Números Complejos",
    bg="#eb9191",
    fg="#0b3d91",
    font=("Arial", 13, "bold")
)
titulo.pack(pady=10)

modo = None  # guarda la forma actual: binómica, polar o exponencial

# Variables globales para almacenar los números en AMBAS formas
z1_binomica = (0, 0)  # (a, b)
z1_polar = (0, 0)     # (r, theta)
z2_binomica = (0, 0)  # (a, b)
z2_polar = (0, 0)     # (r, theta)


# Forma binómica 

def activar_binomica():
    global modo
    modo = "binomica"
    messagebox.showinfo("Modo Binómico", "Modo binómico activado (a + bi)")

marco_binomica = tk.LabelFrame(ventana, text="Forma Binómica (a + bi)", bg="#eb9191", font=("Arial", 10, "bold"))
marco_binomica.pack(pady=10)

tk.Label(marco_binomica, text="Primer número:", bg="#eb9191").grid(row=0, column=0, padx=5)
real1 = tk.Entry(marco_binomica, width=7)
real1.grid(row=0, column=1)
tk.Label(marco_binomica, text="+", bg="#eb9191").grid(row=0, column=2)
imag1 = tk.Entry(marco_binomica, width=7)
imag1.grid(row=0, column=3)
tk.Label(marco_binomica, text="i", bg="#eb9191").grid(row=0, column=4)

tk.Label(marco_binomica, text="Segundo número:", bg="#eb9191").grid(row=1, column=0, padx=5)
real2 = tk.Entry(marco_binomica, width=7)
real2.grid(row=1, column=1)
tk.Label(marco_binomica, text="+", bg="#eb9191").grid(row=1, column=2)
imag2 = tk.Entry(marco_binomica, width=7)
imag2.grid(row=1, column=3)
tk.Label(marco_binomica, text="i", bg="#eb9191").grid(row=1, column=4)

tk.Button(ventana, text="Usar forma binómica (a + bi)", bg="#b3d1ff", command=activar_binomica).pack(pady=5)

# Forma polar


def abrir_polar():
    ventana_polar = tk.Toplevel(ventana)
    ventana_polar.title("Forma Polar (r cis θ)")
    ventana_polar.geometry("360x260")
    ventana_polar.config(bg="#e8eaf6")

    tk.Label(ventana_polar, text="Primer número (z₁ = r₁ cis θ₁)", bg="#e8eaf6", font=("Arial", 10, "bold")).pack(pady=5)
    marco1 = tk.Frame(ventana_polar, bg="#e8eaf6")
    marco1.pack(pady=3)
    tk.Label(marco1, text="r₁:", bg="#e8eaf6").grid(row=0, column=0, padx=5)
    modulo1 = tk.Entry(marco1, width=8)
    modulo1.grid(row=0, column=1)
    tk.Label(marco1, text="θ₁ (°):", bg="#e8eaf6").grid(row=0, column=2, padx=5)
    angulo1 = tk.Entry(marco1, width=8)
    angulo1.grid(row=0, column=3)

    tk.Label(ventana_polar, text="Segundo número (z₂ = r₂ cis θ₂)", bg="#e8eaf6", font=("Arial", 10, "bold")).pack(pady=5)
    marco2 = tk.Frame(ventana_polar, bg="#e8eaf6")
    marco2.pack(pady=3)
    tk.Label(marco2, text="r₂:", bg="#e8eaf6").grid(row=0, column=0, padx=5)
    modulo2 = tk.Entry(marco2, width=8)
    modulo2.grid(row=0, column=1)
    tk.Label(marco2, text="θ₂ (°):", bg="#e8eaf6").grid(row=0, column=2, padx=5)
    angulo2 = tk.Entry(marco2, width=8)
    angulo2.grid(row=0, column=3)

    def confirmar_polar():
        global modo, z1_binomica, z1_polar, z2_binomica, z2_polar
        modo = "polar"
        try:
            r1 = float(modulo1.get())
            t1 = float(angulo1.get())
            r2 = float(modulo2.get())
            t2 = float(angulo2.get())

            z1_polar = (r1, t1)
            z2_polar = (r2, t2)
            z1_binomica = convertir_a_binomica(r1, t1)
            z2_binomica = convertir_a_binomica(r2, t2)
            
            messagebox.showinfo("Datos Guardados", f"z₁ = {r1} cis {t1}°\nz₂ = {r2} cis {t2}°")
            ventana_polar.destroy()
        except ValueError:
            messagebox.showwarning("Error", "Ingresa solo números válidos.")

    tk.Button(ventana_polar, text="Confirmar", width=15, bg="#c5cae9", command=confirmar_polar).pack(pady=12)

tk.Button(ventana, text="Ingresar en forma polar (r cis θ)", width=25, bg="#b3d1ff", command=abrir_polar).pack(pady=5)

# Forma exponencial


def abrir_exponencial():
    ventana_exp = tk.Toplevel(ventana)
    ventana_exp.title("Exponencial (r·e^(iθ))")
    ventana_exp.geometry("360x260")
    ventana_exp.config(bg="#e7eeee")

    tk.Label(ventana_exp, text="Primer número (z₁ = r₁·e^(iθ₁))", bg="#f1e3ff", font=("Arial", 10, "bold")).pack(pady=5)
    marco1 = tk.Frame(ventana_exp, bg="#f1e3ff")
    marco1.pack(pady=3)
    tk.Label(marco1, text="r₁:", bg="#f1e3ff").grid(row=0, column=0, padx=5)
    modulo_exp1 = tk.Entry(marco1, width=8)
    modulo_exp1.grid(row=0, column=1)
    tk.Label(marco1, text="θ₁ (°):", bg="#f1e3ff").grid(row=0, column=2, padx=5)
    angulo_exp1 = tk.Entry(marco1, width=8)
    angulo_exp1.grid(row=0, column=3)

    tk.Label(ventana_exp, text="Segundo número (z₂ = r₂·e^(iθ₂))", bg="#f1e3ff", font=("Arial", 10, "bold")).pack(pady=5)
    marco2 = tk.Frame(ventana_exp, bg="#f1e3ff")
    marco2.pack(pady=3)
    tk.Label(marco2, text="r₂:", bg="#f1e3ff").grid(row=0, column=0, padx=5)
    modulo_exp2 = tk.Entry(marco2, width=8)
    modulo_exp2.grid(row=0, column=1)
    tk.Label(marco2, text="θ₂ (°):", bg="#f1e3ff").grid(row=0, column=2, padx=5)
    angulo_exp2 = tk.Entry(marco2, width=8)
    angulo_exp2.grid(row=0, column=3)

    def confirmar_exponencial():
        global modo, z1_binomica, z1_polar, z2_binomica, z2_polar
        modo = "exponencial"
        try:
            r1 = float(modulo_exp1.get())
            t1 = float(angulo_exp1.get())
            r2 = float(modulo_exp2.get())
            t2 = float(angulo_exp2.get())

            z1_polar = (r1, t1)
            z2_polar = (r2, t2)
            z1_binomica = convertir_a_binomica(r1, t1)
            z2_binomica = convertir_a_binomica(r2, t2)
            
            messagebox.showinfo("Datos Guardados", f"z₁ = {r1}·e^(i{t1}°)\nz₂ = {r2}·e^(i{t2}°)")
            ventana_exp.destroy()
        except ValueError:
            messagebox.showwarning("Error", "Ingresa solo números válidos.")

    tk.Button(ventana_exp, text="Confirmar", width=15, bg="#d6bfff", command=confirmar_exponencial).pack(pady=12)

tk.Button(ventana, text="Ingresar en forma exponencial (r·e^(iθ))", width=30, bg="#d6bfff", command=abrir_exponencial).pack(pady=5)

# Aquí van las funciones de las operaciones: 

# --- FUNCIÓN DE GRÁFICA (Versión "Híbrida" con Zoom Automático) ---
def graficar_con_tkinter(z1_bin, z1_label, z2_bin, z2_label, res_bin, res_label):
    
    # 1. Crear la nueva ventana y el canvas
    ventana_grafica = tk.Toplevel(ventana)
    ventana_grafica.title("Plano Complejo (Argand)")
    
    ANCHO = 500
    ALTO = 500
    CENTRO_X = ANCHO / 2
    CENTRO_Y = ALTO / 2
    PADDING = 40 # Margen

    canvas = tk.Canvas(ventana_grafica, width=ANCHO, height=ALTO, bg="white")
    canvas.pack()

    # 2. Encontrar el valor máximo para ajustar la escala (LA PARTE "INTELIGENTE")
    max_val = 0
    
    # Crear una lista temporal de todos los números a graficar
    numeros_para_escalar = []
    if z1_bin: numeros_para_escalar.append(z1_bin)
    if z2_bin: numeros_para_escalar.append(z2_bin)
    if res_bin:
        if isinstance(res_bin, list):
            numeros_para_escalar.extend(res_bin) # Añadir todas las raíces
        else:
            numeros_para_escalar.append(res_bin) # Añadir resultado único
    
    # Encontrar el valor (real o imag) más grande
    for real, imag in numeros_para_escalar:
        if real is not None and imag is not None:
            max_val = max(max_val, abs(real), abs(imag))
    
    if max_val == 0:
        max_val = 5 # Un zoom por defecto si todos los números son 0

    # 3. Calcular la escala (cuántos píxeles por unidad)
    escala = (ANCHO / 2 - PADDING) / max_val

    # 4. Función auxiliar para convertir (Real, Img) a (pixel X, pixel Y)
    def a_pixel(r, i):
        px = CENTRO_X + (r * escala)
        py = CENTRO_Y - (i * escala) # El eje Y está invertido en Tkinter
        return (px, py)

    # 5. Dibujar Ejes (X e Y)
    canvas.create_line(0, CENTRO_Y, ANCHO, CENTRO_Y, fill="black") # Eje Real (X)
    canvas.create_line(CENTRO_X, 0, CENTRO_X, ALTO, fill="black") # Eje Imag (Y)
    
    canvas.create_text(ANCHO - 20, CENTRO_Y + 15, text="Real", fill="black")
    canvas.create_text(CENTRO_X + 25, 10, text="Img", fill="black")

    # 6. Dibujar marcas de escala
    txt_max = f"{max_val:.1g}"
    txt_min = f"{-max_val:.1g}"
    canvas.create_text(a_pixel(max_val, 0)[0], CENTRO_Y + 10, text=txt_max, fill="gray")
    canvas.create_text(a_pixel(-max_val, 0)[0], CENTRO_Y + 10, text=txt_min, fill="gray")
    canvas.create_text(CENTRO_X - 15, a_pixel(0, max_val)[1], text=f"{txt_max}i", fill="gray")
    canvas.create_text(CENTRO_X - 15, a_pixel(0, -max_val)[1], text=f"{txt_min}i", fill="gray")


    # 7. Dibujar los vectores (z1, z2, resultado)
    
    # z1
    a1, b1 = z1_bin
    px1, py1 = a_pixel(a1, b1)
    canvas.create_line(CENTRO_X, CENTRO_Y, px1, py1, fill="blue", width=2, arrow=tk.LAST)
    canvas.create_text(px1 + 5, py1, text=z1_label, fill="blue", anchor="w")

    # z2 (si existe)
    if z2_bin is not None:
        a2, b2 = z2_bin
        px2, py2 = a_pixel(a2, b2)
        canvas.create_line(CENTRO_X, CENTRO_Y, px2, py2, fill="green", width=2, arrow=tk.LAST)
        canvas.create_text(px2 + 5, py2, text=z2_label, fill="green", anchor="w")

    # Resultado (si existe)
    if res_bin is not None:
        if isinstance(res_bin, list): # Si es una lista (para raíces)
            for i, (a_res, b_res) in enumerate(res_bin):
                px_res, py_res = a_pixel(a_res, b_res)
                canvas.create_line(CENTRO_X, CENTRO_Y, px_res, py_res, fill="red", width=2, arrow=tk.LAST, dash=(4, 2))
                canvas.create_text(px_res + 5, py_res, text=f"{res_label} (k={i})", fill="red", anchor="w")
        
        else: # Si es un solo resultado
            a_res, b_res = res_bin
            px_res, py_res = a_pixel(a_res, b_res)
            canvas.create_line(CENTRO_X, CENTRO_Y, px_res, py_res, fill="red", width=2, arrow=tk.LAST)
            canvas.create_text(px_res + 5, py_res, text=res_label, fill="red", anchor="w")

    # 8. Traer la ventana al frente
    ventana_grafica.lift()
    ventana_grafica.attributes("-topmost", True)
    ventana_grafica.attributes("-topmost", False)


# --- Funciones de Conversión Manual ---
def convertir_a_polar(a, b):
    r = math.sqrt(a**2 + b**2)
    theta_rad = math.atan2(b, a)
    theta_grados = math.degrees(theta_rad)
    return (r, theta_grados)

def convertir_a_binomica(r, theta_grados):
    theta_rad = math.radians(theta_grados)
    a = r * math.cos(theta_rad)
    b = r * math.sin(theta_rad)
    if abs(a) < 1e-10: a = 0.0 # Corrección para evitar -0.0
    if abs(b) < 1e-10: b = 0.0 # Corrección para evitar -0.0
    return (a, b)

# --- Funciones de Operaciones (con nombres de equipo ¡chido!) ---
def suma_ale(z1_bin, z2_bin):
    a1, b1 = z1_bin
    a2, b2 = z2_bin
    return (a1 + a2, b1 + b2)

def restar(z1_bin, z2_bin):
    a1, b1 = z1_bin
    a2, b2 = z2_bin
    return (a1 - a2, b1 - b2)

def multiplicacion_alan(z1_bin, z2_bin):
    a, b = z1_bin
    c, d = z2_bin
    multireal = (a * c) - (b * d)
    multimag = (a * d) + (b * c)
    return (multireal, multimag)

def division_erick(z1_bin, z2_bin):
    a, b = z1_bin
    c, d = z2_bin
    denominador = (c**2) + (d**2)
    if denominador == 0:
        return None 
    
    divreal = ((a * c) + (b * d)) / denominador
    divimag = ((b * c) - (a * d)) / denominador
    return (divreal, divimag)

def potencia_german(z1_pol, n):
    r, t = z1_pol
    r_res = r ** n
    t_res = t * n
    return (r_res, t_res)

def raiz(z1_pol, n):
    r, t = z1_pol
    resultados_polares = [] 
    r_res = r ** (1/n)
    
    for k in range(n):
        t_k = (t + 360 * k) / n
        resultados_polares.append( (r_res, t_k) )
        
    return resultados_polares # Devuelve una LISTA de tuplas polares


#  Menú de operaciones (EL CEREBRO actualizado a los nombres de equipo)
def operar(operacion):
    global modo, z1_binomica, z1_polar, z2_binomica, z2_polar

    if modo is None:
        messagebox.showwarning("Sin modo", "Primero elige una forma: binómica, polar o exponencial.")
        return

    try:
        # --- PASO 1: Cargar datos de z1 y z2 ---
        if modo == "binomica":
            if real1.get() == "" or imag1.get() == "" or real2.get() == "" or imag2.get() == "":
                 messagebox.showwarning("Campos Vacíos", "Por favor, llena todos los campos de la forma binómica.")
                 return
            
            a1 = float(real1.get())
            b1 = float(imag1.get())
            a2 = float(real2.get())
            b2 = float(imag2.get())
            
            z1_binomica = (a1, b1)
            z2_binomica = (a2, b2)
            z1_polar = convertir_a_polar(a1, b1)
            z2_polar = convertir_a_polar(a2, b2)
        
        # (Si el modo es polar/exp, los datos ya están listos)
        
        # Definir etiquetas para la gráfica
        a1, b1 = z1_binomica
        a2, b2 = z2_binomica
        z1_label = f"z₁: {a1:.3g} {'+' if b1 >= 0 else '-'} {abs(b1):.3g}i"
        z2_label = f"z₂: {a2:.3g} {'+' if b2 >= 0 else '-'} {abs(b2):.3g}i"
        
        resultado_texto = "" # El texto para la etiqueta
        
        # --- PASO 2: Realizar Operación ---
        
        if operacion == "Potencia" or operacion == "Raiz enésima":
            n_texto = real2.get()
            if n_texto == "":
                messagebox.showerror("Error", "Para Potencia/Raíz, 'n' debe estar en el campo 'real' del segundo número.")
                return
            n = int(n_texto)
            
            if operacion == "Potencia":
                res_pol = potencia_german(z1_polar, n) 
                res_bin = convertir_a_binomica(res_pol[0], res_pol[1])
                
                a_res, b_res = res_bin
                r_res, t_res = res_pol
                
                resultado_texto = f"Forma Binómica: {a_res:.4g} {'+' if b_res >= 0 else '-'} {abs(b_res):.4g}i\n"
                resultado_texto += f"Forma Polar: {r_res:.4g} cis {t_res:.4g}°"
                
                res_label = f"z₁^{n}"
                # Graficar solo z1 y el resultado. z2 (None) no se usó.
                graficar_con_tkinter(z1_binomica, z1_label, None, None, res_bin, res_label)

            else: # Raiz enésima
                if n <= 0:
                    messagebox.showerror("Error", "El índice 'n' debe ser un entero positivo.")
                    return
                
                lista_res_pol = raiz(z1_polar, n) 
                
                resultado_texto = f"Raíces ({n}) de z₁:\n"
                
                # Convertir todas las raíces a binómica para graficarlas
                lista_res_bin = []
                k = 0 # Iniciar el contador k
                for (r_k, t_k) in lista_res_pol:
                    a_k, b_k = convertir_a_binomica(r_k, t_k)
                    lista_res_bin.append((a_k, b_k))
                    # Poner texto en la etiqueta
                    resultado_texto += f"k={k}: {a_k:.3g} {'+' if b_k >= 0 else '-'} {abs(b_k):.3g}i  (Polar: {r_k:.3g} cis {t_k:.3g}°)\n"
                    k += 1 # Incrementar k
                
                res_label = "Raíz"
                # Graficar z1 y la LISTA de raíces. z2 (None) no se usó.
                graficar_con_tkinter(z1_binomica, z1_label, None, None, lista_res_bin, res_label)

        else:
            # Operaciones con z1 y z2
            res_bin = (0,0)
            op_label = ""
            
            if operacion == "Suma":
                res_bin = suma_ale(z1_binomica, z2_binomica) 
                op_label = "Suma"
            elif operacion == "Resta":
                res_bin = restar(z1_binomica, z2_binomica) 
                op_label = "Resta"
            elif operacion == "Multiplicación":
                res_bin = multiplicacion_alan(z1_binomica, z2_binomica)
                op_label = "Mult"
            elif operacion == "División":
                res_bin = division_erick(z1_binomica, z2_binomica)
                if res_bin is None:
                    messagebox.showerror("Error", "División por cero (r₂ no puede ser 0).")
                    return
                op_label = "Div"
            
            # Convertir el resultado a AMBAS formas
            a_res, b_res = res_bin
            res_pol = convertir_a_polar(a_res, b_res)
            r_res, t_res = res_pol
            
            # Poner texto en la etiqueta
            resultado_texto = f"Forma Binómica: {a_res:.4g} {'+' if b_res >= 0 else '-'} {abs(b_res):.4g}i\n"
            resultado_texto += f"Forma Polar: {r_res:.4g} cis {t_res:.4g}°"
            
            # Graficar z1, z2 y el resultado
            graficar_con_tkinter(z1_binomica, z1_label, z2_binomica, z2_label, res_bin, op_label)

        # --- PASO 3: Mostrar Texto ---
        resultado_label.config(text=resultado_texto, height=max(4, resultado_texto.count('\n') + 1))
        
    except ValueError:
        messagebox.showerror("Error de entrada", "Revisa que todos los campos sean números válidos.\nSi usas Potencia/Raíz, 'n' debe ser un entero en el campo 'real' del segundo número.")
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Ocurrió un error: {e}")


tk.Label(ventana, text="Selecciona la operación:", bg="#eb9191", font=("Arial", 11, "bold")).pack(pady=8)
lista_operaciones = ["Suma", "Resta", "Multiplicación", "División", "Potencia", "Raiz enésima"]
for texto in lista_operaciones:
    tk.Button(ventana, text=texto, width=20, bg="#f4d9d9", command=lambda o=texto: operar(o)).pack(pady=3)

 # Resultado ventana 
resultado_label = tk.Label(
    ventana,
    text="Aquí aparecerá el resultado",
    bg="#ffffff",
    fg="#000000",
    font=("Arial", 11, "bold"),
    relief="ridge",
    width=45, 
    height=4, 
    justify="left" 
)
resultado_label.pack(pady=10)
    
# Brous aqui agreguen su nombre   
tk.Label(
    ventana,
    text="Integrantes:\nJuárez Ávila Erick Alejandro\n(aqui brous)",
    bg="#eb9191",
    fg="#0b3d91",
    font=("Arial", 9, "italic"),
    justify="right"
).pack(side="right", anchor="se", padx=10, pady=10)

ventana.mainloop()

  