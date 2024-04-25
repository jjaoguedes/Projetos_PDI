import matplotlib.pyplot as plt
from pixVal4e import pixVal4e

def cursorValues4e(f):
    def onclick(event):  #ocorrência de evento de clique no gráfico.
        global r, c, v
        r, c = int(event.xdata), int(event.ydata) #coordenadas do x(linha) e y(colunas)
        v = pixVal4e(f, r, c) #valor do pixel
        plt.close()

    image, ax = plt.subplots() #cria uma nova imagem e e um objeto de eixos ax
    ax.imshow(f) #exibe a imagem
    image.canvas.mpl_connect('button_press_event', onclick) #conecta a função onclick ao button_press_event da tela da figura.
    plt.show() #exibe a janela do gráfico criada anteriormente.

    if 'r' in globals() and 'c' in globals() and 'v' in globals(): #verifica se as variáveis globais r, c e v foram definidas pela função onclick
        return (r, c, v)
    else:
        return None