import json
import requests

r = requests.get("https://www.amiiboapi.com/api/amiibo/?amiiboSeries=Super%20Mario%20Bros.")
datos = r.json()
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


def mostrarListaNombres():
   cont = 0
   for i in datos["amiibo"]:
      print(i["name"])
      cont += 1
   print("Total de amiibos: ", cont)


def buscarPorNombre():
   nombre = input("Ingrese el nombre del amiibo: ")
   cont = 0
   for i in datos["amiibo"]:
      if i["name"] == nombre:
         print("Nombre: ", i["name"])
         print("Serie: ", i["amiiboSeries"])
         print("Fecha de lanzamiento: ", i["release"]["eu"])
         cont += 1
   if cont == 0:
      print("No se encontró ningún amiibo con ese nombre")
   print("\nTotal de amiibos: ", cont, "\n")

def mostrarDatos():
   for i in datos["amiibo"]:
      print("amiiboSeries:",i["amiiboSeries"], "\n"
            "character:", i["character"], "\n"
            "gameSeries:", i["gameSeries"], "\n"
            "id:", i["head"] + i["tail"], "\n"
            "image:", i["image"], "\n"
            "name:", i["name"], "\n"
            "release(eu):", i["release"]["eu"], "\n"
            "type:", i["type"], "\n"
            )

def mostrarLista():
   lista = []
   for i in datos["amiibo"]:
      lista.append(i["amiiboSeries"])
      lista.append(i["character"])
      lista.append(i["gameSeries"])
      lista.append(i["head"] + i["tail"])
      lista.append(i["image"])
      lista.append(i["name"])
      lista.append(i["release"]["eu"])
      lista.append(i["type"])
   print(lista)

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
   valor = input("Ingrese el valor: ")
   r = requests.get("https://www.amiiboapi.com/api/amiibo/?" + filtro + "=" + valor)
   datos = r.json()

# print del menú que hace llamadas a las funciones
opcion = 1 #inicializar variable para que entre al while
while opcion != 0:
   print("----------Menú----------")
   print("1. Mostrar lista de nombres")
   print("2. Buscar amiibos por nombre")
   print("3. Mostrar datos")
   print("4. Mostrar datos en forma de lista")
   print("5. Cambiar filtro de la API")
   print("0. Salir")
   print("-------------------------")
   opcion = int(input("Ingrese una opción: "))
   if opcion == 1:
      mostrarListaNombres()
   elif opcion == 2:
      buscarPorNombre()
   elif opcion == 3:
      mostrarDatos()
   elif opcion == 4:
      mostrarLista()
   elif opcion == 5:
      cambiarFiltro()
   elif opcion == 0:
      print("Saliendo...")
   else:
      print("Opción incorrecta")
