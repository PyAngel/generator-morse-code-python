import tkinter as tk
from morse import diccionario_morse  
from sonido import texto_a_morse

texto_ingresado_global = ""

def procesar_texto():
    global texto_ingresado_global
    texto_ingresado_global = entrada_texto.get()
    texto_ingresado_global = texto_ingresado_global.lower()
    texto_procesado = "".join(filter(lambda i: i.isalnum(), texto_ingresado_global))
    texto_a_morse(texto_procesado,diccionario_morse)

ventana = tk.Tk()
ventana.title("Conversor Código Morse V1.0")

entrada_texto = tk.Entry(ventana, width=70)
entrada_texto.pack(pady=10)

boton_mostrar = tk.Button(ventana, text="Convertir", command=procesar_texto)
boton_mostrar.pack()

etiqueta_valores = tk.Label(ventana, text="")
etiqueta_valores.pack(pady=10)

ventana.mainloop()
