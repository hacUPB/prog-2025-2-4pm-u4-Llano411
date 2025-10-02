def analizar_trayectoria(rumbo_planeado, rumbo_real, umbral_desviacion=5):
    """
    Identifica puntos en la trayectoria donde el avión se desvió
    significativamente del rumbo planeado.

    Args:
        rumbo_planeado: Lista de ángulos planeados (grados)
        rumbo_real: Lista de ángulos reales seguidos (grados)
        umbral_desviacion: Desviación máxima permitida en grados

    Returns:
        Lista de índices donde la desviación superó el umbral
    """
    
    puntos_con_desviacion = []
    
    
    for i in range(len(rumbo_planeado)):
        
        diferencia = rumbo_planeado[i] - rumbo_real[i]
        
        
        if diferencia < 0:
            desviacion = -diferencia  
        else:
            desviacion = diferencia   
        
        
        if desviacion >= umbral_desviacion:
            
            puntos_con_desviacion.append(i)
            
    
    return puntos_con_desviacion

# Datos de prueba
planeado = [45, 45, 45, 90, 90, 90, 180, 180, 225, 225, 270]
real = [43, 47, 48, 86, 91, 95, 183, 176, 222, 230, 265]

# Probando la función
desviaciones = analizar_trayectoria(planeado, real, 5)
print(f"Se detectaron desviaciones significativas en los puntos(indices): {desviaciones}")