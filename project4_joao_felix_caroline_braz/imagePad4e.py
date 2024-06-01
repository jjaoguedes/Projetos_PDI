import numpy as np
from PIL import Image

def imagePad4e(f, r, c, padtype):
    #obtém a dimensão da imagem
    height, width = f.shape[0], f.shape[1]

    #calcula a nova altura e largura do pad
    new_height = height + (2 * r)
    new_width = width + (2 * c)

    #cria o vetor de zeros do pad
    f_pad = np.zeros((new_height, new_width), dtype=f.dtype)

    #coloca a imagem original no centro do pad de zeros
    #percorre os pixels para colocar a imagem no centro do pad de zeros
    for row in range(height):
        for column in range(width):
            f_pad[row + r][column + c] = f[row][column]

    if padtype == 'replicate':
        #replica bordas superior e inferior
        for row in range(r):
            for column in range(new_width):
                f_pad[row][column] = f_pad[(2*r)-row-1][column]  # Borda superior
                f_pad[new_height-1-row][column] = f_pad[new_height-(2*r)-1+row][column]  # Borda inferior
        #replica bordas esquerda e direita
        for row in range(new_height):
            for column in range(c):  # loop para linhas (superior e inferior)
                f_pad[row][column] = f_pad[row][(2 * c) - column + 1]  # Borda superior
                f_pad[row][new_width-1-column] = f_pad[row][new_width-(2*c)-1-column]  # Borda inferior
    return f_pad

name_image = 'testpattern1024'
#abre a imagem usando PIL
f = Image.open(name_image + '.tif')

#obtém o DPI original da imagem
dpi_original = f.info.get('dpi')

#converte a imagem para escala de cinza
f_gray = f.convert('L')

#converte a imagem em escala de cinza para uma matriz Numpy
image_matrix = np.asarray(f_gray)

#imagem original
image_matrix_original = image_matrix.copy()
img = Image.fromarray(image_matrix_original)
img.show()
padtype = 'replicate'
g = imagePad4e(image_matrix_original,100,100, padtype)
#transforma a matriz resultante de volta em um objeto de imagem
s = Image.fromarray(g)
s.show()

#define o DPI alvo como o valor original do DPI
dpi_target = dpi_original

#salva a imagem resultante com a imagem equalizada
s.save(name_image + '_padding_' + padtype + '.tif', optimize=False, dpi=dpi_target)

