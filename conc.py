import glob
import csv

csvfiles = glob.glob("/home/kevin/Documentos/Analisis_Correos/correos/*.csv")
wf = csv.writer(open("/home/kevin/Documentos/Analisis_Correos/emails.csv","wb"),delimiter=",")

for files  in csvfiles:
    print(files)
    rd = csv.reader(open(files,"r"),delimiter=",")
    #rd.next()
    for row in rd:
        print(row)
        wf.writerow(row)

