import csv
import  re
import matplotlib.pyplot as plt
import seaborn as sns
import collections
import statistics
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

colors = ["#83a598","#d3869b"]
fig, ax = plt.subplots()
ax.pie(cantidad_genero, labels=variable_genero, colors=colors,autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Variable Sexo')
plt.show()


with open('emails.csv') as edad:
   reader_edad = csv.DictReader(edad)
   edad = Counter(columna['Edad'] for columna in reader_edad)

print(edad)

orden_edad = collections.OrderedDict(sorted(edad.items()))
print("edades:",orden_edad)


#media
multiplicacion = 0
div=0
for k, v in edad.items():
    multiplicacion += int(k)*int(v)
    div += v
media = multiplicacion/div
print("media:" ,media)

#Mediana

lista_edades = orden_edad.keys()
resultado = list(map(int,lista_edades))
mediana =statistics.median(resultado)
print("mediana:" , mediana)

plt.bar(list(map(int,orden_edad.keys())),orden_edad.values(),edgecolor="black",width=1, color='#8ec07c')
plt.axvline(media, color='r', linestyle='--')
plt.axvline(mediana, color='b', linestyle='--')
plt.grid()
plt.show()
##Se crea un bar plot

plt.bar(range(len(orden_salida)),list(orden_salida.values()),edgecolor="black",color="#83a598",align='center')
plt.xticks(range(len(orden_salida)),list(orden_salida.keys()))
plt.show()


