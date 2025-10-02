def cargar_cajas(pesos, peso_maximo):
    """
    Selecciona cajas para cargar en la aeronave sin exceder el peso máximo.

    Args:
        pesos: lista de pesos de las cajas (kg)
        peso_maximo: peso máximo permitido (kg)
    """
    
    pesos.sort()
       
    cajas_cargadas = []
    peso_actual = 0
    
    for peso_caja in pesos:
        if (peso_actual + peso_caja) <= peso_maximo: 
            cajas_cargadas.append(peso_caja)
            peso_actual += peso_caja
            
    print("--- Resultado de la Carga ---")
    print(f"Cajas disponibles (ordenadas): {pesos}")
    print(f"Límite de peso: {peso_maximo} kg")
    print(f"Cajas cargadas: {cajas_cargadas}")
    print(f"Número de cajas cargadas: {len(cajas_cargadas)}")
    print(f"Peso total cargado: {peso_actual} kg")
    
    return cajas_cargadas

# Datos de prueba
pesos_cajas = [120, 400, 300, 180, 450, 200]
peso_max_avion = 1000

cargar_cajas(pesos_cajas, peso_max_avion)