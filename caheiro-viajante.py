import itertools

# CIDADE    # DISTANCIA
# TAUBATE   # 43
# SÃO PAULO # 100
# SÃO JOSÉ DOS CAMPOS # 50
# CAMPINAS  # 70
# RIBEIRÃO PRETO # 150


# Definindo as cidades e as distâncias entre elas (matriz de adjacência)
cidades = ['Taubate', 'Sao Paulo', 'Sao Jose dos Campos', 'Campinas', 'Ribeirao Preto']
distancias = [
    [0, 100, 43, 70, 150],   # Taubate
    [100, 0, 50, 70, 150],   # Sao Paulo
    [43, 50, 0, 70, 150],    # Sao Jose dos Campos
    [70, 70, 70, 0, 150],    # Campinas
    [150, 150, 150, 150, 0]  # Ribeirao Preto
]

def calcular_distancia(percurso):
    distancia_total = 0
    for i in range(len(percurso) - 1):
        distancia_total += distancias[percurso[i]][percurso[i+1]]
    # Volta para a cidade inicial
    distancia_total += distancias[percurso[-1]][percurso[0]]
    return distancia_total

# Gerar todas as permutações possíveis (exceto a cidade inicial para evitar ciclos repetidos)
menor_distancia = float('inf')
melhor_percurso = None

for perm in itertools.permutations(range(1, len(cidades))):
    percurso = [0] + list(perm)
    distancia = calcular_distancia(percurso)
    if distancia < menor_distancia:
        menor_distancia = distancia
        melhor_percurso = percurso

# Exibir o melhor percurso e a menor distância
print("Melhor percurso:")
for idx in melhor_percurso:
    print(cidades[idx], end=" -> ")
print(cidades[melhor_percurso[0]])
print(f"Menor distância: {menor_distancia} km")
