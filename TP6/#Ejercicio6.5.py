#Ejercicio6.5
#Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.
#Funcion
def segundos_a_horas(segundos):
    Horas=segundos/3600
    return Horas
#Programa Principal
segundos=float(input("Ingresar segundos: "))
print(f"{segundos} segundo/s equivale a {segundos_a_horas(segundos)} hora/s")