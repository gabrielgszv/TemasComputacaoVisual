from PIL import Image

lista_imagens = []

for i in range(1,12):
    lista_imagens.append(f'two_triangle_separate{2**i}x{2**i}.png')

def criar_gif_resolucao_pixelart(
    lista_imagens,
    saida="animacao.gif",
    tamanho=(512, 512),
    duracao=500
):
    """
    Cria GIF ampliando imagens pequenas sem borrar (ideal p/ pixel-art).
    """

    frames = []

    for path in lista_imagens:
        img = Image.open(path).convert("RGB")

        # escala SEM suavização
        img = img.resize(tamanho, Image.Resampling.NEAREST)

        frames.append(img)

    frames[0].save(
        saida,
        save_all=True,
        append_images=frames[1:],
        duration=duracao,
        loop=0
    )

    print(f"GIF criado: {saida}")

criar_gif_resolucao_pixelart(lista_imagens, saida='two_triangle_separate.gif')
