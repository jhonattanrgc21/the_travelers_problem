import itertools

def calcular_distancia(ruta, distancias):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        distancia_total += distancias[ciudad1][ciudad2]
    distancia_total += distancias[ruta[-1]][ruta[0]]  
    return distancia_total

def encontrar_ruta_mas_corta(distancias):
    ciudades = list(distancias.keys())
    distancia_mas_corta = float('inf')
    ruta_mas_corta = None

    for perm in itertools.permutations(ciudades):
        distancia = calcular_distancia(perm, distancias)
        if distancia < distancia_mas_corta:
            distancia_mas_corta = distancia
            ruta_mas_corta = perm

    return ruta_mas_corta, distancia_mas_corta


def main():
    distancias = {
        "Caracas": {"Barcelona": 127, "Valencia": 98, "Ciudad Bolívar": 398},
        "Ciudad Bolívar": {"Caracas": 398, "Valencia": 476, "Barcelona": 285},
        "Valencia": {"Caracas": 98, "Barcelona": 215, "Ciudad Bolívar": 476},
        "Barcelona": {"Caracas": 127, "Ciudad Bolívar": 285, "Valencia": 215}
    }
    ruta_mas_corta, distancia_mas_corta = encontrar_ruta_mas_corta(distancias)
    print("Ruta más corta:", ruta_mas_corta)
    print("Distancia:", distancia_mas_corta)

if __name__ == "__main__":
    main()