# defines a scene with a ball using implicit function
import math
from src.base import BaseScene, Color
from src.shapes import Ball, PlaneUV, Cube, Cylinder, ObjectTransform, Surface
from src.camera import Camera
from src.vector3d import Vector3D
from src.light import PointLight, AreaLight
from src.materials import SimpleMaterial, SimpleMaterialWithShadows, TranslucidMaterial, CheckerboardMaterial

class Scene(BaseScene):
    def __init__(self):
        super().__init__("Ball Scene")

        # light blue background
        self.background = Color(0.7, 0.8, 1)
        self.ambient_light = Color(0.1, 0.1, 0.1)
        self.max_depth = 10  # for reflections/refractions
        self.camera = Camera(
            eye=Vector3D(0, -8, 3),
            look_at=Vector3D(0, 0, 1),
            up=Vector3D(0, 0, 1),
            fov=35,
            img_width=800,
            img_height=600,
            len_size=0.6,
        )

        self.lights = [
            # add a point light
            #PointLight(position=Vector3D(0, 1, 1)*10, color=Color(1, 1, 1), intensity=1.6),
            AreaLight(
                position=Vector3D(5, -5, 10), #Mudei a posicao da luz
                look_at=Vector3D(0, 0, 0),
                up=Vector3D(0, 0, 1),
                width=4,
                height=4,
                color=Color(1, 1, 1),
                intensity=1.6
            )
        ]

        material = SimpleMaterial(
            ambient_coefficient=0.1,
            diffuse_coefficient=0.8,
            diffuse_color=Color(0.7,0.2,0.2),
            specular_coefficient=0.3,
            specular_color=Color(1,1,1),
            specular_shininess=32
        )

        #Esferas
        self.add(Ball(Vector3D(-2, -1, 1), 1), material)  #Perto focus=7.55
        self.add(Ball(Vector3D(0, 0, 1), 1), material)    #MEio focus=8.25
        self.add(Ball(Vector3D(2, 3, 1), 1), material)    #Longe focus=11.35

        # ground plane
        gray_material = CheckerboardMaterial(
            ambient_coefficient=1,
            diffuse_coefficient=0.8,
            square_size=1.0,
            white_color=Color(0.9, 0.9, 0.9),
            black_color=Color(0.2, 0.2, 0.2)
        )
        self.add(PlaneUV(point=Vector3D(0, 0, 0), normal=Vector3D(0, 0, 1), forward_direction=Vector3D(1, 1, 0)), gray_material)
