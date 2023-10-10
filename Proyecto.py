import json
import requests

#Descarga de datos de la API
r = requests.get("https://www.amiiboapi.com/api/amiibo/?amiiboSeries=Super%20Mario%20Bros.")
datos = r.json()
# Selecciono la lista de amiibos y la guardo en la variable
lista = []
for i in datos["amiibo"]:
   lista.append(i)
datos = lista

# Ejemplo de datos
#{
#      "amiiboSeries": "Super Mario Bros.",
#      "character": "Mario",
#      "gameSeries": "Super Mario",
#      "head": "00000000",
#      "image": "https://raw.githubusercontent.com/N3evin/AmiiboAPI/master/images/icon_00000000-00340102.png",
#      "name": "Mario",
#      "release": {
#        "au": "2015-03-21",
#        "eu": "2015-03-20",
#        "jp": "2015-03-12",
#        "na": "2015-03-20"
#      },
#      "tail": "00340102",
#      "type": "Figure"
#    }
# Donde head y tail forman el id del amiibo


#*----------Funciones----------*

# Función que muestra la lista de nombres de los amiibos
def mostrarListaNombres():
   cont = 0
   for i in datos:
      print(i["name"])
      cont += 1
   print("Total de amiibos: ", cont)

# Función que busca un amiibo por nombre
def buscarPorNombre():
   nombre = input("Ingrese el nombre del amiibo: ")
   cont = 0
   for i in datos:
      if i["name"] == nombre:
         print("Nombre: ", i["name"])
         print("Serie: ", i["amiiboSeries"])
         print("Fecha de lanzamiento: ", i["release"]["eu"])
         cont += 1
   if cont == 0:
      print("No se encontró ningún amiibo con ese nombre \n")

# Función que muestra todos los datos de los amiibos
def mostrarDatos():
   for i in datos:
      print("amiiboSeries:",i["amiiboSeries"], "\n"
            "character:", i["character"], "\n"
            "gameSeries:", i["gameSeries"], "\n"
            "id:", i["head"] + i["tail"], "\n"
            "image:", i["image"], "\n"
            "name:", i["name"], "\n"
            "release(eu):", i["release"]["eu"], "\n"
            "type:", i["type"], "\n"
            )

# Función que muestra todos los datos de los amiibos según los datos que se le pasen
def mostrarDatos2(datosAMostrar):
   for i in datosAMostrar:
      print("amiiboSeries:",i["amiiboSeries"], "\n"
            "character:", i["character"], "\n"
            "gameSeries:", i["gameSeries"], "\n"
            "id:", i["head"] + i["tail"], "\n"
            "image:", i["image"], "\n"
            "name:", i["name"], "\n"
            "release(eu):", i["release"]["eu"], "\n"
            "type:", i["type"], "\n"
            )

# Función que cambia el filtro de la API
def cambiarFiltro():
   print("Filtros disponibles: ")
   print("amiiboSeries")
   print("character")
   print("gameSeries")
   print("id") #id = head + tail
   print("image")
   print("name")
   print("release(eu)")
   print("type")

   filtro = input("Ingrese el filtro: ")
   if filtro == "id":
      filtro = input("¿Buscamos por head o tail?: (H/T) ") #Uso la misma variable para no crear otra innecesariamente
      if filtro == "H":
         filtro = "head"
      elif filtro == "T":
         filtro = "tail"
   
   valor = input("Ingrese el valor: ")
   r = requests.get("https://www.amiiboapi.com/api/amiibo/?" + filtro + "=" + valor)
   datos = r.json()

# Función que muestra todos los datos de los amiibos sin filtro
def mostrarDatosSinFiltro():
   #Auxiliar para no perder los datos originales
   rAux = requests.get("https://www.amiiboapi.com/api/amiibo/")
   datosAux = rAux.json()
   mostrarDatos2(datosAux)

# Función que muestra los amiibos que salieron en una fecha
def mostrarSegunFecha():
   fecha = input("Ingrese la fecha (yyyy-mm-dd): ")
   cont = 0
   for i in datos:
      if i["release"]["eu"] == fecha:
         print("Nombre: ", i["name"])
         print("Serie: ", i["amiiboSeries"])
         print("Fecha de lanzamiento: ", i["release"]["eu"])
         cont += 1
   if cont == 0:
      print("No se encontró ningún amiibo con esa fecha")
   print("\nTotal de amiibos: ", cont, "\n")

