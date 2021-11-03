import csv
archivo = open('laboratorio_II/clase7/01/0-datos.csv', 'w', newli
# lector_csv = csv.reader(archivo)
escritor_csv = csv.writer(archivo, delimiter=',', quotechar='"')
# lector_csv = csv.reader(archivo, delimiter=',', quotechar='"')

# Escribir los datos
escritor_csv.writerow(['jose', 'sanchez', 'js@correo.com'])


# Cerrar archivo
archivo.close()