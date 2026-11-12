maximo = 20
asignados = 0
cantidad_de_liberados = 0

print("¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Investigación!")
print("=== MENÚ PRINCIPAL ===")
print("1.- Equipos disponibles.")
print("2.- Asignar equipo.")
print("3.- Liberar equipo.")
print("4.- Historial de usos.")
print("5.- Salir.")
opcion = int(input("Ingrese alguna de las opciones: \n"))
while opcion != 5:
    match opcion:
        case 1:
            print()
        case 2:
            asignar = int(input("Ingrese la cantidad de investigadores a registrar"))
            if asignar <= 0:
                print("Error")
            else:
                asignados += asignar
        case 3:
            Liberar = int(input("Ingrese la cantidad de equipos para liberar."))
            if Liberar > 0 and Liberar < maximo:
                asignados -= Liberar
                cantidad_de_liberados = Liberar
        case 4:
            print(f'El historial de usos es de: se han asignado un total de: {asignados} Y de eliminados es de: {cantidad_de_liberados}')

print("Gracias por utilizar nuestro software, hasta la proxima")