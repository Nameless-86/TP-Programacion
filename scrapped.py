##Llamo a la libreria csv para poder manipular listings.csv
import csv
#Variables para contar o llenar
dias = []
counter = 0

#abro el archivo
with open('listings.csv') as csvfile:
    archivo = csv.reader(csvfile)
    for i in archivo:
            dias.append(i[15])
#Hago una lista con la columna de los dias disponibles al año y le saco el titulo

dias.pop(0)
#paso los valores de str a ints
for j in range(0, len(dias)):
    dias[j] = int(dias[j])
#Itero por todos los dias de la lista, si alguno es igual a 365 lo cuento
for k in dias:
    if k == 365:
        print(k)
        counter += 1
        
print(dias)
print("De todos los alojamientos", counter, "Estan disponibles todo el año")