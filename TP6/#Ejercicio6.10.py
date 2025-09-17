#Ejercicio6.10
#Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.
#Funcion
def calcular_promedio(a, b, c):
    promedio=(a+b+c)/3
    return promedio
#Programa Principal
print("Calcular promedio de tres numeros")
a=float(input("Ingrese el primer numero: "))
b=float(input("Ingrese el segundo numero: "))
c=float(input("Ingrese el tercer numero: "))
print(f"Promedio={calcular_promedio(a,b,c)}")
