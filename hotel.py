reservas = []


def mostrar_menu():
    print("\n======== MENÚ PRINCIPAL ========")
    print("1. Agregar reserva")
    print("2. Buscar reserva")
    print("3. Eliminar reserva")
    print("4. Confirmar reservas")
    print("5. Mostrar reservas")
    print("6. Salir")
    print("=================================")

def leer_opcion():
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion >= 1 and opcion <= 6:
            return opcion
        else:
            print("Opción inválida.")
            return 0
    except ValueError:
        print("Debe ingresar un número.")
        return 0


def validar_huesped(nombre):
    return nombre.strip() != ""


def validar_habitacion(habitacion):
    return habitacion >= 1 and habitacion <= 200


def validar_noches(noches):
    return noches > 0


def agregar_reserva(lista):
    huesped = input("Ingrese nombre del huésped: ")

    if not validar_huesped(huesped):
        print("El nombre no puede estar vacío.")
        return

    try:
        habitacion = int(input("Ingrese número de habitación: "))
    except ValueError:
        print("La habitación debe ser un número entero.")
        return

    if not validar_habitacion(habitacion):
        print("La habitación debe estar entre 1 y 200.")
        return

    try:
        noches = int(input("Ingrese cantidad de noches: "))
    except ValueError:
        print("Las noches deben ser un número entero.")
        return

    if not validar_noches(noches):
        print("La cantidad de noches debe ser mayor que cero.")
        return

    reserva = {
        "huesped": huesped,
        "habitacion": habitacion,
        "noches": noches,
        "confirmada": False
    }

    lista.append(reserva)
    print("Reserva agregada correctamente.")


def buscar_reserva(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["huesped"] == nombre:
            return i
    return -1


def eliminar_reserva(lista):
    nombre = input("Ingrese el nombre del huésped a eliminar: ")
    posicion = buscar_reserva(lista, nombre)

    if posicion != -1:
        lista.pop(posicion)
        print("Reserva eliminada correctamente.")
    else:
        print(f"La reserva del huésped '{nombre}' no se encuentra registrada.")


def confirmar_reservas(lista):
    for reserva in lista:
        if reserva["noches"] >= 2:
            reserva["confirmada"] = True
        else:
            reserva["confirmada"] = False


def mostrar_reservas(lista):
    confirmar_reservas(lista)

    if len(lista) == 0:
        print("No hay reservas registradas.")
        return

    print("\n=== LISTA DE RESERVAS ===")
    for reserva in lista:
        print("Huésped:", reserva["huesped"])
        print("Habitación:", reserva["habitacion"])
        print("Noches:", reserva["noches"])

        if reserva["confirmada"]:
            print("Estado: CONFIRMADA")
        else:
            print("Estado: PENDIENTE")

        print("********************************************")


while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_reserva(reservas)

    elif opcion == 2:
        nombre = input("Ingrese el nombre del huésped a buscar: ")
        posicion = buscar_reserva(reservas, nombre)

        if posicion != -1:
            print("Reserva encontrada en la posición:", posicion)
            print(reservas[posicion])
        else:
            print("No se encontró la reserva.")

    elif opcion == 3:
        eliminar_reserva(reservas)

    elif opcion == 4:
        confirmar_reservas(reservas)
        print("Reservas confirmadas correctamente.")

    elif opcion == 5:
        mostrar_reservas(reservas)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break