from os import system
lista_trabajador = []
def menu_principal():
    opciones = {
        '1': ('Registrar trabajador', reg_trabajador),
        '2': ('Listar todos los trabajadores', lis_trabajador),
        '3': ('Imprimir planilla de sueldos', imp_trabajador),
        '4': ('Salir del Programa', salir)
    }

    generar_menu(opciones, '4')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def reg_trabajador():
    system("cls")
    nombres = input("Ingrese  nombre  y Apellido del trabajador ")
    cargo   = input("Ingrese el cargo del trabajador ")
    sueldo_bruto = int(input("Ingrese el sueldo bruto del Trabajador "))
    desc_salud =  int(round(sueldo_bruto *  7/100,0))
    desc_afp =  int(round(sueldo_bruto*12/100,0))
    liquido = sueldo_bruto - desc_salud - desc_afp
    lista_trabajador.append({
                    "nombres": nombres,
                    "cargo": cargo,
                    "sueldo_bruto": sueldo_bruto,
                    "desc_salud": desc_salud,
                    "desc_afp": desc_afp,
                    "liquido": liquido,
                })
    print(lista_trabajador)
    input()
    return 


def lis_trabajador():
    print('Has elegido la opción 2')
    system("cls")
    print(f"Nombres\t        Cargo\t   Sueldo_Bruto\t Desc_salud\t Desc_afp\t Liquido\t")
    for trabajador in lista_trabajador:
         print(f"{trabajador['nombres']}\t {trabajador['cargo']}\t   {trabajador['sueldo_bruto']}\t  {trabajador['desc_salud']}\t   {trabajador['desc_afp']}\t  {trabajador['liquido']}\t" )
    input()
    return 


def imp_trabajador():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')


menu_principal()