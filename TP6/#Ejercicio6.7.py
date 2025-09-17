#Ejercicio6.7
#Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
# devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
#Funciones
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    division=a/b
    multiplicacion=a*b
    resultados_operaciones = (
    f"Suma: {suma}",
    f"Resta: {resta}",
    f"Division: {division}",
    f"Multiplicacion: {multiplicacion}"
)

    return resultados_operaciones

#Programa principal
a=float(input("Primer numero: "))
b=float(input("Segundo numero: "))
print(operaciones_basicas(a,b))