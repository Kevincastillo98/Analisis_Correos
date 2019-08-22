import glob
import csv
import pandas as pd

archivo = glob.glob("/home/kevin/Documentos/Analisis_Correos/correos/*.csv")
wf = csv.writer(open("/home/kevin/Documentos/Analisis_Correos/emails.csv","wb"),delimiter=",")

for i  in archivo:
    #print(i)
    rd = csv.reader(open(i,"r"),delimiter=",")
    #rd.next()
    for fila in rd:
        #print(fila)
        wf.writerow(fila)


with open('emails.csv', 'w') as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames = ["Apellido Paterno", "Apellido Materno","Nombre","Sexo","Edad","Correo"])
    writer.writeheader()
