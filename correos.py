import  re
import matplotlib.pyplot as plt
from collections import Counter

texto = open("emails.csv","r").read()


##Se hace uso de regex

emails = re.findall("@.*",texto)

lista = [i.split('.', 1)[0] for i in emails]

salida = Counter(lista)

##Salida es una lista

print(salida)

##Se crea un bar plot

plt.bar(range(len(salida)),list(salida.values()),align='center')
plt.xticks(range(len(salida)),list(salida.keys()))
plt.show()


