import tkinter as tk
from PIL import Image, ImageTk

# FUNCIONES

def actualizar_lista(lista):
    archivo = open("productos.txt", "w")
    for i in lista:
        archivo.write(i)
    archivo.close()

def cargar_lista():
    archivo = open("productos.txt", "r")
    lista_productos = archivo.readlines()
    archivo.close()
    return lista_productos

def editar_p_bbdd():
    lista_productos = cargar_lista()
    new_precio = " " + entry_precio_p.get() + " "
    new_stock = " " + entry_stock_p.get() + " "
    producto_s = lista_productos[indice_p_ep].split("-")
    producto_s[2] = new_precio
    producto_s[3] = new_stock
    producto_f = "-".join(producto_s)
    lista_productos[indice_p_ep] = producto_f
    print(lista_productos)
    actualizar_lista(lista_productos)
    cerrar_ventana_em_ep()
    cargar_productos()
    

def editar_producto():
    lista_productos = cargar_lista()
    seleccion = listbox.curselection()
    if seleccion:
        datos = listbox.get(seleccion[0])
        global indice_p_ep
        indice_p_ep = lista_productos.index(datos)
    datos_s = datos.split("-")
    global ventana_emergente_ep
    ventana_emergente_ep = tk.Toplevel(ventana)
    ventana_emergente_ep.title("Editar producto")
    ventana_emergente_ep.geometry("200x200+400+200")
    etiqueta_nombre_p = tk.Label(ventana_emergente_ep, text=f"Nombre_producto: {datos_s[1]}")
    etiqueta_nombre_p.place(x= 20, y=20)
    etiqueta_precio_p = tk.Label(ventana_emergente_ep, text=f"Precio: {datos_s[2]}")
    etiqueta_precio_p.place(x=20, y=60)
    etiqueta_stock_p = tk.Label(ventana_emergente_ep, text=f"Stock: {datos_s[3]}")
    etiqueta_stock_p.place(x=120, y=60)
    global entry_precio_p
    entry_precio_p = tk.Entry(ventana_emergente_ep, width=10)
    entry_precio_p.place(x=20, y=80)
    global entry_stock_p
    entry_stock_p = tk.Entry(ventana_emergente_ep, width=10)
    entry_stock_p.place(x=120, y=80)
    boton_aceptar = tk.Button(ventana_emergente_ep, text="Aceptar", command=editar_p_bbdd)
    boton_aceptar.place(x=20, y=120)
    boton_cancelar = tk.Button(ventana_emergente_ep, text="Cancelar", command=cerrar_ventana_em_ep)
    boton_cancelar.place(x=100, y=120)

def cargar_productos():
    listbox.delete(0, tk.END)
    lista_productos = cargar_lista()
    for i in lista_productos:
                i_s = i.split("-")
                if i_s[5].strip() == "1":
                    listbox.insert(tk.END, i)

def agregar_a_bbdd():
    lista_productos = cargar_lista()
    id_producto = len(lista_productos) + 1
    nombre_producto = entry_nombre_ap.get()
    precio_producto = entry_precio_ap.get()
    stock_producto = entry_stock_ap.get()
    imagen_producto = entry_imagen_ap.get()
    producto = f"{id_producto}- {nombre_producto} - {precio_producto} - {stock_producto} - {imagen_producto} - 1\n"
    lista_productos.append(producto)
    actualizar_lista(lista_productos)
    ventana_emergente.destroy()
    cargar_productos()

def cerrar_ventana_em_ep():
    ventana_emergente_ep.destroy()

def cerrar_ventana_em():
    ventana_emergente.destroy()

def agregar_producto():
    global ventana_emergente
    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("Agregar producto")
    ventana_emergente.geometry("200x250+400+200")
    etiqueta_nombre_ap = tk.Label(ventana_emergente, text="Nombre:")
    etiqueta_nombre_ap.place(x=10,y=10)
    global entry_nombre_ap
    entry_nombre_ap = tk.Entry(ventana_emergente)
    entry_nombre_ap.place(x=10,y=30)
    etiqueta_precio_ap = tk.Label(ventana_emergente, text="Precio:")
    etiqueta_precio_ap.place(x=10,y=60)
    global entry_precio_ap
    entry_precio_ap = tk.Entry(ventana_emergente)
    entry_precio_ap.place(x=10,y=80)
    etiqueta_stock_ap = tk.Label(ventana_emergente, text="Stock:")
    etiqueta_stock_ap.place(x=10,y=110)
    global entry_stock_ap
    entry_stock_ap = tk.Entry(ventana_emergente)
    entry_stock_ap.place(x=10,y=130)
    etiqueta_imagen_ap = tk.Label(ventana_emergente, text="Imagen:")
    etiqueta_imagen_ap.place(x=10,y=160)
    global entry_imagen_ap
    entry_imagen_ap = tk.Entry(ventana_emergente)
    entry_imagen_ap.place(x=10,y=180)
    boton_aceptar = tk.Button(ventana_emergente, text="Aceptar", command=agregar_a_bbdd)
    boton_aceptar.place(x=20, y=220)
    boton_cancelar = tk.Button(ventana_emergente, text="Cancelar", command=cerrar_ventana_em)
    boton_cancelar.place(x=100, y=220)


def elimiar_producto():
    lista_productos = cargar_lista()
    seleccion = listbox.curselection()
    if seleccion:
        datos = listbox.get(seleccion[0])
        indice = lista_productos.index(datos)
        datos_s = datos.split("-")
        datos_s[5] = " 0"
        datos_a = "-".join(datos_s)
        lista_productos[indice] = datos_a
        actualizar_lista(lista_productos)
        cargar_productos()

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


boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_producto)
boton_agregar.place(x=20, y=270)
boton_ver = tk.Button(ventana, text="Ver", command=ver_producto)
boton_ver.place(x=20, y=300)
boton_editar = tk.Button(ventana, text="Editar", command=editar_producto)
boton_editar.place(x=20, y=330)
boton_eliminar = tk.Button(ventana, text="Eliminar", command=elimiar_producto)
boton_eliminar.place(x=20, y=360)

listbox = tk.Listbox(ventana, width=35)
listbox.place(x=20, y=20)
cargar_productos()


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
