componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]
# Indexación (comienza en 0)
print(componentes[0])  # "alas"
print(componentes[-1])  # "tren de aterrizaje" (indexación negativa)

# Slicing (rebanado): Sirven para hacer sublistas a partir de ciertos rangos 
print(componentes[1:3])  # ["fuselaje", "motores"]
print(componentes[:2])   # ["alas", "fuselaje"]
print(componentes[2:])   # ["motores", "tren de aterrizaje"]