Proyecto sobre datos de los coleccionables Amiibos de Nintendo provenientes de una API externa, usando Python y la biblioteca requests.

El Python usado es el Python 3.11.6 junto a la biblioteca requests en la versión 2.31.0.
   Instalamos python3 con el comando `pip install python3`
   Es recomendable utilizar un entorno virtual, personalmente recomiendo virtualenvwrapper, que se puede instalar con el comando 
   `pip install virtualenvwrapper-win` en la terminal.
   Para crear un entorno virtual se debe ejecutar el comando `mkvirtualenv nombre_entorno` y para activarlo `workon nombre_entorno` y 
   ya dentro del entorno virtual se debe instalar la biblioteca requests con el comando `pip install requests`.
   Otra manera de instalar todas las bibliotecas necesarias es ejecutando el comando `pip install -r requirements.txt` ya que este archivo
   contiene todas las bibliotecas necesarias para ejecutar el programa.

La mejor manera de descargarse al programa, es clonar el repositorio desde vscode o desde la terminal con el comando git clone.


Este proyecto cuenta con 6 funcionalidades dentro de las cuales se encuentran:
1- Mostrar lista de nombres de los Amiibos.
   Esta funcionalidad muestra una lista de los nombres de los Amiibos.

2- Buscar un Amiibo por nombre.
   Esta funcionalidad busca un Amiibo por nombre y muestra su nombre, serie y 
   fecha de lanzamiento. Si no lo encuentra muestra un mensaje de error.

3- Mostrar datos.
   Esta funcionalidad muestra los datos de todos los Amiibos según la API.

4- Cambiar filtro de la API
   Esta funcionalidad cambia el filtro de la API para que muestre los Amiibos
   según el filtro elegido, ya sea por nombre, serie, fecha de lanzamiento, id...

5- Mostrar todos los datos sin filtro
   Esta funcionalidad muestra todos los datos de los Amiibos de toda la API, sin importar el filtro seleccionado.

6- Mostrar amiibos que salieron en una fecha seleccionada
   Esta funcionalidad muestra los amiibos que salieron en una fecha seleccionada por el usuario.

7- Modificar datos
   Esta funcionalidad modifica los datos de la API, ya sea añadir un amiibo, eliminarlo o modificar uno existente.

Para ejecutar el programa se debe ejecutar el archivo proyecto.py, como un archivo de Python desde la terminal usando el comando 
`python3 proyecto.py` o desde un IDE.