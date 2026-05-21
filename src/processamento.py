#from PIL import Image, ImageFont, ImageDraw

#image = Image.new ('RGB', (10,10), color = 'white')

#draw = ImageDraw.Draw(image)

#draw.text((1,-2), "P", fill="black", font_size=11)

import cv2
import matplotlib.pyplot as plt
import numpy as np

def processar_imagem(caminho):

    #ler img
    img = cv2.imread(caminho)

    #converte para cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    #binarizacao
    _, binaria = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY_INV
    )

    #redimesiona
    redimensionada = cv2.resize(binaria, (20,20))


    #tras 255 em 1 e 0 em -1
    #redimensionada = redimensionada // 255
    #redimensionada = ( redimensionada ).astype(int)

    #redimensionada[
    #    redimensionada == 0
    #] = -1

    # transforma:
    # preto -> 1
    # branco -> -1
    redimensionada = np.where(
        redimensionada > 0,
        1,
        -1
    )

    # mostra imagem
    plt.imshow(
        redimensionada,
        cmap="gray"
    )

    plt.title(
        "Imagem Processada"
    )

    plt.show()

    return redimensionada


   # plt.imshow(redimensionada, cmap="gray")

    #plt.title("Imagem Processada")

    #plt.show()

    #return redimensionada

    