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
    21 - Determinar la cantidad de jugadores que hay por cada posición
    22 - Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente
    24 - Determinar qué jugador tiene las mejores estadísticas en cada valor
    26 - salir
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
    if re.match(r"^([0-9]{1,2})$", valor_ingresado):
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
                mostrar_jugador__mayor_menor_key(lista_jugadores, "rebotes_totales", True)
            case 8:
                mostrar_jugador__mayor_menor_key(lista_jugadores, "porcentaje_tiros_de_campo", True)
            case 9:
                mostrar_jugador__mayor_menor_key(lista_jugadores, "asistencias_totales", True)
            case 10:
                jugadores_superioes_promedio_key(lista_jugadores, "promedio_puntos_por_partido")
            case 11:
                jugadores_superioes_promedio_key(lista_jugadores, "promedio_rebotes_por_partido")
            case 12:
                jugadores_superioes_promedio_key(lista_jugadores, "promedio_asistencias_por_partido") 
            case 13:
                mostrar_jugador__mayor_menor_key(lista_jugadores, "robos_totales", True)
            case 14:
                mostrar_jugador__mayor_menor_key(lista_jugadores, "bloqueos_totales", True)
            case 15:
                jugadores_superioes_promedio_key(lista_jugadores, "porcentaje_tiros_libres")
            case 16:
                promedio_puntos_partido_sin_menor(lista_jugadores, "promedio_puntos_por_partido")
            case 17:
                buscar_mostrar_jugador_mayor_logros(lista_jugadores)
            case 18:
                jugadores_superioes_promedio_key(lista_jugadores, "porcentaje_tiros_triples")
            case 19:
                mostrar_jugador__mayor_menor_key(lista_jugadores, "temporadas", True)
            case 20:
                ordenar_jugadores_posicion_superiores(lista_jugadores, "porcentaje_tiros_de_campo")
            case 21:
                mostrar_cantidad_jugadores_posicion(lista_jugadores)
            case 22:
                mostrar_jugadores_cantidad_all_star(lista_jugadores)
            case 23:
                guardar_ranking_csv(lista_jugadores)
            case 24:
                mostrar_jugador_mejor_estadisticas(lista_jugadores)
            case 25:
                mostrar_jugador_maximo(lista_jugadores)
            case 26:
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
        print("Error Error: lista vacia")
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
        print("Error: Lista Vacia")
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
        if re.match(r"^[a-zA-Z]+ ?[a-zA-Z]*$", cadena_ingreso):
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
        print("Error: Lista Vacia")
    else:
        lista_encontrados = buscar_jugador_nombre(jugadores)
        if lista_encontrados == 0:
            print("No existe un jugador con el valor ingresado")
        else:
            for i in lista_encontrados:
                print("-"*30)
                print("Nombre: {0}".format(i["nombre"]))
                print("Logros: \n{0}\n".format("\n".join(i["logros"])))
                print("-"*30)
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
        print("Error: Lista Vacia")
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
        print("Error: Lista Vacia")
    else:
        lista_encontrados = buscar_jugador_nombre(jugadores)
        logro = "Defensor del Año en la NBA en 1988"
        for jugador in lista_encontrados:
            if logro in jugador["logros"]:
                print("El jugador {0} es {1}".format(jugador["nombre"], logro))
            else:
                print("El jugador {0} no es {1}".format(jugador["nombre"], logro))
#----------------------------------------------------------------

#PUNTOS 7 , 8 , 9 , 13, 14, 19
def buscar_mayor_jugador_clave(jugadores:list, key_buscar:str, valor_orden:bool) -> dict:
    """
    busca al jugador mayor jugador segun la clave
    recibe la lista de jugadores, un string para la clave a ordenar y un boolean para el mayor o menor
    retorna el diccionario del jugador mayor
    """
    if len(jugadores) == 0:
        print("Error: Lista Vacia")
    else:
        lista_ord = ordenar_segun_key(jugadores, key_buscar)
        lista_aux = []
        if valor_orden == True:
            valor_mayor_menor = lista_ord[-1]
            lista_ord = lista_ord[:-1]
        else:
            valor_mayor_menor = lista_ord[0]
            lista_ord = lista_ord[1:]
        lista_aux.append(valor_mayor_menor)
        for i in lista_ord:
            if i["estadisticas"][key_buscar] == valor_mayor_menor["estadisticas"][key_buscar]:
                lista_aux.append(i)
        return lista_aux
