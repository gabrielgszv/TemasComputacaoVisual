from PIL import Image

#Função para criar GIF com varias imagens
def criar_gif(
    lista_imagens,
    saida="animacao.gif",
    tamanho=(512, 384),
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


#GIF com function filtro box
'''
lista_functionbox = []

for i in range(1,12):
    lista_functionbox.append(f'images/filter/function/function_box{2**i}x{2**i}.png')


criar_gif(lista_functionbox, saida='function_box.gif')

'''
#GIF com function filtro hat
'''
lista_functionhat = []

for i in range(1,12):
    lista_functionhat.append(f'images/filter/function/function_hat{2**i}x{2**i}.png')


criar_gif(lista_functionhat, saida='function_hat.gif')

'''
#GIF com lion filtro box

lista_liongaussian = []

for i in range(1,8):
    lista_liongaussian.append(f'images/filter/leao/lion_box{4*(2**i)}x{3*(2**i)}.png')


for i in range(8,12):
    lista_liongaussian.append(f'images/filter/leao/lion_box{4*(2**7)}x{3*(2**7)}.png')

criar_gif(lista_liongaussian, saida='lion_box.gif')


#GIF com lion filtro hat

lista_liongaussian = []

for i in range(1,7):
    lista_liongaussian.append(f'images/filter/leao/lion_hat{4*(2**i)}x{3*(2**i)}.png')


for i in range(7,12):
    lista_liongaussian.append(f'images/filter/leao/lion_hat{4*(2**6)}x{3*(2**6)}.png')

criar_gif(lista_liongaussian, saida='lion_hat.gif')
'''

lista_functiongaussian = []

for i in range(1,10):
    lista_functiongaussian.append(f'images/filter/function/function_gaussian{(2**i)}x{(2**i)}.png')


for i in range(10,12):
    lista_functiongaussian.append(f'images/filter/function/function_gaussian{(2**9)}x{(2**9)}.png')

criar_gif(lista_functiongaussian, saida='function_gaussian.gif')
'''


lista_liongaussian = []

for i in range(1,7):
    lista_liongaussian.append(f'images/filter/leao/lion_box{4*(2**i)}x{3*(2**i)}.png')


for i in range(7,12):
    lista_liongaussian.append(f'images/filter/leao/lion_gaussian{4*(2**6)}x{3*(2**6)}.png')

criar_gif(lista_liongaussian, saida='lion_gaussian.gif')
