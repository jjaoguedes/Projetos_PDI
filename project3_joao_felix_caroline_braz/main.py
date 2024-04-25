import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from project3_joao_felix_caroline_braz.histEqual4e import histEqual4e
from project3_joao_felix_caroline_braz.imagehist4e import imagehist4e


name_image = 'spillway-dark'
#name_image = 'rose1024'
#name_image = 'hidden-horse'

# Abre a imagem usando PIL
f = Image.open(name_image + '.tif')
# Obtém o DPI original da imagem
dpi_original = f.info.get('dpi')
# Converte a imagem para escala de cinza
f_gray = f.convert('L')
# Converte a imagem em escala de cinza para uma matriz Numpy
image_matrix = np.asarray(f_gray)

g_histograma = imagehist4e(image_matrix, 'n')
#plota o grafico do histograma
plt.xlabel("Valor de Intensidade")
plt.ylabel("Frequência")
plt.title("Histograma da Imagem")
plt.bar(range(len(g_histograma)), g_histograma)
plt.savefig(name_image + '_Histograma' + '.png')
plt.show()

g_equalizada = histEqual4e(g_histograma)
#plota o grafico histograma equalizado
plt.xlabel("Valor de Intensidade")
plt.ylabel("Frequência")
plt.title("Histograma da Imagem equalizado")
plt.bar(range(len(g_equalizada)), g_equalizada)
plt.savefig(name_image + '_Histograma_Equalizado' +'.png')
plt.show()

#imagem original
image_matrix_original = image_matrix.copy()

#aplicação dos novos valores na imagem original
for i in range(image_matrix.shape[0]):
    for j in range(image_matrix.shape[1]):
        image_matrix_original[i][j] = g_equalizada[image_matrix_original[i][j]]

# Transforma a matriz resultante de volta em um objeto de imagem
s = Image.fromarray(image_matrix_original)

# Define o DPI alvo como o valor original do DPI
dpi_target = dpi_original

# Salva a imagem resultante com a imagem equalizada
s.save(name_image + '_equalizada.tif', optimize=False, dpi=dpi_target)
