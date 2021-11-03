import csv
archivo = open('laboratorio_II/clase7/00/00-datos.csv')
lector_csv = csv.reader(archivo)
# lector_csv = csv.reader(archivo, delimiter=',', quotechar='"')

#Leer supuesto encabezados
#encabezados = next(lector_csv)
# print('encabezados: '+str(encabezados))
for fila in lector_csv:
    print(f''' 
    Nombre: {fila[0]}
    Apellido: {fila[1]}
    Mail: {fila[2]}''')

archivo.close()