#----------------------------------------------------------------

def mostrar_jugador__mayor_menor_key(jugadores:list, key_buscar:str, valor_orden:bool) -> None:
    """
    Con el o los jugadore encontrados muestra los datos de la clave
    Recibe una lista y un string para la clave y un boolean para el mayor o menor
    No retorna nada solo imprime un mensaje
    """
    if len(jugadores) == 0:
        print("Error: Lista Vacia")
    else:
        jugadores_encontrados = buscar_mayor_jugador_clave(jugadores, key_buscar, valor_orden)
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
        print("Error: Lista Vacia")
    else:
        dato_ingresado = (validar_ingreso_numero(input("ingrese el valor a comparar: ")))
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
        print("Error: Lista Vacia")
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
        print("Error: Lista Vacia")
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
        print("Error: Lista Vacia")
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

#extras
#21
def cantidad_jugadores_posicion(jugadores:list) -> dict:
    """
    crea un diccionario en el que cuenta los jugadores segun su posicion de juego
    recibe una lista con los datos de los jugadores
    retorna un diccionario con las cantidades de posiciones
    """
    if len(jugadores) == 0:
        print("Error: Lista Vacia")
    else:
        diccionario = {}
        for jugador in jugadores:
            if jugador["posicion"] in diccionario:
                diccionario[jugador["posicion"]] += 1       
            else:
                diccionario[jugador["posicion"]] = 1
        return diccionario
#----------------------------------------------------------------
def mostrar_cantidad_jugadores_posicion(jugadores:list) -> None:
    """
    genera un diccionario con las cantidades de posiciones y lo imprime 
    recibe una lista con los datos de los jugadores
    No retorna nada solo imprime las posiciones
    """
    if len(jugadores) == 0:
        print("Error: Lista Vacia")
    else:
        cantidades_encontradas = cantidad_jugadores_posicion(jugadores)
        print("Cantidad de posiciones en el Team Dream")
        for posicion, valor in cantidades_encontradas.items():
            print("{0}: {1}".format(posicion, valor))
#----------------------------------------------------------------

#22
def jugador_cantidad_all_star(jugador:dict) -> list:
    """
    recorre la lista de logros buscando "[0-9] veces All-Star" 
    recibe un diccionario con los datos del jugador
    retorna el logro All-Star
    """
    bandera = False
    for logro in jugador["logros"]:
        if re.search(r"[0-9]{1,2} veces All-Star", logro):
            valor_encontrado = logro
            bandera = True
            break
    if bandera == False:
        valor_encontrado = "0 veces All-Star"
    return valor_encontrado
#----------------------------------------------------------------
def encontrar_numero(frase:str) -> int:
    """
    esta funcion se encarga de buscar los numeros en un string y los convierte a entero
    recibe un string que es el logro encontrado
    retorna un numero 
    """
    if type(frase) == str:
        valor = re.findall(r"[0-9]+", frase)
        return int("".join(valor))
    else:
        print("No es un string")
        return -1
#----------------------------------------------------------------    

def ordenar_lista_logros(jugadores:list) -> list:
    """
    ordena la lista de jugadores en base a la cantidad de All-Star
    recibe una lista con los jugadores
    retorna una lista ordenada 
    """
    if len(jugadores) <= 1:
        return jugadores
    else:
        lista_i = []
        lista_d = []
        pivot = jugadores[0]
        valor_b = jugador_cantidad_all_star(pivot)
        valor_b = encontrar_numero(valor_b)
        for jugador in jugadores[1:]:
            valor_a = jugador_cantidad_all_star(jugador)
            valor_a = encontrar_numero(valor_a)
            if valor_b < valor_a:
                lista_i.append(jugador)
            else:
                lista_d.append(jugador)
        lista_i = ordenar_lista_logros(lista_i)
        lista_i.append(pivot)
        lista_d = ordenar_lista_logros(lista_d)
        lista_i.extend(lista_d)
        return lista_i
#----------------------------------------------------------------   
def mostrar_jugadores_cantidad_all_star(jugadores:list) -> None:
    """
    recorre la lista ordenada de jugadores para mostrar los nombres y cantidades de all stars
    recibe la lista de jugadores
    no retorna nada solo imprime 
    """
    if len(jugadores) == 0:
        print("Error: Lista Vacia")
    else:
        lista_ord = ordenar_lista_logros(jugadores)
        for i in lista_ord:
            star = jugador_cantidad_all_star(i)
            print("{0} ({1})".format(i["nombre"], star))
