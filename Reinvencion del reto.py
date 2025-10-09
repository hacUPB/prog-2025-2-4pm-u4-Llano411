configuracion = {
        "initCG": 22.5,
        "uprLMT": 25,
        "lwrLMT": 20
    }
opciones_cg = [
        ("ALAS", -0.3),
        ("FUSELAJE CENTRAL", 0.5)
    ]
mensajes = {
        "input_flt": "Ingrese la duración del vuelo (horas): ",
        "iteracion": "Iteración actual: ",
        "menu_opciones": "Seleccione la sección de tanques de combustible a consumir:\n 1. ALAS\n 2. FUSELAJE CENTRAL\n",
        "menu_info": "**¡IMPORTANTE! RANGO DE CG SEGURO: entre ",
        "alerta_estabilidad": "¡ALERTA! ESTABILIDAD CRITICA. MODIFIQUE EL CENTRO DE GRAVEDAD INMEDIATAMENTE",
        "aterrizaje_seguro": "¡Aterrizaje seguro! CG actual: ",
        "aterrizaje_peligroso": "¡ATERRIZAJE PELIGROSO! CG actual: ",
        "historial_cg": "Historial de CG durante el vuelo: ",
        "error_vuelo": "El tiempo de vuelo ingresado no es válido."
    }
def fuelsim():
    # 1) Diccionario para la configuración
    
    
    # 2) Lista de tuplas para las opciones del menú
    

    # 4) Diccionario para centralizar los mensajes (adaptado para f-strings)
    

    flt = int(input(mensajes["input_flt"]))
    currentCG = configuracion["initCG"]
    
    # 3) Almacenar el historial de CG en una lista
    cg_history = [currentCG]
    
    i = 1
    while i <= flt and 0 < flt < 20:
        print(f'{mensajes["iteracion"]}{i}')
        
        menu_completo = (
            f'{mensajes["menu_opciones"]}'
            f'{mensajes["menu_info"]}{configuracion["lwrLMT"]}% y {configuracion["uprLMT"]}% \n'
            f' CG actual: {currentCG:0.2f}\n SU SELECCION: '
        )
        opcion_tanque = int(input(menu_completo))
        
        if opcion_tanque == 1:
            currentCG += opciones_cg[0][1]
        elif opcion_tanque == 2:
            currentCG += opciones_cg[1][1]
        
        cg_history.append(currentCG)
        
        if configuracion["uprLMT"] < currentCG < configuracion["lwrLMT"]:
            print(mensajes["alerta_estabilidad"])
        i += 1

    if configuracion["lwrLMT"] < currentCG < configuracion["uprLMT"] and 0 < flt < 20:
       print(f'{mensajes["aterrizaje_seguro"]}{currentCG:0.2f}')
       for a in cg_history:
        print(f'{mensajes["historial_cg"]}{a:0.2f}')
        #print(f'{mensajes["historial_cg"]}{cg_history}')
    elif currentCG < configuracion["lwrLMT"] or currentCG > configuracion["uprLMT"]:
       print(f'{mensajes["aterrizaje_peligroso"]}{currentCG:0.2f}')
       for a in cg_history:
        print(f'{mensajes["historial_cg"]}{a:0.2f}') 
        #print(f'{mensajes["historial_cg"]}{cg_history}')
    
    if flt >= 20 or flt <= 0:
       print(mensajes["error_vuelo"])
           
    return currentCG

def diccionarios():
    print("Diccionario de configuracion:")
    for b, v in configuracion.items():
        print(b,v)
    print("Diccionario de mensajes")
    for c, w in mensajes.items():
        print(f"{c}: \t\t{w}")

def listas():
    for z,x in enumerate(opciones_cg):
        print(f"{z+1}-{x[0]}: {x[1]}")

while True:
    choice = int(input("**¡Bienvenido!** Escoja una de las opciones a continuación:\n1. Simulador de Gestión del Centro de Gravedad\n2. Diccionarios\n3. listas\n4. Salir\n SU SELECCION: "))
    match choice:
        case 1:
            fuelsim()
        case 2:
            diccionarios()
        case 3:
            listas()
        case 4: 
            break
        case _:
            print("valor ingresado invalido")