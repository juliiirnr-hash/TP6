##Ejercicio6.4
#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
#calcular_peri metro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados
#Funcion Area
def calcular_area_circulo(radio):
    import math
    valor_de_pi=math.pi
    Formula_de_area=valor_de_pi*radio**2
    return Formula_de_area
#Funcion de perimetro
def calcular_perimetro_circulo(radio):
    import math
    valor_de_pi=math.pi
    Formula_de_perimetro=valor_de_pi*radio*2
    return Formula_de_perimetro
#Programa principal

#Datos necesarios
radio=float(input("Ingrese el radio: "))
Area=calcular_area_circulo(radio)
Perimetro=calcular_perimetro_circulo(radio)
print(f"Area: {Area}       Perimetro: {Perimetro}")
