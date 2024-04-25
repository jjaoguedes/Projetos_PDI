import numpy as np

def imagehist4e(f, modo):

    #inicializa o histograma
    histograma = np.zeros(256)

    numero_total_pixels = f.shape[0] * f.shape[1]
    #conta quantas vezes cada valor de intensidade aparece na imagem
    for row in f:
        for column in row:
            histograma[column] = histograma[column] + 1

    #Normaliza o histograma, se necessário
    #cálculo probabilístico da divisão de quantas vezes o valor apareceu pelo número total de pixels na imagem
    histograma_normalizado = []
    if modo == 'n':
        for k in range(256):
            valor_normalizado = histograma[k]/numero_total_pixels
            histograma_normalizado.append(valor_normalizado)
        return histograma_normalizado
    if modo == 'u':
        return np.array(histograma)
