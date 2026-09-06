numero_secreto = 17

for intento in range(1, 6):

    numero_usuario = int(input("Intento " + str(intento) + ": ingrese un numero del 1 al 20: "))

    if numero_usuario == numero_secreto:
        print("¡Felicitaciones! Adivinaste el numero secreto.")
        break

    elif numero_usuario < numero_secreto:
        print("El numero secreto es mayor.")

    else:
        print("El numero secreto es menor.")

    if intento == 5:
        print("Lo siento,se acabaron los 5 intentos.")
        print("El numero secreto era:", numero_secreto)
        
