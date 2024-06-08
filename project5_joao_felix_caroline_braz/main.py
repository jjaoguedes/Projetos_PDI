import numpy as np
from PIL import Image
from Projetos_PDI.project5_joao_felix_caroline_braz.medianSFilter import medianSFilter
from Projetos_PDI.project5_joao_felix_caroline_braz.twodSFilter import twodSFilter

name_image = 'Fig3.37(a)'
#open the image using module PIL
f = Image.open(name_image + '.jpg')

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

#the neighborhood size
w = 3

#Linear Filtering - Mean filter
g1 = twodSFilter(image_matrix_original, w)
#transforms the resulting array back into an image object
img_filter_media = Image.fromarray(g1)
img_filter_media.show()
#sets the target DPI to the original DPI value
dpi_target = dpi_original
#saves the resulting image with the mean-filtered image
img_filter_media.save(name_image + '_img_filter_media_' + str(w) + 'x' + str(w) + '.jpg', optimize=False, dpi=dpi_target)

if w == 3:
    #Non-Linear Filtering - Median Filter
    g2 = medianSFilter(image_matrix_original, w)
    #transforms the resulting array back into an image object
    img_filter_median = Image.fromarray(g2)
    img_filter_median.show()
    #define the target DPI to the original DPI value
    dpi_target = dpi_original
    #saves the resulting image with the mean-filtered image
    img_filter_median.save(name_image + '_img_filter_median_' + str(w) + 'x' + str(w) + '.jpg', optimize=False, dpi=dpi_target)
