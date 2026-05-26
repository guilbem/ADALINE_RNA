import numpy as np

class Adaline:

    # construtor
    def __init__(self, taxa=0.001, epocas=200):

        # taxa aprendizado
        self.taxa = taxa

        # quantidade épocas
        self.epocas = epocas

        # pesos da rede
        self.pesos = None

        # bias
        self.bias = 0


    # função treinamento
    def treinar(self, X, y):

        # quantidade entradas
        entradas = X.shape[1]

        # inicia pesos aleatórios
        self.pesos = np.random.rand(
            entradas
        )

        # loop épocas
        for epoca in range(self.epocas):

            erro_total = 0

            # percorre dataset
            for i in range(len(X)):

                x = X[i]

                alvo = y[i]

                # saída da rede
                saida = self.ativacao(x)

                # calcula erro
                erro = alvo - saida

                # soma erro
                erro_total += erro ** 2

                # atualiza pesos
                self.pesos = (
                    self.pesos
                    +
                    self.taxa
                    *
                    erro
                    *
                    x
                )

                # atualiza bias
                self.bias = (
                    self.bias
                    +
                    self.taxa
                    *
                    erro
                )

            print(
                f"Época {epoca+1} "
                f"Erro: {erro_total}"
            )


    # função ativação
    def ativacao(self, x):

        return np.dot(
            x,
            self.pesos
        ) + self.bias


    # previsão
    def prever(self, x):

        saida = self.ativacao(x)

        # classificação
        if saida >= 0:
            return 1
        else:
            return -1
        