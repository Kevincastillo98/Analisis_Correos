import csv
import  re
import matplotlib.pyplot as plt
import collections
from collections import Counter



texto = open("emails.csv","r").read()


##Se hace uso de regex

emails = re.findall("@.*",texto)

lista = [i.split('.', 1)[0] for i in emails]

salida = Counter(lista)

##Salida es un diccionario

print(salida)

orden_salida = collections.OrderedDict(sorted(salida.items(), key=lambda t: t[1]))
print(orden_salida)


nueva_lista = salida.keys()
print(nueva_lista)


with open('emails.csv') as sexo:
   reader = csv.DictReader(sexo)
   genero = Counter(columna['Sexo'] for columna in reader)

print(genero)

variable_genero = list(genero.keys())
cantidad_genero = list(genero.values())

fig, ax = plt.subplots()
ax.pie(cantidad_genero, labels=variable_genero, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Variable Sexo')
plt.show()


with open('emails.csv') as edad:
   reader_edad = csv.DictReader(edad)
   edad = Counter(columna['Edad'] for columna in reader_edad)

print(edad)

orden_edad = collections.OrderedDict(sorted(edad.items()))
print(orden_edad)


plt.bar(list(orden_edad.keys()),orden_edad.values(), color='g')
plt.show()

##Se crea un bar plot


plt.bar(range(len(orden_salida)),list(orden_salida.values()),align='center')
plt.xticks(range(len(orden_salida)),list(orden_salida.keys()))
plt.show()


