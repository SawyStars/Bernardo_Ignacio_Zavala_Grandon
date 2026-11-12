Registrar = 0
investigadores_Principales = 0
investigadores_Asistentes = 0
while Registrar < 1: 
    Registrar = int(input("Ingrese la cantidad cientificos que quiere registrar \n"))
    if Registrar < 1:
        print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")

for i in range(Registrar):
    ID =  input(f"Ingrese el ID del cientifico {i+1}\n\n")
    if len(ID) >= 6:
        print()
    else:
        while len(ID) < 6:
            print("¡Dato de investigación inválido! Ingrese ID correctamente.")
            ID =  input(f"Ingrese el ID del cientifico {i+1}\n\n")
    publicaciones = int(input("Ingrese el número de publicaciones del cientifico. \n"))
    if publicaciones < 1:
        print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
    else:
        if publicaciones > 10:
            investigadores_Principales += 1
        else:
            investigadores_Asistentes += 1

print(f"¡El instituto cuenta con {investigadores_Principales} Investigadores Principales y {investigadores_Asistentes} Investigadores Asistentes! ¡Ciencia en marcha!")