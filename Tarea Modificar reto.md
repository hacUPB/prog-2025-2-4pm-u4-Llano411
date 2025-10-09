# Ejercicio elegido: Centro de gravedad

``` python
def fuelsim():
    # 1) Diccionario para la configuración
    configuracion = {
        "initCG": 22.5,
        "uprLMT": 25,
        "lwrLMT": 20
    }
    
    # 2) Lista de tuplas para las opciones del menú
    opciones_cg = [
        ("ALAS", -0.3),
        ("FUSELAJE CENTRAL", 0.5)
    ]

    # 4) Diccionario para centralizar los mensajes (adaptado para f-strings)
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

    flt = int(input(mensajes["input_flt"]))
    currentCG = configuracion["initCG"]
    
    # 3) Almacenar el historial de CG en una lista
    cg_history = [currentCG]
    
    i = 0
    while i <= flt and 0 < flt < 20:
        print(f'{mensajes["iteracion"]}{i}')
        
        menu_completo = (
            f'{mensajes["menu_opciones"]}'
            f'{mensajes["menu_info"]}{configuracion["lwrLMT"]}% y {configuracion["uprLMT"]}% \n'
            f' CG actual: {currentCG}\n SU SELECCION: '
        )
        opcion_tanque = int(input(menu_completo))
        
        if opcion_tanque == 1:
            currentCG += opciones_cg[0][1]
        elif opcion_tanque == 2:
            currentCG += opciones_cg[1][1]
        
        cg_history.append(currentCG)
        
        if configuracion["uprLMT"] < currentCG:
            print(mensajes["alerta_estabilidad"])
        i += 1

    if configuracion["lwrLMT"] < currentCG < configuracion["uprLMT"] and 0 < flt < 20:
        print(f'{mensajes["aterrizaje_seguro"]}{currentCG}')
        print(f'{mensajes["historial_cg"]}{cg_history}')
    elif currentCG < configuracion["lwrLMT"] or currentCG > configuracion["uprLMT"]:
        print(f'{mensajes["aterrizaje_peligroso"]}{currentCG}')
        print(f'{mensajes["historial_cg"]}{cg_history}')
    
    if flt >= 20 or flt <= 0:
           print(mensajes["error_vuelo"])
           
    return currentCG
```
## Mejoras sugeridas:

1) Hacer un diccionario para las constantes: Agrupar todas las constantes en un diccionario llamado "constantes" para mejorar la legibilidad y facilitar futuras modificaciones.

2) Usar una lista de tuplas para las opciones del menú: Crear una lista de tuplas que contenga las opciones del menú y sus respectivos cambios en el centro de gravedad. Esto permitirá iterar sobre las opciones y reducir la redundancia en el código.

3) Almacenar el historial de CG en una lista: Guardar los valores del centro de gravedad en cada iteración del vuelo en una lista. Esto permitiría visualizar la evolución del CG a lo largo del tiempo

4) Centralizar los mensajes en un diccionario: Agrupar todos los mensajes de texto que se muestran al usuario (alertas, menús, estados) en un diccionario.

