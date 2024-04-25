import cv2  # Biblioteca OpenCV para processamento de imagens
import numpy as np  # Biblioteca NumPy para manipulação de arrays
from PIL import Image  # Biblioteca PIL para manipulação de imagens


# Função para reduzir a intensidade da imagem
def reduce_intensity(image, intensity_level):
    # Calcula o valor de desnormalização com base no nível de intensidade
    value_denormalized = 255 / intensity_level

    # Reduz o nível de intensidade da imagem, convertendo para tipo de dado np.uint8
    image_reduced_level = np.uint8(np.floor(np.double(image) / value_denormalized))

    # Normaliza a imagem reduzida para o intervalo de 0 a 255
    image_normalized = cv2.normalize(image_reduced_level, None, 0, 255, norm_type=cv2.NORM_MINMAX)

    return image_normalized


# Abre a imagem usando PIL
r = Image.open('drip-bottle-256.tif')

# Converte a imagem para escala de cinza
image_gray = r.convert('L')

# Obtém o DPI original da imagem
dpi_original = r.info.get('dpi')

# Converte a imagem em escala de cinza para uma matriz Numpy
image_matrix = np.asarray(image_gray)

# Itera sobre os valores de k de 1 a 7 (total de 8 níveis de intensidade)
for k in range(8):
    intensity_level = 2 ** k  # Calcula o nível de intensidade como 2 elevado a k

    # Chama a função de redução de intensidade e recebe a imagem normalizada
    matrix_result = reduce_intensity(image_matrix, intensity_level)

    # Transforma a matriz resultante de volta em um objeto de imagem
    s = Image.fromarray(matrix_result)

    # Define o DPI alvo como o valor original do DPI
    dpi_target = dpi_original

    # Salva a imagem resultante com o nível de intensidade ajustado
    s.save('drip-bottle-' + str(intensity_level) + '.tif', optimize=False, dpi=dpi_target)
