import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('bola1.csv', sep=';')

df1=df.apply(pd.value_counts)
print(df1)

# Plotando gráficos de frequência para cada bola


def contar_numero_em_dataframe(dataframe, numero):
    """Conta quantas vezes o número especificado aparece em um DataFrame do Pandas."""
    return (dataframe == numero).sum().sum()

quantidades = []
for n in range(1, 26):
    quantidade = contar_numero_em_dataframe(df, n)
    quantidades.append(quantidade)
    print(f"O número {n} aparece {quantidade} vezes.")

quantidades_series = pd.Series(quantidades)
labels1 = quantidades_series.value_counts().index
indices = range(1, 26)  # Índice de 1 a 25 para o gráfico

# Exemplo de gráfico de barras
plt.bar(indices, quantidades)
plt.xlabel('Número')
plt.ylabel('Frequência')
plt.title('Frequência de cada número de 1 a 25')
plt.xticks(indices)
plt.show()

print(labels1)