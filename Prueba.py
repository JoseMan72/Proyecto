import json
import requests

r = requests.get(
   "https://www.amiiboapi.com/api/amiibo/?amiiboSeries=Super%20Mario%20Bros."
)
# print(r.text)
datos = r.json()

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


# print del menú que hace llamadas a las funciones
opcion = 1 #inicializar variable para que entre al while
while opcion != 0:
   print("----------Menú----------")
   print("1. Mostrar lista de nombres")
   print("2. Buscar amiibos por nombre")
   print("0. Salir")
   print("-------------------------")
   opcion = int(input("Ingrese una opción: "))
   if opcion == 1:
      mostrarListaNombres()
   if opcion == 2:
      buscarPorNombre()
