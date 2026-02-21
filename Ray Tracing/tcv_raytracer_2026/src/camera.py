# world is right-handed, z is up
import math
import random
from .ray import Ray

#===============================
# Parte 5 da Atividade
#===============================

class Camera:
    def __init__(self, eye, look_at, up, fov, img_width, img_height, len_size=0.0, focus_distance=0.0):
        self.eye = eye
        # self.look_at = look_at
        # self.up = up
        # self.fov = fov
        # self.aspect_ratio = aspect_ratio
        self.img_width = img_width
        self.img_height = img_height

        aspect_ratio = img_height / img_width

        self.su = 2 * math.tan(math.radians(fov) / 2)
        self.sv = self.su * aspect_ratio

        self.w = (eye - look_at).normalize()
        up = up.normalize()
        #self.u = self.w.cross(up).normalize()
        self.u = up.cross(self.w).normalize()
        self.v = self.w.cross(self.u).normalize()
        
        
        #Tamanho da lente
        self.len_size = len_size 
        #Distância de foco
        if focus_distance == 0.0:
            self.focus_distance = (look_at - eye).length()
        else:
            self.focus_distance = focus_distance

    def point_image2world(self, x, y):
        # from image coordinates to coordinates 
        # in the camera's view plane
        x_ndc = self.su * x / self.img_width - self.su / 2
        y_ndc = self.sv * y / self.img_height - self.sv / 2

        # from view plane to world coordinates
        return self.eye + self.u * x_ndc * self.focus_distance + self.v * y_ndc * self.focus_distance - self.w * self.focus_distance

    def ray(self, x, y):
        point_world = self.point_image2world(x, y)

        if self.len_size/2 == 0:
            direction = (point_world - self.eye).normalize()
            return Ray(self.eye, direction)
        
        #Pegar um ponto aleatório na lente
        r = self.len_size/2 * math.sqrt(random.random())
        theta = 2 * math.pi * random.random()

        dx = r * math.cos(theta)
        dy = r * math.sin(theta)

        len_point = self.eye + self.u * dx + self.v * dy

        direction = (point_world - len_point).normalize()

        return Ray(len_point, direction)