# Función que modifica los datos
def modificarDatos():
   opcion = 1
   while opcion != 0:
      print("¿Borrar o añadir o modificar dato?: (1/2/3)")
      print("0. Salir")
      opcion = input()
      if opcion == 1:
         id = input("id del amiibo a borrar: ")
         for i in datos:
            if i["head"] + i["tail"] == id:
               datos.remove(i)
               print("Amiibo borrado")
      elif opcion == 2:
         amiiboNuevo = {}
         print("Ingrese los datos del amiibo: ")
         print("amiiboSeries")
         amiiboNuevo["amiiboSeries"] = input("amiiboSeries: ")
         print("character")
         amiiboNuevo["character"] = input("character: ")
         print("gameSeries")
         amiiboNuevo["gameSeries"] = input("gameSeries: ")
         print("head")
         amiiboNuevo["head"] = input("head: ")
         print("image")
         amiiboNuevo["image"] = input("image: ")
         print("name")
         amiiboNuevo["name"] = input("name: ")
         print("release(eu)")
         amiiboNuevo["release"]["eu"] = input("release(eu): ")
         print("tail")
         amiiboNuevo["tail"] = input("tail: ")
         print("type")
         amiiboNuevo["type"] = input("type: ")

         #Añado el amiibo a la lista
         datos.append(amiiboNuevo)
         print("Amiibo añadido")
      elif opcion == 3:
         id = input("id del amiibo a modificar: ")
         for i in datos:
            if i["head"] + i["tail"] == id:
               print("Datos del amiibo: ")
               print("amiiboSeries:",i["amiiboSeries"], "\n"
                     "character:", i["character"], "\n"
                     "gameSeries:", i["gameSeries"], "\n"
                     "head:", i["head"], "\n"
                     "image:", i["image"], "\n"
                     "name:", i["name"], "\n"
                     "release(eu):", i["release"]["eu"], "\n"
                     "tail:", i["tail"], "\n"
                     "type:", i["type"], "\n"
                     )
               print("¿Qué dato desea modificar?")
               print("1. amiiboSeries")
               print("2. character")
               print("3. gameSeries")
               print("4. head")
               print("5. image")
               print("6. name")
               print("7. release(eu)")
               print("8. tail")
               print("9. type")
               print("0. Salir")
               opcion = 1
               while opcion != 0:
                  opcion = input()
                  if opcion == 1:
                     print("amiiboSeries")
                     i["amiiboSeries"] = input("amiiboSeries: ")
                  elif opcion == 2:
                     print("character")
                     i["character"] = input("character: ")
                  elif opcion == 3:
                     print("gameSeries")
                     i["gameSeries"] = input("gameSeries: ")
                  elif opcion == 4:
                     print("head")
                     i["head"] = input("head: ")
                  elif opcion == 5:
                     print("image")
                     i["image"] = input("image: ")
                  elif opcion == 6:
                     print("name")
                     i["name"] = input("name: ")
                  elif opcion == 7:
                     print("release(eu)")
                     i["release"]["eu"] = input("release(eu): ")
                  elif opcion == 8:
                     print("tail")
                     i["tail"] = input("tail: ")
                  elif opcion == 9:
                     print("type")
                     i["type"] = input("type: ")
                  elif opcion == 0:
                     print("Saliendo...")
                  else:
                     print("Opción incorrecta\n")
            else:
               print("No se encontró ningún amiibo con ese id\n")
      elif opcion != 0:
         print("Opción incorrecta\n")

#*----------Programa Principal----------*
# print del menú que hace llamadas a las funciones
opcion = 1 #inicializar variable para que entre la primera vez al while
while opcion != 0:
   print("--------------------Menú--------------------")
   print("1. Mostrar lista de nombres")
   print("2. Buscar amiibos por nombre")
   print("3. Mostrar datos")
   print("4. Cambiar filtro de la API")
   print("5. Mostrar todos los datos sin filtro")
   print("6. Mostrar amiibos que salieron en una fecha")
   print("7. Modificar datos")
   print("0. Salir")
   print("--------------------------------------------")
   opcion = int(input("Ingrese una opción: "))

   #Llamadas a las funciones según la opción elegida
   if opcion == 1:
      mostrarListaNombres()
   elif opcion == 2:
      buscarPorNombre()
   elif opcion == 3:
      mostrarDatos()
   elif opcion == 4:
      cambiarFiltro()
   elif opcion == 5:
      mostrarDatosSinFiltro()
   elif opcion == 6:
      mostrarSegunFecha()
   elif opcion == 7:
      modificarDatos()
   elif opcion == 0:
      print("Saliendo...")
   else:
      print("Opción incorrecta, elija una opciones del menú (0-7) \n")
