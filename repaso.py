import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

lista_productos = ["1- Coca - 14 - 5 - coca_sf.png - 1", "2- Pan - 10 - 15 - pan.png - 1"]

# FUNCIONES

def agregar_producto():
    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("Agregar producto")
    ventana_emergente.geometry("200x250+400+200")
    etiqueta_nombre_ap = tk.Label(ventana_emergente, text="Nombre:")
    etiqueta_nombre_ap.place(x=10,y=10)
    entry_nombre_ap = tk.Entry(ventana_emergente)
    entry_nombre_ap.place(x=10,y=30)
    etiqueta_precio_ap = tk.Label(ventana_emergente, text="Precio:")
    etiqueta_precio_ap.place(x=10,y=60)
    entry_precio_ap = tk.Entry(ventana_emergente)
    entry_precio_ap.place(x=10,y=80)
    etiqueta_stock_ap = tk.Label(ventana_emergente, text="Stock:")
    etiqueta_stock_ap.place(x=10,y=110)
    entry_stock_ap = tk.Entry(ventana_emergente)
    entry_stock_ap.place(x=10,y=130)
    etiqueta_imagen_ap = tk.Label(ventana_emergente, text="Imagen:")
    etiqueta_imagen_ap.place(x=10,y=160)
    entry_imagen_ap = tk.Entry(ventana_emergente)
    entry_imagen_ap.place(x=10,y=180)


def elimiar_producto():
    seleccion = listbox.curselection()
    if seleccion:
        datos = listbox.get(seleccion[0])
        indice = lista_productos.index(datos)
        datos_s = datos.split("-")
        datos_s[5] = " 0"
        datos_a = "-".join(datos_s)
        lista_productos[indice] = datos_a
        listbox.delete(0, tk.END)
        for i in lista_productos:
            i_s = i.split("-")
            if i_s[5].strip() == "1":
                listbox.insert(tk.END, i)


def ver_producto():
    seleccion = listbox.curselection()
    if seleccion:
        datos = listbox.get(seleccion[0])
        datos_s = datos.split("-")
        nombre_producto = tk.Label(ventana, text=datos_s[1])
        nombre_producto.place(x=350, y=300)
        precio_producto = tk.Label(ventana, text=datos_s[2])
        precio_producto.place(x=350, y=330)
        stock_producto = tk.Label(ventana, text=datos_s[3])
        stock_producto.place(x=350, y=360)
        ruta_foto = datos_s[4].strip()
        imagen_producto = Image.open(ruta_foto)
        imagen_prod_r = imagen_producto.resize((200, 150), Image.Resampling.LANCZOS)
        nueva_imagen = ImageTk.PhotoImage(imagen_prod_r)
        lbl_imagen.config(image=nueva_imagen)
        lbl_imagen.image = nueva_imagen
        


# CODIGO APP
ventana = tk.Tk()
ventana.geometry("500x500+300+100")
ventana.title("APP KIOSKO")

etiqueta_nombre = tk.Label(ventana, text="nombre:")
etiqueta_nombre.place(x=300, y=300)
etiqueta_precio = tk.Label(ventana, text="precio:")
etiqueta_precio.place(x=300, y=330)
etiqueta_stock = tk.Label(ventana, text="stock:")
etiqueta_stock.place(x=300, y=360)


boton_agregar = tk.Button(ventana, text="agregar", command=agregar_producto)
boton_agregar.place(x=20, y=270)
boton_ver = tk.Button(ventana, text="ver", command=ver_producto)
boton_ver.place(x=20, y=300)
boton_editar = tk.Button(ventana, text="editar")
boton_editar.place(x=20, y=330)
boton_eliminar = tk.Button(ventana, text="eliminar", command=elimiar_producto)
boton_eliminar.place(x=20, y=360)

listbox = tk.Listbox(ventana, width=35)
listbox.place(x=20, y=20)
for i in lista_productos:
    i_s = i.split("-")
    if i_s[5].strip() == "1":
        listbox.insert(tk.END, i)


frame = tk.Frame(ventana, width=200, height=150)
frame.place(x=270, y=20)
frame.pack_propagate(False)
imagen_original = Image.open("image.png")
imagen_redimensionada = imagen_original.resize((300, 200), Image.Resampling.LANCZOS)
imagen_inicial = ImageTk.PhotoImage(imagen_redimensionada)
lbl_imagen = tk.Label(frame, image=imagen_inicial)
lbl_imagen.image = imagen_inicial # Guardar referencia inicial
lbl_imagen.pack(fill="both", expand=True)

ventana.mainloop()
