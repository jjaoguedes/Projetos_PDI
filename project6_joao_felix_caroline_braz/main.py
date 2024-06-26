import numpy as np
from PIL import Image

def globalThresh(f, detT):

    imagem_norm = f/255
    T = np.mean(imagem_norm)

    # Inicializa as variáveis para as médias dos grupos
    m1 = 0
    m2 = 0

    # Loop principal da iteração
    while True:
    # Segmentação de pixels com base no limiar atual
        g = np.where(imagem_norm > T, 255, 0)

        # Cálculo das médias dos grupos G1 e G2
        if m1 == 0:
            m1 = np.mean(imagem_norm[g == 255])
            m2 = np.mean(imagem_norm[g == 0])
        else:
            m1_novo = np.mean(imagem_norm[g == 255])
            m2_novo = np.mean(imagem_norm[g == 0])
            m1 = 0.5 * (m1 + m1_novo)
            m2 = 0.5 * (m2 + m2_novo)
    # Cálculo do novo valor de limiar
        T_novo = 0.5 * (m1 + m2)

        # Verificação da convergência
        if np.abs(T_novo - T) < detT:
            break
        # Atualização do limiar para a próxima iteração
        T = T_novo
    return g


name_image = 'rice-shaded'
#open the image using module PIL
f = Image.open(name_image + '.tif')

#get the original DPI of the image
dpi_original = f.info.get('dpi')

#converts the image for gray scale
f_gray = f.convert('L')

#converts grayscale image to a Numpy matrix
image_matrix = np.asarray(f_gray)

#copy image original
image_matrix_original = image_matrix.copy()
#transforms the matrix to an image object
img = Image.fromarray(image_matrix_original)
img.show()

g = globalThresh(image_matrix_original,0.01)
#transforms the matrix to an image object
s = Image.fromarray(g)
s.show()

#sets the target DPI to the original DPI value
dpi_target = dpi_original

#saves the resulting image with the mean-filtered image
#s.save(name_image + '.tif', optimize=False, dpi=dpi_target)