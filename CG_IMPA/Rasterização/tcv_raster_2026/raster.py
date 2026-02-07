import argparse
import importlib
from itertools import product

import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

def main(args):
    xmin, xmax, ymin, ymax = args.window
    width, height = args.resolution

    # create tensor for image: RGB
    image = np.zeros((height, width, 3))

    # Find coordinates for each pixel
    x_coords = [xmin + (xmax - xmin) * (i + 0.5) / width for i in range(width)]
    y_coords = [ymin + (ymax - ymin) * (j + 0.5) / height for j in range(height)]

    # load scene from file args.scene
    scene = importlib.import_module(args.scene).Scene()


    # for each pixel, determine if it is inside any primitive in the scene
    # use cartesian product for efficiency
    for j, i in tqdm(product(range(height), range(width)), total=height*width):
        point = (x_coords[i], y_coords[j])
        # set background color
        image[j, i] = list(scene.background.as_list())
        # if point is inside any primitive, set pixel color to that primitive's color
        for primitive, color in scene:
            inside = primitive.in_out(point)
            if inside:
                # Simple shading: use the red channel as intensity
                image[j, i] = [color.r, color.g, color.b]
                break  # Stop at the first primitive that contains the point

    # save image as png using matplotlib
    plt.imsave(args.output, image, vmin=0, vmax=1, origin='lower')

if __name__ == "__main__":
    '''
    parser = argparse.ArgumentParser(description="Raster module main function")
    parser.add_argument('-s', '--scene', type=str, help='Scene name', default='mickey_scene')
    parser.add_argument('-w', '--window', type=float, nargs=4, help='Window: xmin xmax ymin ymax', default=[0, 8.0, 0, 6.0])
    parser.add_argument('-r', '--resolution', type=int, nargs=2, help='Resolution: width height', default=[800, 600])
    parser.add_argument('-o', '--output', type=str, help='Output file name', default='output.png')
    args = parser.parse_args()

    main(args)
    '''

    #=================================================
    #Atividade 1
    #=================================================

    #Criar varias cenas com um triângulo
    '''
    for i in range(1,14):
        parser = argparse.ArgumentParser(description="Raster module main function")
        parser.add_argument('-s', '--scene', type=str, help='Scene name', default='triangle_scene')      
        parser.add_argument('-w', '--window', type=float, nargs=4, help='Window: xmin xmax ymin ymax', default=[0, 4, 0, 4])
        parser.add_argument('-r', '--resolution', type=int, nargs=2, help='Resolution: width height', default=[2**i, 2**i])
        parser.add_argument('-o', '--output', type=str, help='Output file name', default=f'images/triangle{2**i}x{2**i}.png')
        args = parser.parse_args()

        main(args)
    '''

    #Criar varias cenas com dois triângulos
    '''
    for i in range(1,14):
        parser = argparse.ArgumentParser(description="Raster module main function")
        parser.add_argument('-s', '--scene', type=str, help='Scene name', default='triangle_scene')      
        parser.add_argument('-w', '--window', type=float, nargs=4, help='Window: xmin xmax ymin ymax', default=[0, 5, 0, 5])
        parser.add_argument('-r', '--resolution', type=int, nargs=2, help='Resolution: width height', default=[2**i, 2**i])
        parser.add_argument('-o', '--output', type=str, help='Output file name', default=f'images/two_triangle_separate{2**i}x{2**i}.png')
        args = parser.parse_args()

        main(args)
    '''

    #=================================================
    #Atividade 2
    #=================================================
    '''
    for i in range(1,14):
        parser = argparse.ArgumentParser(description="Raster module main function")
        parser.add_argument('-s', '--scene', type=str, help='Scene name', default='function_scene')
        parser.add_argument('-w', '--window', type=float, nargs=4, help='Window: xmin xmax ymin ymax', default=[-2.5, 2.5, -2, 3])
        parser.add_argument('-r', '--resolution', type=int, nargs=2, help='Resolution: width height', default=[2**i, 2**i])
        parser.add_argument('-o', '--output', type=str, help='Output file name', default=f'images/function{2**i}x{2**i}.png')
        args = parser.parse_args()

        main(args)
        '''