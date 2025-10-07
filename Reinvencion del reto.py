def CG(opt, CG):  #Reemplazar "constantes" con un Diccionario
            if opt == 1:
                        CG = CG - 0.3
            elif opt == 2:
                        CG = CG + 0.5
            return CG

def fuelsim(): #Almacenar la Configuración en un Diccionario
            #initCG = 22.5
            uprLMT = 25
            lwrLMT = 20
            #chgWING = -0.3
            #chgCTR = 0.5
            flt = int(input("Ingrese la duración del vuelo (horas): "))
            currentCG = 22.5
            i = 0
            while i <= flt and flt < 20 and flt > 0: #Usar una Lista de Tuplas para las Opciones del Menú
                        print(f"Iteración actual: {i}")
                        opcion_tanque = 0
                        opcion_tanque = int(input(f"Seleccione la sección de tanques de combustible a consumir:\n 1. ALAS\n 2. FUSELAJE CENTRAL\n **¡IMPORTANTE! RANGO DE CG SEGURO: entre 20% y 25%\n CG actual: {currentCG}\n SU SELECCION: ")) 
                        if opcion_tanque == 1:
                                    currentCG = CG(opcion_tanque, currentCG)
                        elif opcion_tanque == 2:
                                    currentCG = CG(opcion_tanque, currentCG)
                        if uprLMT < currentCG :
                                    print("¡ALERTA! ESTABILIDAD CRITICA. MODIFIQUE EL CENTRO DE GRAVEDAD INMEDIATAMENTE")
                        i += 1
            if lwrLMT < currentCG < uprLMT and flt < 20 and flt > 0:
                        print(f"¡Aterrizaje seguro! CG actual: {currentCG}")
            elif currentCG < lwrLMT or currentCG > uprLMT:
                        print(f"¡ATERRIZAJE PELIGROSO! CG actual: {currentCG}")
            if flt > 20 or flt < 0:
                   print("El tiempo de vuelo ingresado no es válido.")
            return currentCG