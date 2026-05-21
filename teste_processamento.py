from src.processamento import processar_imagem
#apresenta a letra selecionada binarizada no pronpt, porem todas as outras ja foram binarizadas
matriz = processar_imagem(
    "dados/treino/A/A_arial.png"
)

print(matriz)