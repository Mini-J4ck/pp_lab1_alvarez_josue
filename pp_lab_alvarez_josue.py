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
    3 - Guardar en archivo CSV
    4 - Buscar un jugador y mostrar sus logros
    5 - Calcular promedio de puntos ordenados alfabeticamente
    6 - Verificar si el jugador pertenece al salon de la fama
    7 - Mostrat al jugador con la mayor cantidad de rebotes totales
    8 - Mostrar el jugador con el mayor porcentaje de tiros de campo
    9 - Mostrar el jugador con la mayor cantidad de asistencias totales
    10 - Mostrar los jugadores que han promediado más puntos por partido
    11 - Mostrar los jugadores que han promediado más rebotes por partido
    12 - Mostrar los jugadores que han promediado más asistencias por partido
    13 - Mostrar el jugador con la mayor cantidad de robos totales
    14 - Mostrar el jugador con la mayor cantidad de bloqueos totales
    15 - Mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior 
    16 - Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido
    17 - Mostrar el jugador con la mayor cantidad de logros obtenidos
    18 - Mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior
    19 - Mostrar el jugador con la mayor cantidad de temporadas jugadas
    20 - Mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior
    24 - salir
    """)
#----------------------------------------------------------------
def validar_opcion_menu_principal() -> str | int:
    """
    imprime el menu, pide un caracter y lo valida en un rango de 1 a 20 (incluye el 24 para salir)
    no recibe nada
    retorna el caracter convertido a entero si es valido, sino el valor -1
    """
    imprimir_menu_opciones()
    valor_ingresado = input("ingrese una opcion: ")
    if re.match(r"^(1?[0-9]|20|24)$", valor_ingresado):
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
            case 4:
                mostrar_logros_jugador(lista_jugadores)
            case 5:
                mostrar_promedio_puntos_jugadores(lista_jugadores)
            case 6:
                revisar_jugador_salon_fama(lista_jugadores)    
            case 7:
                mostrar_jugador__mayor_key(lista_jugadores, "rebotes_totales")
            case 8:
                mostrar_jugador__mayor_key(lista_jugadores, "porcentaje_tiros_de_campo")
            case 9:
                mostrar_jugador__mayor_key(lista_jugadores, "asistencias_totales")
            case 10:
                jugadores_superioes_promedio_key(lista_jugadores, "promedio_puntos_por_partido")
            case 11:
                jugadores_superioes_promedio_key(lista_jugadores, "promedio_rebotes_por_partido")
            case 12:
                jugadores_superioes_promedio_key(lista_jugadores, "promedio_asistencias_por_partido") 
            case 13:
                mostrar_jugador__mayor_key(lista_jugadores, "robos_totales")
            case 14:
                mostrar_jugador__mayor_key(lista_jugadores, "bloqueos_totales")
            case 15:
                jugadores_superioes_promedio_key(lista_jugadores, "porcentaje_tiros_libres")
            case 16:
                promedio_puntos_partido_sin_menor(lista_jugadores, "promedio_puntos_por_partido")
            case 17:
                buscar_mostrar_jugador_mayor_logros(lista_jugadores)
            case 18:
                jugadores_superioes_promedio_key(lista_jugadores, "porcentaje_tiros_triples")
            case 19:
                mostrar_jugador__mayor_key(lista_jugadores, "temporadas")
            case 20:
                ordenar_jugadores_posicion_superiores(lista_jugadores, "porcentaje_tiros_de_campo")
            case 24:
                print("hasta pronto")
                break
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
def validar_ingreso_numero(valor_ingreso:str) -> int:
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
        id_ingresado = (validar_ingreso_numero(input("ingrese el ID de un jugador: ")))
        while id_ingresado >= len(lista):
            id_ingresado = (validar_ingreso_numero(input("valor incorrecto, ingrese un numero valido: ")))    
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
            print("se creo el archivo datos_jugador_{0}.csv".format(estadisticas_jugador["nombre"]))
            return True
#----------------------------------------------------------------

#PUNTO 4
def validar_ingreso_palabras(cadena_ingreso:str) -> str:
    """
    revisa que la cadena ingresada sea solo letras si no lo es pide al usuario
    recibe un string
    retorna una cadena que cumpla con ser solo letras 
    """
    while True:
        if re.match(r"^[a-zA-Z]+$", cadena_ingreso):
            return cadena_ingreso
        else:
            cadena_ingreso = input("ingrese un nombre: ")
#----------------------------------------------------------------
def buscar_jugador_nombre(jugadores:list[dict]) -> list:
    """
    le pide al usuario un nombre y si coinciden agrega el diccionario del jugador a una lista
    recibe una lista de jugadores
    retorna una lista con los jugadores que contengan el dato ingresado
    """
    nombre_ing = validar_ingreso_palabras(input("ingrese un nombre: "))
    nombre_ing = re.compile(nombre_ing, re.IGNORECASE)
    lista_aux = []
    bandera = False
    for i in jugadores:
        if re.search(nombre_ing, i["nombre"]):
            lista_aux.append(i)
            bandera = True
    if bandera == False:
        return 0
    else:
        return lista_aux
#----------------------------------------------------------------
def mostrar_logros_jugador(jugadores:list) -> None:
    """
    muestra los logros de los jugadores encontrados (si los hay)
    recibe una lista de jugadores
    no retorna nada solo imprime 
    """
    if len(jugadores) == 0:
        print("Lista Vacia")
    else:
        lista_encontrados = buscar_jugador_nombre(jugadores)
        if lista_encontrados == 0:
            print("No existe un jugador con el valor ingresado")
        else:
            for i in lista_encontrados:
                print("Nombre: {0}".format(i["nombre"]))
                print("Logros: \n{0}\n".format("\n".join(i["logros"])))
#----------------------------------------------------------------

#PUNTO 5
def ordenar_segun_key(lista_jugadores:list, key_buscar:str) -> list:
    """
    ordena la lista de jugadores segun la clave que puede ser el nombre o alguna estadistica
    recibe una lista con los jugadores y un string para la clave a ordenar
    retorna una lista ordenada
    """
    if len(lista_jugadores) <= 1:
        return lista_jugadores
    else:
        jugadores = lista_jugadores[:]
        lista_iz = []
        lista_der = []
        pivot = jugadores[0]
        for jugador in jugadores[1:]:
            if (key_buscar == "nombre" or key_buscar == "posicion") and jugador[key_buscar] <= pivot[key_buscar] \
                  or  (key_buscar != "nombre" and key_buscar != "posicion") and jugador["estadisticas"][key_buscar] <= pivot["estadisticas"][key_buscar]:           
                lista_iz.append(jugador)
            else:
                lista_der.append(jugador)
        lista_iz = ordenar_segun_key(lista_iz, key_buscar)
        lista_iz.append(pivot)
        lista_der = ordenar_segun_key(lista_der, key_buscar)
        lista_iz.extend(lista_der)
        return lista_iz
#----------------------------------------------------------------
def mostrar_promedio_puntos_jugadores(jugadores:list) -> None:
    """
    Usando la lista ordenada alfabeticamente muestra el promedio de puntos de cada jugador
    y al final saca el promedio de puntos de todo el equipo
    Recibe la lista de jugadores
    No retorna nada solo imprime el promedio
    """
    if len(jugadores) == 0:
        print("Lista Vacia")
    else:
        lista_jugadores = ordenar_segun_key(jugadores, "nombre")
        acumulador = 0
        for i in lista_jugadores:
            print("Nombre: {0}, Promedio puntos por partido: {1}".format(i["nombre"], i["estadisticas"]["promedio_puntos_por_partido"]))
            acumulador += i["estadisticas"]["promedio_puntos_por_partido"]
            promedio = acumulador / len(jugadores)
        print("El promedio de puntos por partido del equipo es: {0}".format(promedio))
#----------------------------------------------------------------

#PUNTO 6
def revisar_jugador_salon_fama(jugadores:list) -> None:
    """
    busca en los logros de el o los jugadores si pertenecen al salon de la fama
    recibe una lista de jugadores
    no retorna nada
    """
    if len(jugadores) == 0:
        print("Lista Vacia")
    else:
        lista_encontrados = buscar_jugador_nombre(jugadores)
        logro = "Miembro del Salon de la Fama del Baloncesto"
        for jugador in lista_encontrados:
            
            if re.search(r"^"+  re.escape(logro) +"$", jugador["logros"][-1]):
                print("El jugador {0} es {1}".format(jugador["nombre"], logro))
            else:
                print("El jugador {0} no es {1}".format(jugador["nombre"], logro))
#----------------------------------------------------------------

#PUNTOS 7 , 8 , 9 , 13, 14, 19
def buscar_mayor_jugador_clave(jugadores:list, key_buscar:str) -> dict:
    """
    busca al jugador mayor jugador segun la clave
    recibe la lista de jugadores y un string para la clave a ordenar
    retorna el diccionario del jugador mayor
    """
    if len(jugadores) == 0:
        print("Lista Vacia")
    else:
        lista_ord = ordenar_segun_key(jugadores, key_buscar)
        lista_aux = []
        valor_mayor = lista_ord[-1]
        lista_aux.append(valor_mayor)
        for i in lista_ord[:-1]:
            if i["estadisticas"][key_buscar] == valor_mayor["estadisticas"][key_buscar]:
                lista_aux.append(i)
        return lista_aux
#----------------------------------------------------------------

def mostrar_jugador__mayor_key(jugadores:list, key_buscar:str) -> None:
    """
    Con el o los jugadore encontrados muestra los datos de la clave
    Recibe una lista y un string para la clave
    No retorna nada solo imprime un mensaje
    """
    if len(jugadores) == 0:
        print("Lista Vacia")
    else:
        jugadores_encontrados = buscar_mayor_jugador_clave(jugadores, key_buscar)
        for jugador in jugadores_encontrados:
            print("Nombre: {0}, {1}: {2}".format(jugador["nombre"],key_buscar, jugador["estadisticas"][key_buscar]))
#----------------------------------------------------------------

#PUNTO 10, 11, 12, 15, 18 
def jugadores_superioes_promedio_key(jugadores:list, key_buscar:str) -> None:
    """
    pide al usuario un valor y muestra a los jugadores que superen ese valor
    recibe una lista con los datos de los jugadores y un string para la clave a ordenar
    no retorna nada solo imprime mensajes
    """
    if len(jugadores) == 0: 
        print("Lista Vacia")
    else:
        dato_ingresado = (validar_ingreso_numero(input("ingrese el valor a superar: ")))
        print("los jugadores que superan {0} son:\n".format(dato_ingresado))
        bandera = False
        for jugador in jugadores:
            if jugador["estadisticas"][key_buscar] > dato_ingresado:
                print("Nombre: {0}, {1}: {2}".format(jugador["nombre"], key_buscar, jugador["estadisticas"][key_buscar]))
                bandera = True
        if bandera == False:
            print("Nadie supera el valor ingresado")
#----------------------------------------------------------------

 #PUNTO 16
def promedio_puntos_partido_sin_menor(jugadores:list, key_buscar:str) -> None:
    """
    saca el promedio de puntos excluyendo al jugador que tenga menos puntos
    recibe una lista con los datos de los jugadores y un string para la clave a ordenar
    no retorna nada solo imprime mensajes
    """
    if len(jugadores) == 0:
        print("Lista Vacia")
    else:
        lista_encontrados = ordenar_segun_key(jugadores, key_buscar)
        jugador_excluido = lista_encontrados[0]
        acumulador = 0
        for jugador in lista_encontrados[1:]:
            acumulador += jugador["estadisticas"][key_buscar]
        promedio = acumulador / len(lista_encontrados[1:])
        print("el {0} es: {1} excluyendo al jugador {2}".format(key_buscar, promedio, jugador_excluido["nombre"]))
#----------------------------------------------------------------

#PUNTO 17
def buscar_mostrar_jugador_mayor_logros(jugadores:list) -> None:
    """
    busca el jugador con la mayor cantidad de logros obtenidos
    recibe una lista con los jugadores
    no retorna nada solo imprime un mensaje
    """
    if len(jugadores) == 0:
        print("Lista Vacia")
    else:
        for jugador in range(len(jugadores)-1):
            if len(jugadores[jugador]["logros"]) > len(jugadores[jugador + 1]["logros"]):
                jugadores[jugador], jugadores[jugador + 1] =  jugadores[jugador + 1], jugadores[jugador]
        print("El jugador con mayor cantidad de logros es: {0} con {1} logros obtenidos"
            .format(jugadores[-1]["nombre"], len(jugadores[-1]["logros"])))
#----------------------------------------------------------------

#20
def ordenar_jugadores_posicion_superiores(jugadores:list, key_buscar:str) -> None:
    """
    Pide al usuario un valor y muestra los jugadores que lo superen ordenados segun su posicion
    recibe una lista con los datos de los jugadores y un string para la clave a ordenar
    no retorna nada solo imprime mensajes
    """
    if len(jugadores) == 0:
        print("Lista Vacia")
    else:
        lista_encontrados = ordenar_segun_key(jugadores, "posicion")
        dato_ingresado = (validar_ingreso_numero(input("ingrese el valor a superar: ")))
        print("los jugadores que superan {0} son:\n".format(dato_ingresado))
        bandera = False
        for jugador in lista_encontrados:
            if jugador["estadisticas"][key_buscar] > dato_ingresado:
                print("Nombre: {0}, Posicion: {1}, {2}: {3}".format(jugador["nombre"],jugador["posicion"], key_buscar, jugador["estadisticas"][key_buscar]))
                bandera = True
        if bandera == False:
            print("Nadie supera el valor ingresado")
#----------------------------------------------------------------

lista_jugadores = leer_archivo("dt.json")
menu_principal(lista_jugadores)