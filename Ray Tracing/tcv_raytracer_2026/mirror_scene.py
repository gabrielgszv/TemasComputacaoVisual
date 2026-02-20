# defines a scene with a ball using implicit function
import math
from src.base import BaseScene, Color
from src.shapes import Ball, PlaneUV, Cube, Cylinder, ObjectTransform, Surface
from src.camera import Camera
from src.vector3d import Vector3D
from src.light import PointLight, AreaLight
from src.materials import SimpleMaterial, SimpleMaterialWithShadows, TranslucidMaterial, CheckerboardMaterial, MirrorMaterial

from src.functions import *

# class name should be Scene
class Scene(BaseScene):
    def __init__(self):
        super().__init__("Ball Scene")

        # light blue background
        self.background = Color(0.7, 0.8, 1)
        self.ambient_light = Color(0.1, 0.1, 0.1)
        self.max_depth = 10  # for reflections/refractions
        self.camera = Camera(
            eye=Vector3D(0, 0, 2),
            look_at=Vector3D(0, 3, 2),
            up=Vector3D(0, 0, 1),
            fov=30,
            img_width=800,
            img_height=600
        )
        self.lights = [
            # add a point light
            #PointLight(position=Vector3D(0, 1, 1)*10, color=Color(1, 1, 1), intensity=1.6),
            AreaLight(
                position=Vector3D(0, -4, 6),
                look_at=Vector3D(0, 0, 1),
                up=Vector3D(0, 0, 1),
                width=4,
                height=4,
                color=Color(1, 1, 1),
                intensity=2.0
            )
        ]

        blue_material = SimpleMaterial(
            ambient_coefficient=1,
            diffuse_coefficient=0.2,
            diffuse_color=Color(0, 0, 0.5),
            specular_coefficient=0.5,
            specular_color=Color(1, 1, 0),
            specular_shininess=32
        )

        S = [
            [2, 0, 0],
            [0, 0.01, 0],
            [0, 0, 2]
        ]

        # espelho esquerdo
        self.add(
            ObjectTransform(
                Cube(center=Vector3D(0, 3, 1), size=2),
                S
            ),
            MirrorMaterial()
        )

        # espelho direito
        self.add(
            ObjectTransform(
                Cube(center=Vector3D(0, -3, 1), size=2),
                S
            ),
            MirrorMaterial()
        )

        self.add(
            Ball(center=Vector3D(-2.5, 2, 1), radius=1), 
            blue_material
        )
        
        '''
        self.add(
            Cube(center=Vector3D(0, -2, 2), size=1),
            blue_material
        )'''

        # ground plane
        gray_material = CheckerboardMaterial(
            ambient_coefficient=1,
            diffuse_coefficient=0.8,
            square_size=1.0,
            white_color=Color(0.9, 0.9, 0.9),
            black_color=Color(0.2, 0.2, 0.2)
        )
        self.add(PlaneUV(point=Vector3D(0, 0, 0), normal=Vector3D(0, 0, 1), forward_direction=Vector3D(1, 1, 0)), gray_material)
