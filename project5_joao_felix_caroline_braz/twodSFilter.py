from math import floor
import numpy as np
from imagePad4e import imagePad4e

def twodSFilter(f , w):

    #dimensão da imagem
    M, N = f.shape[0], f.shape[1]
    #criação da máscara
    mask = (1 / (w * w) * (np.ones((w, w), dtype=np.int32)))
    # tamanho da vizinhança
    size_mask = (floor(w / 2))
    # replicamento de pad com a vizinhança
    pad = imagePad4e(f, size_mask, size_mask, 'replicate')
    #criação de um novo array de zeros com a mesma forma e tipo de dados da imagem
    filtered_image = np.zeros_like(f, dtype=np.float32)
    for rows in range(M):
        for columns in range(N):
            #posicionamento do pixel com a vizinhança
            pad_img = pad[rows:rows + w, columns:columns + w]
            #obtenção de todos os produtos entre os elementos do filtro com os correspondentes elementos da vizinhança
            product = mask * pad_img
            #resultado do pixel pela soma dos produtos
            filtered_image[rows, columns] = product.sum()

    return filtered_image