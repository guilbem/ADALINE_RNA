from PIL import Image, ImageDraw

image = Image.new(
    'RGB',
    (100,100),
    color='white'
)

draw = ImageDraw.Draw(image)

draw.text(
    (30,20),
    "P",
    fill="black"
)

image.save("dados/teste.png")

print("Imagem salva com sucesso!")