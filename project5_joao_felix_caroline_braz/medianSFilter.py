import statistics
from math import floor
import numpy as np
from Projetos_PDI.project5_joao_felix_caroline_braz.imagePad4e import imagePad4e

def medianSFilter(f , w):

    #dimensão da imagem
    M, N = f.shape[0], f.shape[1]
    #tamanho da vizinhança
    size_mask = (floor(w / 2))
    #replicamento de pad com a vizinhança
    pad = imagePad4e(f, size_mask, size_mask, 'replicate')
    #criação de um novo array de zeros com a mesma forma e tipo de dados da imagem
    filtered_image = np.zeros_like(f, dtype=np.float32)
    for rows in range(M):
        for columns in range(N):
            #posicionamento do pixel com a vizinhança
            pad_img = pad[rows:rows + w, columns:columns + w]
            #transforma em um array unidimensional
            img_uni = pad_img.ravel()
            #converte para uma lista
            List = list(img_uni)
            #organiza os elementos da lista
            List.sort()
            #calcula a mediana da lista
            median = statistics.median(List)
            #resultado da mediana para o pixel
            filtered_image[rows, columns] = median
    return filtered_image