#----------------------------------------------------------------

#23
def calcular_rankings_jugadores(jugadores:list) -> list:
    """

    recibe la lista de jugadores
    retorna una lista con las posiciones
    """
    keys_buscar = ["puntos_totales", "rebotes_totales", "asistencias_totales", "robos_totales"]
    lista_aux = []
    for jugador in jugadores:
        lista = []
        for key in keys_buscar:
            lista_or = ordenar_segun_key(jugadores, key)
            lista_or = lista_or[::-1]
            for i in range(len(lista_or)):
                if jugador["nombre"] == lista_or[i]["nombre"]:
                    mensaje = "{0}".format(i+1)
                    lista.append(mensaje)
                    break
        lista_aux.append(lista)
    return lista_aux

def mostrar_ranking(jugadores:list):
    lista_ran = calcular_rankings_jugadores(jugadores)
    lista_aux = []
    for i in range(len(jugadores)):
        mensaje = "{0} {1}".format(jugadores[i]["nombre"], ",".join(lista_ran[i]))
        lista_aux.append(mensaje)
    return lista_aux

def guardar_ranking_csv(jugadores:list):
    if len(jugadores) == 0:
        print("Error Lista Vacia")
    else:
        lista_jugadores = mostrar_ranking(jugadores)
        with open("Parcial_op\pp_lab1_alvarez_josue\\ranking_jugadores.csv", "w", encoding="utf-8") as archivo:
            lista_columnas = ["Jugador","Puntos","Rebotes","Asistencias","Robos\n"]
            archivo.writelines(",".join(lista_columnas))
            archivo.writelines("\n".join(lista_jugadores))
        print("Se creo correctamente el archivo: ranking_jugadores.csv")

#24
def jugador_mejores_caracteristicas(jugadores:list) -> list:
    """
    Usando las claves de estadisticas y la funcion ordenar_segun_key obtiene el mejor jugador de X clave
    para guardarlo en una lista con el formato requerido.
    Recibe una lista de jugadores.
    Retorna una lista con los jugadores Nro 1.
    """
    claves = jugadores[0]["estadisticas"].keys()
    lista_maximos_por_clave = []
    for clave in claves:
        lista_ord = ordenar_segun_key(jugadores, clave)
        jugador_maximo = lista_ord[-1]
        mensaje = "Mayor cantidad de {0}: {1} ({2})".format(
            clave, jugador_maximo["nombre"], jugador_maximo["estadisticas"][clave])
        lista_maximos_por_clave.append(mensaje)
    return lista_maximos_por_clave
#----------------------------------------------------------------
def mostrar_jugador_mejor_estadisticas(jugadores:list) -> None:
    """
    Imprime la lista con los mejores jugadores en cada clave de estadisticas
    recibe la lista de jugadores
    no retorna nada solo imprime
    """
    if len(jugadores) == 0:
        print("Error: Lista Vacia")
    else:
        lista = jugador_mejores_caracteristicas(jugadores)
        for jugador in lista:
            print(jugador)
#----------------------------------------------------------------

#25
def jugador_maximo_caracteristicas(jugadores:list):
    lista_aux = []
    for jugador in jugadores:
        acumulador = 0
        print(jugador["nombre"])
        for valor in jugador["estadisticas"].values():
            acumulador += valor
        print(acumulador)
        lista_aux.append(acumulador)
        print("-"*30)
    return lista_aux
def mostrar_jugador_maximo(jugadores:list):
    if len(jugadores) == 0:
        print("Error Lista Vacia")
    else:
        lita = jugador_maximo_caracteristicas(jugadores)
        for i in range(len(jugadores)-1):
            if lita[i] > lita[i+1]:
                lita[i], lita[i+1] = lita[i+1], lita[i]
                jugadores[i], jugadores[i+1] = jugadores[i+1],jugadores[i]
        print("El jugador con las mejores estadisticas de todos es: {0}".format(jugadores[-1]["nombre"]))

lista_jugadores = leer_archivo("Parcial_op\pp_lab1_alvarez_josue\dt.json")
menu_principal(lista_jugadores)