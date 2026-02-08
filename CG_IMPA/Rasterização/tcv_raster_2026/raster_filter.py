import argparse
import importlib
from itertools import product

import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

#==========================================
#Filtros
#==========================================

def box_filter(d):
    return 1.0

def hat_filter(d):
    return max(0.0, 1.0-d)

def gaussian_filter(d, sigma=0.5):
    return np.exp(-(d**2)/(2*(sigma**2)))

#==========================================
#Rasterizador
#==========================================

def main(args):
    xmin, xmax, ymin, ymax = args.window
    width, height = args.resolution

    # create tensor for image: RGB
    image = np.zeros((height, width, 3))

    #Tamanho do pixel
    dx = (xmax-xmin)/width
    dy = (ymax-ymin)/height

    #Número de amostras por eixo
    n = int(np.sqrt(args.samples))

    #Escolha do filtro
    if args.filter == 'box':
        filter = box_filter
    elif args.filter == 'hat':
        filter = hat_filter
    elif args.filter == 'gaussian':
        filter = gaussian_filter

    # load scene from file args.scene
    scene = importlib.import_module(args.scene).Scene()


    # for each pixel, determine if it is inside any primitive in the scene
    # use cartesian product for efficiency
    for j, i in tqdm(product(range(height), range(width)), total=height*width):
        
        cor = np.zeros(3)
        peso = 0.0

        #Centro do pixel
        cx = xmin + (i + 0.5) * dx
        cy = ymin + (j + 0.5) * dy
        
        #Amostragem
        for sy in range(n):
            for sx in range(n):
                u = (sx + 0.5)/n
                v = (sy + 0.5)/n

                #Ponto amostra
                x = xmin + (i+u)*dx
                y = ymin + (j+v)*dy

                #Distancia do ponto amostra ao centro
                d = np.sqrt((x-cx)**2 + (y-cy)**2) / (0.5 * np.sqrt(dx*dx + dy*dy))
                w = filter(d)

                sample_color = np.array(scene.background.as_list())

                for primitive, color in scene:
                    if primitive.in_out((x, y)):
                        sample_color = np.array([color.r, color.g, color.b])
                        break

                cor += w*sample_color
                peso += w

        image[j, i] = cor / peso

    # save image as png using matplotlib
    plt.imsave(args.output, image, vmin=0, vmax=1, origin='lower')

if __name__ == "__main__":

    #=================================================
    #Atividade 3
    #=================================================

    #Função com filtro box e 16 amostras
    '''
    for i in range(1,12):
        parser = argparse.ArgumentParser(description="Raster module main function")
        parser.add_argument('-s', '--scene', type=str, help='Scene name', default='function_scene')
        parser.add_argument('-w', '--window', type=float, nargs=4, help='Window: xmin xmax ymin ymax', default=[-2.5, 2.5, -2, 3])
        parser.add_argument('-r', '--resolution', type=int, nargs=2, help='Resolution: width height', default=[2**i, 2**i])
        parser.add_argument('-o', '--output', type=str, help='Output file name', default=f'images/filter/function/function_box{2**i}x{2**i}.png')
        #Parametros do filtro
        parser.add_argument('--samples', type=int, default=16)
        parser.add_argument('--filter', type=str, default='box')

        args = parser.parse_args()

        main(args)
    '''
    #Função com filtro hat e 16 amostras
    '''
    for i in range(1,12):
        parser = argparse.ArgumentParser(description="Raster module main function")
        parser.add_argument('-s', '--scene', type=str, help='Scene name', default='function_scene')
        parser.add_argument('-w', '--window', type=float, nargs=4, help='Window: xmin xmax ymin ymax', default=[-2.5, 2.5, -2, 3])
        parser.add_argument('-r', '--resolution', type=int, nargs=2, help='Resolution: width height', default=[2**i, 2**i])
        parser.add_argument('-o', '--output', type=str, help='Output file name', default=f'images/filter/function/function_hat{2**i}x{2**i}.png')
        #Parametros do filtro
        parser.add_argument('--samples', type=int, default=16)
        parser.add_argument('--filter', type=str, default='hat')

        args = parser.parse_args()

        main(args)
    '''

    #Leão com filtro box e 16 amostras
    '''
    for i in range(1,12):
        parser = argparse.ArgumentParser(description="Raster module main function")
        parser.add_argument('-s', '--scene', type=str, help='Scene name', default='lion_scene')      
        parser.add_argument('-w', '--window', type=float, nargs=4, help='Window: xmin xmax ymin ymax', default=[-300, 500, -100, 500])
        parser.add_argument('-r', '--resolution', type=int, nargs=2, help='Resolution: width height', default=[4*(2**i), 3*(2**i)])
        parser.add_argument('-o', '--output', type=str, help='Output file name', default=f'images/filter/leao/lion_box{4*(2**i)}x{3*(2**i)}.png')

        #Parametros do filtro
        parser.add_argument('--samples', type=int, default=16)
        parser.add_argument('--filter', type=str, default='box')

        args = parser.parse_args()

        main(args)
    '''

    #Leão com filtro hat e 16 amostras

    '''
    for i in range(1,12):
        parser = argparse.ArgumentParser(description="Raster module main function")
        parser.add_argument('-s', '--scene', type=str, help='Scene name', default='lion_scene')      
        parser.add_argument('-w', '--window', type=float, nargs=4, help='Window: xmin xmax ymin ymax', default=[-300, 500, -100, 500])
        parser.add_argument('-r', '--resolution', type=int, nargs=2, help='Resolution: width height', default=[4*(2**i), 3*(2**i)])
        parser.add_argument('-o', '--output', type=str, help='Output file name', default=f'images/filter/leao/lion_hat{4*(2**i)}x{3*(2**i)}.png')

        #Parametros do filtro
        parser.add_argument('--samples', type=int, default=16)
        parser.add_argument('--filter', type=str, default='hat')

        args = parser.parse_args()

        main(args)
    '''

    #==================================
    #Desafio
    #==================================
    
    #Fractal de Mandelbrot

    parser = argparse.ArgumentParser(description="Raster module main function")
    parser.add_argument('-s', '--scene', type=str, default='mandelbrot_scene')    
    parser.add_argument('-w', '--window', type=float, nargs=4, default=[-2.5, 1.5, -2.0, 2.0])
    parser.add_argument('-r', '--resolution', type=int, nargs=2, default=[8192, 8192])
    parser.add_argument('-o', '--output', type=str, default=f'images/mandelbrotgaussian8192x8192.png')
    #Parametros do filtro
    parser.add_argument('--samples', type=int, default=16)
    parser.add_argument('--filter', type=str, default='gaussian')

    args = parser.parse_args()

    main(args)