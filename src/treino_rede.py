import string
import numpy as np

from src.extracao import carregar_dataset
from src.adaline import Adaline


def treinar_redes():

    # carrega dataset
    X, y, infos = carregar_dataset()

    # dicionário de redes
    redes = {}

    # percorre letras
    for letra in string.ascii_uppercase:

        print()
        print("-----------------")

        print(f"Treinando neurônio {letra}")

        print("------------------")

        # saída desejada
        y_treino = np.where(
            y == letra,
            1,
            -1
        )

        # cria rede
        rede = Adaline(
            taxa=0.001,
            epocas=10
        )

        # treina
        rede.treinar(
            X,
            y_treino
        )

        # salva rede
        redes[letra] = rede

    print()
    print("Treinamendo da rede Concluída")
    print()

    return redes