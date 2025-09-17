
#Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice demasa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
#Funcion
def calcular_imc(peso, altura):
    imc=peso/(altura)**2
    imc_redondeado=round(imc,2)
    return imc_redondeado

#Programa Principal
peso=float(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su peso en metros: "))

print(f"Indice de masa corporal: {calcular_imc(peso,altura)}")

