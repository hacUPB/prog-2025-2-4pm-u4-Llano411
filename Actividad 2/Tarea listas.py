def analizar_eficiencia(distancias, combustible_consumido):
    """
    Calcula la eficiencia de combustible en km/L para cada tramo del vuelo
    y devuelve estadísticas relevantes.
    """
    
    eficiencias = []
    for i in range(len(distancias)):
        eficiencias.append(distancias[i] / combustible_consumido[i])
    
    
    eficiencia_maxima = max(eficiencias)
    eficiencia_minima = min(eficiencias)
    tramo_mas_eficiente = eficiencias.index(eficiencia_maxima) + 1
    tramo_menos_eficiente = eficiencias.index(eficiencia_minima) + 1
    
    
    eficiencia_promedio = sum(eficiencias) / len(eficiencias)
    
    
    print("=== Análisis de Eficiencia de Combustible ===")
    print(f"Eficiencias por tramo (km/L): {eficiencias}")
    print(f"Tramo más eficiente: {tramo_mas_eficiente} ({eficiencia_maxima:.4f} km/L)")
    print(f"Tramo menos eficiente: {tramo_menos_eficiente} ({eficiencia_minima:.4f} km/L)")
    print(f"Eficiencia promedio: {eficiencia_promedio:.4f} km/L")
    
    return eficiencias

# Datos de prueba
tramos_distancia = [800, 1200, 1000, 750]  # km
tramos_combustible = [2400, 3000, 2800, 2000]  # L

# Probando la función
eficiencias_resultado = analizar_eficiencia(tramos_distancia, tramos_combustible)

