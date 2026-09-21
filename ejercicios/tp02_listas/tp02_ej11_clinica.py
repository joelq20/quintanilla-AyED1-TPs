# Resolver el siguiente problema, diseñando las funciones a utilizar:
#Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
#ingresa se anuncia en la recepción indicando su número de afiliado (número entero
#de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
#turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
#se solicita:
#a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
#los pacientes atendidos por turno en el orden que llegaron a la clínica.
#b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
#atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
#que se ingrese -1 como número de afiliado.


def load_pacientes(pacientes):
    # este carga pacientes hasta que se ingresa -1
    afiliado = int(input("Ingrese número de afiliado (-1 para finalizar): "))

    while afiliado != -1:
        tipo = int(input("Ingrese 0 para urgencia o 1 para turno: "))

        pacientes.append([afiliado, tipo])

        afiliado = int(input("Ingrese número de afiliado (-1 para finalizar): "))


def show_pacientes(pacientes):
    # este otro muestra los pacientes separados según el tipo de atención
    print("\nPacientes atendidos por urgencia:")
    for paciente in pacientes:
        if paciente[1] == 0:
            print(paciente[0])

    print("\nPacientes atendidos por turno:")
    for paciente in pacientes:
        if paciente[1] == 1:
            print(paciente[0])


def search_afiliado(pacientes):
    # este cuenta las atenciones por turno y por urgencia del afiliado buscado
    afiliado = int(input("\nIngrese número de afiliado a buscar (-1 para finalizar): "))

    while afiliado != -1:
        # Reinicia los contadores para cada nuevo afiliado
        turnos = 0
        urgencias = 0

        for paciente in pacientes:
            if paciente[0] == afiliado:
                if paciente[1] == 0:
                    urgencias += 1
                else:
                    turnos += 1

        print("Atendido por turno:", turnos)
        print("Atendido por urgencia:", urgencias)

        afiliado = int(input("\n Ingrese número de afiliado a buscar (-1 para finalizar): "))


pacientes = []

load_pacientes(pacientes)
show_pacientes(pacientes)
search_afiliado(pacientes)