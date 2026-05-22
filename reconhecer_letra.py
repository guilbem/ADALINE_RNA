from src.processamento import processar_imagem
from src.treino_rede import treinar_redes


#treina as 26 redes
redes = treinar_redes()


#imagem selecionada para ser reconhecida
imagem_teste = (
    "dados/treino/V/V_arial.png"
)

# processa imagem
matriz = processar_imagem(
    imagem_teste
)

# vetoriza
vetor = matriz.flatten()


# ativações
ativacoes = {}


# calcula saída
for letra, rede in redes.items():

    saida = rede.ativacao(
        vetor
    )

    ativacoes[letra] = saida

    #print(
        #f"{letra} → {saida}"
    #)

    print(
    f"Letra {letra} "
    f"→ ativação: {saida}"
)


# pega maior ativação
resultado = max(
    ativacoes,
    key=ativacoes.get
)

print()
print("Ativacoes completas:")
print(ativacoes)

print()
print("---------------------------------")
print("Letra Reconhecida pela ADALINE:")
print(resultado)
print("----------------------------")


