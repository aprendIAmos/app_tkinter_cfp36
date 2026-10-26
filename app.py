import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi AAAAAAPP")
ventana.geometry("700x500+300+100")

# Botones
boton1  = tk.Button(ventana, text="Ver producto", height=2)
boton1.place(x=50, y=300)
boton2 = tk.Button(ventana, text="Editar producto", height=2)
boton2.place(x=150, y=300)
boton3 = tk.Button(ventana, text="Agregar producto", width=20, height=5)
boton3.place(x=70, y=350)


lista_productos = tk.Listbox(ventana, width=50, height=15)
lista_productos.place(x=20, y=20)

lista_productos.insert(tk.END, "1. Laptop Asus")
lista_productos.insert(tk.END, "2. Mouse Logitech")
lista_productos.insert(tk.END, "3. Teclado Mecánico")

frame_foto = tk.Frame(ventana, width=300, height=250)
frame_foto.place(x=350, y=20)
frame_foto.pack_propagate(False)
imagen = tk.PhotoImage(file="image.png")
lbl_imagen = tk.Label(frame_foto, image=imagen)
lbl_imagen.pack(fill="both", expand=True)

#Etiquetas
etiqueta_nombre = tk.Label(ventana, text="Nombre: ")
etiqueta_nombre.place(x=400, y=300)
etiqueta_precio = tk.Label(ventana, text="Precio: ")
etiqueta_precio.place(x=400, y=330)
etiqueta_stock = tk.Label(ventana, text="Stock: ")
etiqueta_stock.place(x=400, y=360)
etiqueta_descuento = tk.Label(ventana, text="Descuento: ")
etiqueta_descuento.place(x=400, y=390)

ventana.mainloop()