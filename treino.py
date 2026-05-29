import string
import numpy as np

from src.extracao import carregar_dataset
from src.adaline import Adaline


# carrega dataset
X, y, infos = carregar_dataset()


# dicionário neurônios
redes = {}


# percorre letras A-Z
for letra in string.ascii_uppercase:

    print()
    print("-----------------")
    print(f"Treinando neurônio {letra}")
    print("------------------")
    print()

    # cria saídas desejadas
    y_treino = np.where(
        y == letra,
        1,
        -1
    )

    # cria neurônio
    rede = Adaline(
        taxa=0.001,
        epocas=1000
    )

    # treina rede
    rede.treinar(
        X,
        y_treino
    )

    # salva rede
    redes[letra] = rede


print()
print("treino finalizado")
print()

print()

print("Quantidade de redes treinadas:")
print(len(redes))

print()

print("Letras treinadas:")
print(redes.keys())