import cv2
import numpy as np


def processar_imagem(caminho):

   #consulta imagem
    imagem = np.fromfile(
        caminho,
        dtype=np.uint8
    )

    img = cv2.imdecode(
        imagem,
        cv2.IMREAD_COLOR
    )

    # verifica erro
    if img is None:

        raise Exception(
            f"Erro ao abrir:\n{caminho}"
        )

   #conversao para cinza
    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

   #binarizacao
    _, binaria = cv2.threshold(

        gray,

        127,

        255,

        cv2.THRESH_BINARY_INV
    )

   #tamanho da imagem
    redimensionada = cv2.resize(

        binaria,

        (20,20)
    )

   #conversao do binario para -1e1, branco=-1  preto=1
    redimensionada = np.where(

        redimensionada > 0, 1, -1
    )

    return redimensionada