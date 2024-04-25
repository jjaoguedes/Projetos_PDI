def pixVal4e(f, r, c):

  if 0 <= r < len(f) and 0 <= c < len(f[0]): #verifica se a linha e coluna estão dentro dos limites da imagem.
    return f[r][c] #valor do pixel
  else:
    return None