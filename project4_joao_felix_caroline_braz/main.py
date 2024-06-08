import numpy as np
from PIL import Image
from Projetos_PDI.project4_joao_felix_caroline_braz.imagePad4e import imagePad4e

name_image = 'testpattern1024'
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

padtype = 'replicate'
g = imagePad4e(image_matrix_original,100,100, padtype)
#transforms the matrix to an image object
s = Image.fromarray(g)
s.show()

#sets the target DPI to the original DPI value
dpi_target = dpi_original

#saves the resulting image with the mean-filtered image
s.save(name_image + '_padding_' + padtype + '.tif', optimize=False, dpi=dpi_target)
