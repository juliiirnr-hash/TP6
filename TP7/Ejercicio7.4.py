def buscar_contacto(contactos):
   nombre_buscado=input("Ingrese el nombre que desea buscar: ")
   if nombre_buscado in contactos:
          print(f"📞 El número de {nombre_buscado} es: {contactos[nombre_buscado]}")
   else:
        print(f"❌ No se encontró ningún contacto con el nombre {nombre_buscado}")




def agregar_contactos(contactos):
    
    count=0
    for i in range(5):
       Nombre_de_Contacto=input(f"Ingrese el nombre de contacto {i+1}: ")
       while True:
         Numero_de_Contacto=(input(f"Ingrese el numero de contacto {i+1}: "))
         if Numero_de_Contacto.isdigit() and len(Numero_de_Contacto) == 10:
            contactos[Nombre_de_Contacto] = Numero_de_Contacto
            print(" Número válido. Contacto guardado.")
            break
       else:
            print("El número debe tener 10 dígitos y ser completamente numérico.")
            continue
    print(contactos)


#########PROGRAMA PRINCIPAL###############
print("Agenda Personal")
contactos={}
agregar_contactos(contactos)
buscar_contacto(contactos)