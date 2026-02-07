from PIL import Image

#Função para criar GIF com varias imagens
def criar_gif(
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


#GIF com um triângulo
lista_triangulo = []

for i in range(1,12):
    lista_triangulo.append(f'triangle{2**i}x{2**i}.png')


criar_gif(lista_triangulo, saida='two_triangle_separate.gif')

#===================================================================================

#GIF com dois triangulos
lista_two_triangle = []

for i in range(1,12):
    lista_two_triangle.append(f'two_triangle{2**i}x{2**i}.png')


criar_gif(lista_two_triangle, saida='two_triangle.gif')

#===================================================================================

#GIF com dois triangulos separados
lista_two_triangle = []

for i in range(1,12):
    lista_two_triangle.append(f'two_triangle_separate{2**i}x{2**i}.png')


criar_gif(lista_two_triangle, saida='two_triangle_separate.gif')

#===================================================================================

#GIF com a função
lista_function = []

for i in range(1,14):
    lista_function.append(f'function{2**i}x{2**i}.png')


criar_gif(lista_function, saida='function.gif')

#===================================================================================