import json
import re

def imprimir_menu_opciones() -> None:
    """
    imprime la lista de opciones del menu
    no recibe nada
    no retorna nada
    """
    print("""
    1 - Mostrar la lista de todos los jugadores del Dream Team
    2 - Mostrar estadisticas del jugador
    3 - guardar en archivo CSV
    4 - buscar un jugador y mostrar sus logros
    5 - Buscar héroes por inteligencia
    6 - Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente
    7 - salir
    """)
#----------------------------------------------------------------
def validar_opcion_menu_principal() -> str | int:
    """
    imprime el menu, pide un caracter y lo valida en un rango de 1 a 20 (incluye ademas el 23)
    no recibe nada
    retorna el caracter convertido a entero si es valido, sino el valor -1
    """
    imprimir_menu_opciones()
    valor_ingresado = input("ingrese una opcion: ")
    if re.match(r"^(1?[0-9]|20|23)$", valor_ingresado):
        return int(valor_ingresado)
    else:
        return -1
#----------------------------------------------------------------
def menu_principal(lista_jugadores:list) -> None:
    """
    llama a la funcion correspondiente al ingreso
    recibe la lista de heroes
    no retorna nada
    """
    estadisticas_jugador = []
    while True:
        respuesta = validar_opcion_menu_principal()
        match(respuesta):
            case 1:
                listar_jugadores(lista_jugadores, False)
            case 2:
                diccionario = mostrar_estadisticas_jugador(lista_jugadores)
                if diccionario != 0:
                    estadisticas_jugador = diccionario
            case 3:
                print(guardar_estadisticas_jugador(estadisticas_jugador))
                
            case _:
                print("Dato Incorrecto")
        input("\nPulse enter para continuar\n")
#----------------------------------------------------------------
def leer_archivo(nombre_archivo:str) -> list[dict]:
    """
    lee un archivo en modo lectura
    recibe un string
    retorna una lista de diccionarios
    """
    lista_aux = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        dict = json.load(archivo)
        lista_aux = dict["jugadores"]
    return lista_aux
#----------------------------------------------------------------
def validar_ingreso(valor_ingreso:str) -> int:
    """
    revisa que el dato recibido sea solo un numero entero
    recibe un string ingresado por el usuario
    retorna el valor convertido a entero
    """
    while True:
        resultado = re.match(r"^[0-9]+$", valor_ingreso)
        if resultado and valor_ingreso != "":
            valor_ingreso = int(valor_ingreso)
            break
        else:
            valor_ingreso = input("valor incorrecto, ingrese un numero valido: ")        
    return valor_ingreso

#PUNTO 1
def listar_jugadores(lista:list, id_jugador:bool) -> None:
    """
    muestra todos los jugadores y sus posiciones o sus id segun se necesite
    recibe una lista con los jugadores y un boolean para usarlo con el punto 2
    no retorna nada
    """
    if len(lista) == 0:
        print("Error lista vacia")
    else:
        lista_jugadores = lista[:]
        if id_jugador == False:
            for jugador in lista_jugadores:
                print("Nombre: {0}, Posicion: {1}".format(jugador["nombre"], jugador["posicion"]))
        elif id_jugador == True:
            for i in range(len(lista)):
                print("Id:{0} Nombre: {1}".format(i, lista[i]["nombre"]))
#----------------------------------------------------------------

#PUNTO 2
def mostrar_estadisticas_jugador(lista_jugadores:list) -> dict:
    """
    pide al usuario un id y lo busca en la lista y muestra sus estadisticas
    recibe la lista con los jugadores
    devuelve un diccionario con las estadisticas del jugador escogido
    """
    if len(lista_jugadores) == 0:
        print("Lista Vacia")
        return 0
    else:
        lista = lista_jugadores[:]
        listar_jugadores(lista, True)
        id_ingresado = (validar_ingreso(input("ingrese el ID de un jugador: ")))
        while id_ingresado >= len(lista):
            id_ingresado = (validar_ingreso(input("ingrese el ID de un jugador: ")))    
        for i in range(len(lista)):
            if i == id_ingresado: 
                print("Nombre: {0}".format(lista[i]["nombre"]))
                print("Posicion: {0}".format(lista[i]["posicion"]))
                for key, value in lista[i]["estadisticas"].items():                 
                    print("{0}: {1}".format(key, value))            
        return lista[id_ingresado]
#------------------------------------------------------------------

#PUNTO 3
def guardar_estadisticas_jugador(estadisticas_jugador:list) -> bool:
    """
    con los datos encontrado en el punto 2 lo guarda en un archivo .CSV 
    recibe un diccionario con las estadisticas del jugador 
    retorna un boolean para informar al usuario True = exitosa o False = error
    """
    if len(estadisticas_jugador) == 0:
        print("Error debe ingresar al punto 2")
        return False
    else:
        with open("Parcial_op\pp_lab1_alvarez_josue\datos_jugador_{0}.csv"
                  .format(estadisticas_jugador["nombre"]), "w", encoding="utf-8") as archivo:
            lista_elementos = [
                                "nombre\t\t\t", "posición\t", "temporadas\t", "puntos totales\t", "promedio de puntos por partido\t",
                                "rebotes totales\t", "promedio de rebotes por partido\t", "asistencias totales\t",
                                "promedio de asistencias por partido\t", "robos totales\t", "bloqueos totales\t",
                                "porcentaje de tiros de campo\t", "porcentaje de tiros libres\t", "porcentaje de tiros triples\n"
                              ]
            archivo.writelines(",".join(lista_elementos))
            mensaje = "{0}\t,{1}\t,{2}\t\t\t,{3}\t\t\t,{4}\t\t\t\t\t\t\t,{5}\t\t\t\t,{6}\t\t\t\t\t\t\t\t,{7}\t\t\t\t\t,{8}\t\t\t\t\t\t\t\t\t,{9}\t\t\t,{10}\t\t\t\t,{11}\t\t\t\t\t\t\t,{12}\t\t\t\t\t\t,{13}" 
            mensaje = mensaje.format(
                        estadisticas_jugador["nombre"], 
                        estadisticas_jugador["posicion"], 
                        estadisticas_jugador["estadisticas"]["temporadas"],
                        estadisticas_jugador["estadisticas"]["puntos_totales"],
                        estadisticas_jugador["estadisticas"]["promedio_puntos_por_partido"],
                        estadisticas_jugador["estadisticas"]["rebotes_totales"],
                        estadisticas_jugador["estadisticas"]["promedio_rebotes_por_partido"],
                        estadisticas_jugador["estadisticas"]["asistencias_totales"],
                        estadisticas_jugador["estadisticas"]["promedio_asistencias_por_partido"],
                        estadisticas_jugador["estadisticas"]["robos_totales"],
                        estadisticas_jugador["estadisticas"]["bloqueos_totales"],
                        estadisticas_jugador["estadisticas"]["porcentaje_tiros_de_campo"],
                        estadisticas_jugador["estadisticas"]["porcentaje_tiros_libres"],
                        estadisticas_jugador["estadisticas"]["porcentaje_tiros_triples"]
                        )
            archivo.write(mensaje)
            return True
lista_jugadores = leer_archivo("Parcial_op\pp_lab1_alvarez_josue\dt.json")
menu_principal(lista_jugadores)