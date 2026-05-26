import string
import numpy as np
from tqdm import tqdm
import pickle

from src.extracao import carregar_dataset
from src.adaline import Adaline


def treinar_redes():

    # carrega dataset
    X, y, infos = carregar_dataset()

    # dicionário redes
    redes = {}

    # percorre letras
    for letra in tqdm(
        string.ascii_uppercase,
        desc="Treinando neurônios"
    ):

        print()

        print(
            f"Treinando neurônio {letra}"
        )

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
            epocas=200
        )


        # treina rede
        rede.treinar(
            X,
            y_treino
        )


        # salva rede
        redes[letra] = rede


    print()
    print("Treinamento da rede concluído!")
    print()

    return redes


#faz o treinamento
redes = treinar_redes()


#salva modelo
with open(
    "modelos/rede_adaline.pkl",
    "wb"
) as arquivo:

    pickle.dump(
        redes,
        arquivo
    )


print()
print("Modelo salvo com sucesso!")
print()