import csv
import  re
import matplotlib.pyplot as plt
from collections import Counter


texto = open("emails.csv","r").read()


##Se hace uso de regex

emails = re.findall("@.*",texto)

lista = [i.split('.', 1)[0] for i in emails]

salida = Counter(lista)

##Salida es un diccionario

print(salida)


nueva_lista = salida.keys()
print(nueva_lista)


with open('emails.csv') as sexo:
   reader = csv.DictReader(sexo)
   genero = Counter(columna['Sexo'] for columna in reader)

print(genero)


#with open('emails.csv') as sexo:
#   reader = csv.DictReader(sexo)
#   genero = Counter(columna['sexo'] for columna in reader)

#print(genero)

##Se crea un bar plot


plt.bar(range(len(salida)),list(salida.values()),align='center')
plt.xticks(range(len(salida)),list(salida.keys()))
plt.show()


