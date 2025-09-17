#Ejercicio6.3
#Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
#  Pedir los datos al usuario y llamar a esta función con los valores ingresados
#Funcion
def informacion_personal(nombre,apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia} .")
#Programa Primcipal
nombre=str(input("Nombre: "))
apellido=str(input("apellido: "))
edad=str(input("edad: "))
residencia=str(input("Residencia: "))
informacion_personal(nombre,apellido,edad, residencia)