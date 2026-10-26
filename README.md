# APP Kiosko

Aplicación de escritorio desarrollada con Python y Tkinter para administrar el catálogo de productos de un kiosko. Los datos se guardan localmente en un archivo de texto y las imágenes se cargan desde la carpeta `images/`.

## Funcionalidades

- Mostrar los productos activos.
- Ver el nombre, precio, stock e imagen de un producto seleccionado.
- Agregar nuevos productos.
- Editar el precio y el stock de un producto existente.
- Eliminar productos mediante una baja lógica.
- Guardar los cambios automáticamente en `productos.txt`.

## Tecnologías

- Python 3
- Tkinter para la interfaz gráfica
- Pillow para abrir y redimensionar imágenes

## Requisitos previos

- Tener Python 3 instalado.
- Tener Tkinter disponible. En instalaciones estándar de Python suele venir incluido.
- Tener acceso a una terminal de Windows, como PowerShell o Símbolo del sistema.

## Instalación

1. Abre una terminal y entra a la carpeta del proyecto:

   ```powershell
   cd "c:\Users\Admin\Desktop\app_tkinter_cfp36"
   ```

2. Crea un entorno virtual:

   ```powershell
   py -m venv .venv
   ```

3. Activa el entorno virtual:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   Si PowerShell bloquea la ejecución de scripts, puedes usar esta terminal alternativa sin activar el entorno:

   ```powershell
   .\.venv\Scripts\python.exe app.py
   ```

4. Instala las dependencias:

   ```powershell
   python -m pip install -r requirements.txt
   ```

## Ejecutar la aplicación

Desde la raíz del proyecto, ejecuta:

```powershell
python app.py
```

O, con el entorno activado, puedes usar:

```powershell
py app.py
```

La aplicación abrirá una ventana titulada **APP KIOSKO**.

## Uso

1. Los productos activos aparecen en la lista principal.
2. Selecciona un producto y pulsa **Ver** para mostrar sus datos e imagen.
3. Pulsa **Agregar** para crear un producto ingresando nombre, precio, stock y nombre o ruta de su imagen.
4. Selecciona un producto y pulsa **Editar** para modificar su precio y stock.
5. Selecciona un producto y pulsa **Eliminar** para ocultarlo de la lista.

## Datos almacenados

La información de los productos se guarda en `productos.txt` con el siguiente formato:

```text
ID- Nombre - Precio - Stock - Imagen - Estado
```

Por ejemplo:

```text
1- Coca - 10 - 2 - coca.png - 1
2- Pan - 10 - 3 - pan.png - 1
```

- El último campo indica el estado: `1` corresponde a activo y `0` a eliminado.
- Las rutas e imágenes deben ser válidas desde la carpeta raíz del proyecto.
- Las imágenes incluidas se encuentran en `images/`.

## Importante

- Ejecuta la aplicación desde la raíz del proyecto, ya que `app.py` utiliza rutas relativas como `productos.txt` y `images/image.png`.
- `productos.txt` debe conservar el formato separado por guiones para que el programa pueda cargar y editar los datos correctamente.
