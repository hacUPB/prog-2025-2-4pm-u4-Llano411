# Tupla vacía
coordenada = () # no tiene sentido usarla vacia porque las tuplas son inmutables

# Tupla con elementos
coordenada = (33.9425, -118.4081)  # LAX (Aeropuerto de Los Ángeles)

# Tupla con un solo elemento (requiere coma al final)
rumbo = (270,)  # Sin la coma sería tratado como un entero entre paréntesis

# Tupla sin paréntesis (empaquetado implícito)
avion_info = "Boeing 787", "Dreamliner", 2009, 242

# Indexación (similar a las listas)
print(coordenada[0])  # 33.9425
print(avion_info[-1])  # 242 (pasajeros)

# Slicing
print(avion_info[0:2])  # ("Boeing 787", "Dreamliner")

# Desempaquetado de tuplas
fabricante, modelo, año, capacidad = avion_info
print(f"El {fabricante} {modelo} se lanzó en {año}")

# Desempaquetado
lat, lon = coordenada
print(f"Latitud: {lat}, Longitud: {lon}")

lista_de_tuplas = [(0,0), (3,5), (8,3)]
print(lista_de_tuplas)
lista_de_tuplas.append((45,6))
lista_de_tuplas[0] = (1,1)
print(lista_de_tuplas) # si se puede cambiar porque estamos cambiando 1 elemento de una lista el (0,0) desaparece y se añade el (1,1)

Tupla_de_listas = ([2,4,3], [9,6,12])
Tupla_de_listas [1][0] = 18
print(Tupla_de_listas)

numeros = (2, 34, 54, 12, 4)

if 12 in numeros: #se usa para comprobar que un elemento esta en una tupla
    print("El 12 esta en la tupla")
else: 
    print("El 12 no esta en la tupla")