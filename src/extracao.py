import os
import string
import numpy as np

from src.processamento import processar_imagem

def carregar_dataset():

    X = []
    y = []

    # percorre letras A-Z
    for letra in string.ascii_uppercase:

        pasta = f"dados/treino/{letra}"

        # percorre imagens da pasta
        for arquivo in os.listdir(pasta):

            caminho = f"{pasta}/{arquivo}"

            # processa imagem
            matriz = processar_imagem(
                caminho
            )

            # transforma em vetor
            vetor = matriz.flatten()

            # salva vetor
            X.append(vetor)

            # salva letra correta
            y.append(letra)

            print(
                "Imagem processada:",
                caminho
            )

    return np.array(X), np.array(y)