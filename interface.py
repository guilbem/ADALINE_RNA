import tkinter as tk

from tkinter import filedialog

import pickle
import shutil

from src.processamento import processar_imagem



#carrega modelo treinado
with open(
    "modelos/rede_adaline.pkl",
    "rb"
) as arquivo:

    redes = pickle.load(
        arquivo
    )


def reconhecer_imagem():

    print("Botão clicado")


    # selecionar imagem
    caminho = filedialog.askopenfilename(

        title="Selecionar imagem",

        filetypes=[
            ("Imagens", "*.png *.jpg *.jpeg")
        ]
    )


    # se cancelar
    if not caminho:

        print("Nenhuma imagem selecionada")

        return


    print("Imagem escolhida:")
    print(caminho)


    # copia imagem temporaria
    # evita erro com acentos
    shutil.copy(
        caminho,
        "temp.png"
    )

    caminho = "temp.png"


    # processa imagem
    matriz = processar_imagem(
        caminho
    )


    # vetoriza
    vetor = matriz.flatten()


    ativacoes = {}


    # percorre redes
    for letra, rede in redes.items():

        saida = rede.ativacao(
            vetor
        )

        ativacoes[letra] = saida

        print(
            f"{letra}: {saida}"
        )


    # pega maior ativação
    letra_reconhecida = max(
        ativacoes,
        key=ativacoes.get
    )


    # pega valor ativacao
    maior_ativacao = ativacoes[
        letra_reconhecida
    ]


    # calcula confianca
    soma = sum(

        abs(valor)

        for valor in ativacoes.values()
    )

    confianca = (

        abs(maior_ativacao) / soma

    ) * 100


    print()
    print(
        "Letra Reconhecida pela ADALINE:",
        letra_reconhecida
    )

    print()

    print(
        f"Confiança: "
        f"{confianca:.2f}%"
    )


    # mostra na tela  ametrica 
    resultado_label.config(

        text=(

            f"Letra reconhecida: "
            f"{letra_reconhecida}\n\n"

            f"Ativação: "
            f"{maior_ativacao:.2f}\n\n"

            f"Confiança: "
            f"{confianca:.2f}%"
        )
    )


#janela
janela = tk.Tk()

janela.title(
    "Reconhecimento de Letras - ADALINE"
)

janela.geometry(
    "400x200"
)


titulo = tk.Label(

    janela,

    text=(
        "Reconhecimento de Letras"
    ),

    font=("Arial", 16)
)

titulo.pack(pady=20)


botao = tk.Button(

    janela,

    text="Selecionar Imagem",

    command=reconhecer_imagem,

    font=("Arial", 12)
)

botao.pack(pady=10)


resultado_label = tk.Label(

    janela,

    text="",

    font=("Arial", 14)
)

resultado_label.pack(pady=20)


# inicia interface
janela.mainloop()