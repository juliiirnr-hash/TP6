#Ejercicio6.9
#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
#Funcion 
def celsius_a_fahrenheit(celsius):
    fahrenheit=celsius*1.8+32
    return fahrenheit
#Programa Principal
print("Convertido de grados Celsius a fahrenheit")
celsius=float(input("Ingrese la temperatura en °C: "))
print(f"{celsius} C°= {celsius_a_fahrenheit(celsius)} °F")
