import cv2
from cursorValues4e import cursorValues4e
from pixVal4e import pixVal4e

def calcular_nivel_medio_cinza(f, r, c):
  soma_pixels = 0
  for linha in f:
    for pixel in linha:
      soma_pixels += pixel #calcula a soma de todos os valores dos pixels

  total_pixels = r * c #calcula o número total de pixels
  nivel_medio_cinza = soma_pixels / total_pixels #calcula a média dos valores dos pixels
  return nivel_medio_cinza

f = cv2.imread('girl.jpg', cv2.IMREAD_GRAYSCALE)

v_origin = pixVal4e(f,1,1)
print('Valor do pixel na origem da imagem: {}'.format(v_origin))

v_middle = pixVal4e(f, 300, 269)
print('Valor do pixel no meio da imagem: {}'.format(v_middle))

tupla = cursorValues4e(f)
print('r = {}\nc = {}\nv = {}'.format(tupla[0], tupla[1], tupla[2]))

largura, altura = f.shape #obtém o tamanho da imagem
print('A dimensão da imagem é {}x{}'.format(altura, largura))

nivel_medio = calcular_nivel_medio_cinza(f, largura, altura)
print('O nível médio de cinza é {:.2f}'.format(nivel_medio))

profundidade_bits = f.dtype.itemsize * 8
print('A profundidade de bits é {}'.format(profundidade_bits))

cv2.imwrite('imagem_salva.tif', f)
print('Imagem salva no formato tif!')
