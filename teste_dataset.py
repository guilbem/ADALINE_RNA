from src.extracao import carregar_dataset

X, y = carregar_dataset()

print()
print("Dataset carregado!")

print()

print("Quantidade de imagens:")
print(len(X))

print()

print("Formato do vetor:")
print(X[0].shape)

print()

print("Primeira letra:")
print(y[0])

print()

print("Primeiro vetor:")
print(X[0])