import csv
import math
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

orden_salida = collections.OrderedDict(sorted(salida.items(), key=lambda t: t[1]))
print("Conteo de Dominio:",orden_salida,"\n")

nueva_lista = salida.keys()
#print(nueva_lista)


with open('emails.csv') as sexo:
   reader = csv.DictReader(sexo)
   genero = Counter(columna['Sexo'] for columna in reader)

print("Conteo de Genero:" , genero,"\n")

variable_genero = list(genero.keys())
cantidad_genero = list(genero.values())

colors = ["#d3869b","#83a598"]
fig, ax = plt.subplots()
ax.pie(cantidad_genero, labels=variable_genero, colors=colors,autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Variable Sexo')
plt.show()


with open('emails.csv') as edad:
   reader_edad = csv.DictReader(edad)
   edad =Counter(columna['Edad'] for columna in reader_edad)

orden_edad = collections.OrderedDict(sorted(edad.items()))
print("Conteo de edades:",orden_edad,"\n")

##Se obtiene la lista para obtener las medidas de tendencia central 

with open("emails.csv") as edad_orden:
    reader_edad = csv.DictReader(edad_orden)
    edad_orden = list(columna["Edad"] for columna in reader_edad)

orden = list(map(int,edad_orden))
lista_orden = sorted(orden)


#media
multiplicacion = 0
div=0
for k, v in edad.items():
    multiplicacion += int(k)*int(v)
    div += v
media = multiplicacion/div
print("Media:" ,media)

#Mediana

lista_edades = orden_edad.keys()
resultado = list(map(int,lista_edades))
mediana =statistics.median(resultado)
print("Mediana:" , mediana)

#varianza estandar

acumulador1 = 0
for m in range(len(lista_orden)):
    acumulador1 +=((lista_orden[m]-media)**2)
calculo_var = acumulador1/len(lista_orden)
print("Varianza:" , calculo_var)

##Desviacion

desviacion = math.sqrt(calculo_var)
print("Desviacion:" , desviacion)

##Asimetria

acumulador2 = 0
for n in range(len(lista_orden)):
    acumulador2 += ((lista_orden[n]-media)**3)
numerador_asim = acumulador2/len(lista_orden)
asimetria = (1/(desviacion)**3)*(numerador_asim)
print("Asimetria:", asimetria)

##Curtosus
acumulador3 = 0
for o in range(len(lista_orden)):
    acumulador3 += ((lista_orden[o]-media)**4)
numerador_curto = acumulador3/len(lista_orden)
curtosis =(1/(desviacion)**4)*(numerador_curto)
print("Curtosis:",curtosis,"\n")


#plt.title("Distribucion de edades", fontsize=20, y=1.012)
plt.title(r"$\sigma=%0.1f$" % desviacion + "\t\t" + r"$Curtosis=%0.1f$" % curtosis + "\t\t" + r"$Asimetria=%0.1f$" % asimetria)
nombres =["mediana","media"]
colores = ["red","blue"]
medidas = [mediana, media]
plt.bar(list(map(int,orden_edad.keys())),orden_edad.values(),edgecolor="black",width=1, color='#8ec07c')
for medidas, nombres, colores in zip(medidas, nombres, colores):
    plt.axvline(x=medidas, linestyle='--', linewidth=2.5, label='{0} at {1}'.format(nombres, medidas), c=colores)

plt.legend();
plt.grid()
plt.show()
##Se crea un bar plot

plt.bar(range(len(orden_salida)),list(orden_salida.values()),edgecolor="black",color="#83a598",align='center')
plt.xticks(range(len(orden_salida)),list(orden_salida.keys()))
plt.show()


with open('emails.csv') as sexo:
    reader = csv.DictReader(sexo)
    for columna_sexo in reader:
        contenido = list(columna_sexo['Sexo'] for columna_sexo in reader)

salida = list(zip(lista,contenido))


conteo_salida = {} 
for i in salida:
    conteo_salida[i] = conteo_salida.get(i, 0) +1
print("Agrupacion Dominio-Sexo:" ,conteo_salida,"\n") 

#orden_conteo = collections.OrderedDict(sorted(conteo_salida.items()))
orden_conteo = collections.OrderedDict(sorted(conteo_salida.items(), key=lambda t: t[1]))
plt.bar(range(len(orden_conteo)),list(orden_conteo.values()),edgecolor="black",color="#83a598",align='center')
plt.xticks(range(len(orden_conteo)),list(orden_conteo.keys()))
plt.show()

