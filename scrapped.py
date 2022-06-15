##Llamo a la libreria csv para poder manipular listings.csv
import csv
#Variables para contar o llenar
dicti = {}
dias= []

counter = 0

#abro el archivo
with open('listings.csv') as csvfile:
    archivo = csv.reader(csvfile, delimiter=',')
    for i in archivo:
        #Esto tendria que leer el titulo de la columna y pararse dependiendo lo que se le pida 
        #TERMINAR
        dicti[i[1]]=i[15]

print(dicti)

#paso los valores de str a ints
for j in dicti:
    #hay que sacar el primer elemento de la columna porque es un string con una palabra y no pasa a entero
    print(dicti[j])

#Falta contar por cada barrio o tipo de habitacion

#Itero por todos los dias de la lista, si alguno es igual a 365 lo cuento
# for k in dias:
#     if k == 365:
#         print(k)
#         counter += 1
        
# print(dias)
print("De todos los alojamientos", counter, "Estan disponibles todo el año")