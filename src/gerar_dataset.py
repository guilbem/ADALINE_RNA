from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os
import string

# fontes
fontes = {
    "arial": "arial.ttf",
    "times": "times.ttf"
}

# cria pasta principal
os.makedirs("dados/treino", exist_ok=True)

# percorre letras A-Z
for letra in string.ascii_uppercase:

    # cria pasta da letra
    pasta_letra = f"dados/treino/{letra}"

    os.makedirs(pasta_letra, exist_ok=True)

    # percorre fontes
    for nome_fonte, arquivo_fonte in fontes.items():

        # cria imagem branca
        image = Image.new(
            "RGB",
            (100,100),
            color="white"
        )

        draw = ImageDraw.Draw(image)

        fonte = ImageFont.truetype(
            arquivo_fonte,
            60
        )

        # desenha letra
        draw.text(
            (25,15),
            letra,
            fill="black",
            font=fonte
        )

        # salva imagem
        caminho = (
            f"{pasta_letra}/"
            f"{letra}_{nome_fonte}.png"
        )

        image.save(caminho)

        print("Salvo:", caminho)

print("Dataset criado com sucesso!")