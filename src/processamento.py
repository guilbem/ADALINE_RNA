#from PIL import Image, ImageFont, ImageDraw

#image = Image.new ('RGB', (10,10), color = 'white')

#draw = ImageDraw.Draw(image)

#draw.text((1,-2), "P", fill="black", font_size=11)

import cv2
import matplotlib.pyplot as plt

def processar_imagem(caminho):

    img = cv2.imread(caminho)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, binaria = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
    )

    redimensionada = cv2.resize(binaria, (20,20))

    plt.imshow(redimensionada, cmap="gray")

    plt.title("Imagem Processada")

    plt.show()

    return redimensionada