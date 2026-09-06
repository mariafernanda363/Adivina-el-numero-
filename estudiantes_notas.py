# INICIO

# leer las notas del estudiante

nota1 = float(input("ingrese la primer nota: "))
nota2 = float(input("ingrese la segunda nota: "))
nota3 = float(input("ingrese la tercer nota: "))

# calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3

# validar si aprobo o no
if promedio >= 30.0:
    resultado = "APROBADO"
else:
    resultado = "REPROBADO"

# escribir resultado
print("El promedio es: ", promedio)
print("Resultado: ", resultado)

# FIN