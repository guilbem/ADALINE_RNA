from src.extracao import carregar_dataset


# carrega dataset completo
X, y, infos = carregar_dataset()


print()
print("DATASET CARREGADO")
print()


# quantidade imagens
print("Quantidade de imagens:")
print(len(X))

print()


# percorre todos vetores
for i in range(len(X)):

    print("- - - - - - - - - - - - - - - - - - - -  -")

    # mostra letra
    print("Letra:")
    print(y[i])

    print()

    # mostra fonte/arquivo
    print("Arquivo:")
    print(infos[i])

    print()

    # mostra vetor
    print("Vetor:")
    print(X[i])

    print()

    # formato vetor
    print("Formato:")
    print(X[i].shape)

    print("- - - - - - - - - - - - - - - - - - - -  -")
    print()