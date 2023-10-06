import json
import requests

r = requests.get(
   "https://www.amiiboapi.com/api/amiibo/?amiiboSeries=Super%20Mario%20Bros."
)
# print(r.text)
data = r.json()
# print para ver el nombre de los todos los amiibos


def mostrarListaNombres():
   cont = 0
   for i in data["amiibo"]:
      print(i["name"])
      cont += 1
   print("Total de amiibos: ", cont)


def buscarNombre():
   nombre = input("Ingrese el nombre del amiibo: ")
   encontrado = False
   for i in data["amiibo"]:
      while encontrado == False:
            if i["name"] == nombre:
               print("Nombre: ", i["name"])
               print("Serie: ", i["amiiboSeries"])
               print("Tipo: ", i["type"])
               encontrado = True
   if encontrado == False:
      print("No se encontró el amiibo")


# print del menú que hace llamadas a las funciones
print("----------Menú----------")
print("1. Buscar amiibo por nombre")
print("2. Buscar amiibo por serie")
print("-------------------------")
opcion = int(input("Ingrese una opción: "))
if opcion == 1:
   mostrarListaNombres()
if opcion == 2:
   buscarNombre()
