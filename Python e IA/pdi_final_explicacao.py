# -*- coding: utf-8 -*-
"""PDI_Final_Explicacao.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vdPYZYZ5fG8MID85kLlZVN2Li1Lnm4NT
"""

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers

# Dados de exemplo
# Conjunto simples de entradas para o problema lógico AND, onde [0,0], [0,1], [1,0] são falsos (0) e [1,1] é verdadeiro (1).
data = np.array([
    [0, 0], [0, 1], [1, 0], [1, 1]  # Entradas
])
labels = np.array([0, 0, 0, 1])  # Saídas esperadas, onde '0' representa falso e '1' verdadeiro.

# Construção do modelo Perceptron
# Modelo sequencial, onde cada camada é adicionada sequencialmente.
model = keras.Sequential([
    layers.Dense(1, input_dim=2, activation='sigmoid')  # Uma camada densa com 1 neurônio, entrada de 2 dimensões.
    # 'sigmoid' é a função de ativação que mapeia os valores de entrada para a saída entre 0 e 1, útil para classificação binária.
])

# Compilação do modelo
# Especificamos como o modelo deve ser treinado.
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
# 'sgd' - Stochastic Gradient Descent, um método para otimizar a função de perda.
# 'binary_crossentropy' - função de perda para comparação entre a saída prevista e a real, adequada para classificação binária.
# 'accuracy' - métrica para avaliar o desempenho do modelo, medindo a porcentagem de resultados corretos.

# Treinamento do modelo
# Treina o modelo pelos dados fornecidos várias vezes (epochs).
model.fit(data, labels, epochs=10, verbose=1)

# Avaliação do modelo
# Testa o desempenho do modelo nos mesmos dados usados para treinamento.
performance = model.evaluate(data, labels)
print("Perda e Acurácia  do modelo:", performance)

# Coletando os pesos do modelo treinado
# Pesos e bias são parâmetros aprendidos usados para fazer previsões.
weights = model.layers[0].get_weights()[0]
bias = model.layers[0].get_weights()[1]

# Preparando o gráfico
# Cria um gráfico para mostrar os dados e a reta de decisão.
plt.figure(figsize=(6, 6))
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=100, edgecolors='k')
# 'viridis' é um mapa de cores que varia de amarelo a azul, distinto visualmente.
# 's' é o tamanho dos pontos no gráfico.
# 'edgecolors' define a cor da borda dos pontos.

# Calculando e desenhando a reta de separação
# Usa a equação do perceptron para calcular a linha.
x = np.linspace(-0.1, 1.1, 100)
y = (-weights[0][0] * x - bias) / weights[1][0]
plt.plot(x, y, color='red')  # Linha de separação em vermelho, calculada a partir dos pesos.

# Configurações do gráfico
plt.title('Visualização da Separação do Perceptron')
plt.xlabel('Feature 1')  # Nome do eixo X.
plt.ylabel('Feature 2')  # Nome do eixo Y.
plt.xlim(-0.1, 1.1)  # Limites para o eixo X.
plt.ylim(-0.1, 1.1)  # Limites para o eixo Y.
plt.grid(True)  # Adiciona uma grade ao gráfico para melhor visualização.
plt.show()  # Mostra o gráfico.