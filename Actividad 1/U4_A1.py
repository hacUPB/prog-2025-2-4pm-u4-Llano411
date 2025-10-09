# 1: Objetos, variables y etiquetas 
# Creamos un objeto (en este caso, un número)
altitud = 10000  # metros

# 'altitud' es una etiqueta que apunta al objeto entero 10000
# Podemos crear otra etiqueta que apunte al mismo objeto
elevacion = altitud

# Si modificamos el valor al que apunta 'elevacion'
elevacion = 9500

# 'altitud' sigue apuntando al valor original
print(altitud)  # 10000
print(elevacion)  # 9500

# se concluye que los valores de las variables cambian segun el orden en el que esten 

# 2: ID de objetos

velocidad = 800  # km/h
print(id(velocidad))  # Muestra el identificador único del objeto

otra_velocidad = 800
print(id(otra_velocidad))  # Para números pequeños, Python reutiliza objetos

lista1 = [1, 3, 67]
print(id(lista1))

# 3: Mutabilidad
def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"Combustible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]  # Lista (objeto mutable)
agregar_combustible(combustible_actual, 500)
print(combustible_actual)  # [1000, 1200, 800, 500] - La lista original fue modificada 

# En Python, cuando pasas un objeto a una función:

# Si es mutable (listas, diccionarios, etc.), los cambios que hagas dentro de la función también afectan al original.

# Si es inmutable (enteros, strings, tuplas, etc.), los cambios solo se quedan dentro de la función y el original no se modifica.

# 4: Iterables 

# Bucle for 
# Iterando sobre una lista de sensores de aeronave
sensores = ["temperatura", "presión", "velocidad", "altitud", "combustible"]

for sensor in sensores:
    print(f"Comprobando sensor de {sensor}...")

# Bucle while
# Simulando lecturas de altitud cada 10 segundos
altitudes = [0, 100, 500, 1000, 1500, 2000, 2200, 2500]
tiempo = 0
i = 0

while i < len(altitudes):
    print(f"Tiempo: {tiempo}s - Altitud: {altitudes[i]} metros")
    tiempo += 10
    i += 1

# enumerate(): Proporciona índices junto con valores
for i, etapa in enumerate(["despegue", "ascenso", "crucero", "descenso", "aterrizaje"]):
    print(f"Etapa {i+1}: {etapa}")

# zip(): Combina dos o más iterables
tiempos = [0, 10, 20, 30]
velocidades = [0, 200, 300, 320]

for t, v in zip(tiempos, velocidades):
    print(f"Tiempo: {t}s - Velocidad: {v} km/h")