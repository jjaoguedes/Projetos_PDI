import numpy as np
from PIL import Image
from Projetos_PDI.project5_joao_felix_caroline_braz.medianSFilter import medianSFilter
from Projetos_PDI.project5_joao_felix_caroline_braz.twodSFilter import twodSFilter

name_image = 'Fig3.37(a)'
#abre a imagem usando PIL
f = Image.open(name_image + '.jpg')

#obtém o DPI original da imagem
dpi_original = f.info.get('dpi')

#converte a imagem para escala de cinza
f_gray = f.convert('L')

#converte a imagem em escala de cinza para uma matriz Numpy
image_matrix = np.asarray(f_gray)

#imagem original
image_matrix_original = image_matrix.copy()

#transforma a matriz em um objeto de imagem
img = Image.fromarray(image_matrix_original)
img.show()

#tamanho da vizinhança
w = 3

#Filtragem Linear - filtro de média
g1 = twodSFilter(image_matrix_original, w)
#transforma a matriz resultante de volta em um objeto de imagem
img_filter_media = Image.fromarray(g1)
img_filter_media.show()
# define o DPI alvo como o valor original do DPI
dpi_target = dpi_original
#salva a imagem resultante com a imagem filtrada da media
img_filter_media.save(name_image + 'img_filter_media_' + str(w) + 'x' + str(w) + '.tif', optimize=False, dpi=dpi_target)

if w == 3:
    #Filtragem não Linear - filtro de mediana
    g2 = medianSFilter(image_matrix_original, w)
    #transforma a matriz resultante de volta em um objeto de imagem
    img_filter_median = Image.fromarray(g2)
    img_filter_median.show()
    # define o DPI alvo como o valor original do DPI
    dpi_target = dpi_original
    # salva a imagem resultante com a imagem filtrada da mediana
    img_filter_median.save(name_image + 'img_filter_median_' + str(w) + 'x' + str(w) + '.tif', optimize=False, dpi=dpi_target)
