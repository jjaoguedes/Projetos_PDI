import numpy as np
from PIL import Image

def globalThresh(f, detT):

    # Convertendo a imagem para uint8
    image = f.astype(np.uint8)

    # Definindo o intervalo inicial para o limiar
    min_valor = np.min(image)
    max_valor = np.max(image)
    T = (min_valor.astype(np.float64) + max_valor.astype(np.float64)) / 2.0

    # Variável para controlar o loop
    finish = False

    while not finish:
        # Criando a imagem binária com o limiar atual
        image_binary = image >= T

        # Calculando a média das intensidades dos pixels brancos e pretos
        mean_white = np.mean(image[image_binary])
        mean_black = np.mean(image[~image_binary])

        # Calculando o novo limiar
        new_T = 0.5 * (mean_white + mean_black)

        # Verificando se o limiar convergiu
        diferency = np.abs(T - new_T)
        finish = diferency < detT

        # Atualizando o limiar
        T = new_T
    # Retornando a imagem binária final
    return image_binary


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
#img.show()

g = globalThresh(image_matrix_original,0.01)
#transforms the matrix to an image object
s = Image.fromarray(g)
s.show()

#sets the target DPI to the original DPI value
dpi_target = dpi_original

#saves the resulting image with the mean-filtered image
s.save(name_image + '_result_globalThresh'+'.tif', optimize=False, dpi=dpi_target)