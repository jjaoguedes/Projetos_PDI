import numpy as np
from PIL import Image

def bilinearInterp(f, x, y):

  # Obter o tamanho da imagem original
  m, n = f.shape

  # Arredondar para baixo as coordenadas x e y
  xi = int(np.floor(x))
  yi = int(np.floor(y))

  # Ajustar xi e yi para evitar índices fora da imagem
  if xi <= 0:
    xi = 1
  if yi <= 0:
    yi = 1

  if xi + 1 > m:
    xi = m - 1
  if yi + 1 > n:
    yi = n - 1

  # Obter os índices dos quatro pontos vizinhos
  xi1 = xi + 1
  yi1 = yi + 1

  # Formar a matriz A do sistema linear
  A = np.array([
    [1, xi, yi, xi * yi],
    [1, xi1, yi, xi1 * yi],
    [1, xi, yi1, xi * yi1],
    [1, xi1, yi1, xi1 * yi1]
  ])

  # Formar o vetor B do sistema linear
  B = np.array([f[xi, yi], f[xi1, yi], f[xi, yi1], f[xi1, yi1]])

  # Resolver o sistema linear AX = B
  X = np.linalg.solve(A, B)

  # Calcular o valor interpolado
  p = X[0] + X[1] * x + X[2] * y + X[3] * x * y

  return p

def imageResize(f, numrows, numcols):

    height, width = f.shape[0], f.shape[1]

    if height > width:

        #cálculo do fator de redução ou expanção, caso a altura seja maior que a largura

        #cx e cy são fatores de escala
        cx = numrows/height
        cy = cx

        #tx e ty são fatores de translação
        cols = round(cy * width)
        tx = 0
        ty = (numcols - cols) / 2
    else:
        #cálculo do fator de redução ou expanção, caso a largura seja maior que a altura

        cy = numcols / width
        cx = cy

        rows = round(cx * height)
        ty = 0
        tx = (numrows - rows) / 2

    image_white = np.ones((numrows, numcols)) * 255
    g = Image.fromarray(image_white.astype('uint8'))

    #matriz de transformação da escala
    As =  np.array([
    [cx, 0, 0],
    [0, cy, 0],
    [0, 0, 1]])

    #matriz de transformação de translação
    At = np.array([
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]])

    #translação e reescala
    A = As * At

    invA = np.linalg.inv(A)
    for xl in range(numrows):
        for yl in range(numcols):
            # Transformações
            a = np.linalg.inv(invA) * np.array([[xl], [yl], [1]])
            x = a[0]
            y = a[1]

            # Interpolação bilinear com retorno da intensidade do pixel pelo mapeamento inverso
            if 0 < x <= height and 0 < y <= width:
                g[xl - 1, yl - 1] = bilinearInterp(f, x, y)

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
#img.show()

g = imageResize(image_matrix_original, 700,700)
#transforms the matrix to an image object
s = Image.fromarray(g)
s.show()