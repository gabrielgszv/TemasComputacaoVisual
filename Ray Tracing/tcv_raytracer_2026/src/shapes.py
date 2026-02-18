from src.vector3d import Vector3D
from .base import Shape, HitRecord, CastEpsilon
from .ray import Ray
import numpy as np

class Ball(Shape):
    def __init__(self, center, radius):
        super().__init__("ball")
        self.center = center
        self.radius = radius

    def hit(self, ray):
        # Ray-sphere intersection
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return HitRecord(False, float('inf'), None, None)
        else:
            hit, point, normal = False, None, None
            t = (-b - discriminant**0.5) / (2.0 * a)
            if t > CastEpsilon:
                hit = True
                point = ray.point_at_parameter(t)
                normal = (point - self.center).normalize()
            else:
                t = (-b + discriminant**0.5) / (2.0 * a)
                if t > CastEpsilon:
                    hit = True
                    point = ray.point_at_parameter(t)
                    normal = (point - self.center).normalize()

            return HitRecord(hit, t, point, normal)

class Plane(Shape):
    def __init__(self, point, normal):
        super().__init__("plane")
        self.point = point
        self.normal = normal.normalize()

    def hit(self, ray):
        denom = self.normal.dot(ray.direction)
        if abs(denom) > 1e-6:
            t = (self.point - ray.origin).dot(self.normal) / denom
            if t >= CastEpsilon:
                point = ray.point_at_parameter(t)
                return HitRecord(True, t, point, self.normal)
        return HitRecord(False, float('inf'), None, None)

class PlaneUV(Shape):
    def __init__(self, point, normal, forward_direction):
        super().__init__("plane")
        self.point = point
        self.normal = normal.normalize()
        self.forward_direction = forward_direction.normalize()
        # compute right direction
        self.right_direction = self.normal.cross(self.forward_direction).normalize()

    def hit(self, ray):
        denom = self.normal.dot(ray.direction)
        if abs(denom) > 1e-6:
            t = (self.point - ray.origin).dot(self.normal) / denom
            if t >= CastEpsilon:
                point = ray.point_at_parameter(t)
                # Calculate UV coordinates
                vec = point - self.point
                u = vec.dot(self.right_direction)
                v = vec.dot(self.forward_direction)
                uv = Vector3D(u, v, 0)
                return HitRecord(True, t, point, self.normal, uv=uv)
        return HitRecord(False, float('inf'), None, None)

class ImplicitFunction(Shape):
    def __init__(self, function):
        super().__init__("implicit_function")
        self.func = function

    def in_out(self, point):
        return self.func(point) <= 0
    
#============================================
# Parte 1 da Tarefa
#============================================


class Cube(Shape):
    def __init__(self, center, size):
        super().__init__("cube")
        self.center = center
        self.size = size

    def hit(self, ray):

        new_origin = ray.origin - self.center
        new_ray = Ray(new_origin, ray.direction)

        pmin = -self.size / 2
        pmax = self.size / 2

        #Eixo x
        tx1 = (pmin - new_ray.origin.x) / new_ray.direction.x
        tx2 = (pmax - new_ray.origin.x) / new_ray.direction.x
        tmin = min(tx1, tx2)
        tmax = max(tx1, tx2)

        #Eixo y
        ty1 = (pmin - new_ray.origin.y) / new_ray.direction.y
        ty2 = (pmax - new_ray.origin.y) / new_ray.direction.y
        tmin = max(tmin, min(ty1, ty2))
        tmax = min(tmax, max(ty1, ty2))

        #Eixo z
        tz1 = (pmin - new_ray.origin.z) / new_ray.direction.z
        tz2 = (pmax - new_ray.origin.z) / new_ray.direction.z
        tmin = max(tmin, min(tz1, tz2))
        tmax = min(tmax, max(tz1, tz2))

        #Verificar se o raio passa pelo cubo
        if tmax < max(tmin, CastEpsilon):
            return HitRecord(False, float('inf'), None, None)

        point = new_ray.point_at_parameter(tmin)

        #Normal
        epsilon = 1e-5
        if abs(point.x - pmin) < epsilon:
            normal = Vector3D(-1, 0, 0)
        elif abs(point.x - pmax) < epsilon:
            normal = Vector3D(1, 0, 0)
        elif abs(point.y - pmin) < epsilon:
            normal = Vector3D(0, -1, 0)
        elif abs(point.y - pmax) < epsilon:
            normal = Vector3D(0, 1, 0)
        elif abs(point.z - pmin) < epsilon:
            normal = Vector3D(0, 0, -1)
        else:
            normal = Vector3D(0, 0, 1)

        return HitRecord(True, tmin, point + self.center, normal)

class Cylinder(Shape):
    def __init__(self, center, r, h):
        super().__init__("cylinder")
        self.center = center
        self.r = r
        self.h = h


    def hit(self, ray):

        new_origin = ray.origin - self.center
        new_ray = Ray(new_origin, ray.direction)

        #Parametros
        hit, point, normal = False, None, None
        t_min = float('inf')

        #Lateral do cilindro

        a = new_ray.direction.x**2 + new_ray.direction.y**2
        b = 2*(new_ray.origin.x*new_ray.direction.x + new_ray.origin.y*new_ray.direction.y)
        c = new_ray.origin.x**2 + new_ray.origin.y**2 - self.r**2

        discriminant = b*b - 4*a*c

        if discriminant >= 0:

            t1 = (-b - discriminant**0.5) / (2*a)
            t2 = (-b + discriminant**0.5) / (2*a)

            if t1 > CastEpsilon:
                p = new_ray.point_at_parameter(t1)
                if abs(p.z) <= self.h/2 and t1 < t_min:
                    t_min = t1
                    hit = True
                    point = p
                    normal = Vector3D(p.x, p.y, 0).normalize()

            if t2 > CastEpsilon:
                p = new_ray.point_at_parameter(t2)
                if abs(p.z) <= self.h/2 and t2 < t_min:
                    t_min = t2
                    hit = True
                    point = p
                    normal = Vector3D(p.x, p.y, 0).normalize()

        #Tampa superior
        t_top = (self.h/2 - new_ray.origin.z)/new_ray.direction.z
        if t_top > CastEpsilon:
            p = new_ray.point_at_parameter(t_top)
            if p.x**2 + p.y**2 <= self.r**2:
                if t_top < t_min:
                    t_min = t_top
                    hit = True
                    point = p
                    normal = Vector3D(0,0,1)

        #Tampa inferior
        t_bottom = (-self.h/2 - new_ray.origin.z)/new_ray.direction.z
        if t_bottom > CastEpsilon:
            p = new_ray.point_at_parameter(t_bottom)
            if p.x**2 + p.y**2 <= self.r**2:
                if t_bottom < t_min:
                    t_min = t_bottom
                    hit = True
                    point = p
                    normal = Vector3D(0,0,-1)

        return HitRecord(hit, t_min, point + self.center, normal)

#============================================
# Parte 2 da Tarefa
#============================================

class ObjectTransform(Shape):
    def __init__(self, obj, matrix):
        super().__init__("objectTransform")
        self.obj = obj
        self.matrix = np.array(matrix)
        self.M_inv = np.linalg.inv(self.matrix)

    def hit(self, ray):

        #Converter raio para o numpy
        org = np.array([ray.origin.x, ray.origin.y, ray.origin.z])
        dir = np.array([ray.direction.x, ray.direction.y, ray.direction.z])

        center = np.array([self.obj.center.x, self.obj.center.y, self.obj.center.z])

        #Transformar raio da cena para o espaço do objeto
        origin_obj = self.M_inv @ (org - center) + center
        direction_obj = self.M_inv @ dir

        ray_obj = Ray(Vector3D(origin_obj[0], origin_obj[1], origin_obj[2]), Vector3D(direction_obj[0], direction_obj[1], direction_obj[2]))

        #Onde raio bateu com o objeto
        raio = self.obj.hit(ray_obj)

        if not raio.hit:
            return raio
        
        #Transformar ponto do espaço do objeto de volta para a cena
        point = np.array([raio.point.x, raio.point.y, raio.point.z])
        point_world = self.matrix @ (point - center) + center

        #Normal
        normal = np.array([raio.normal.x, raio.normal.y, raio.normal.z])
        normal_world = self.M_inv.T @ normal
        normal_world = normal_world / np.linalg.norm(normal_world)

        t_world = np.dot(point_world - org, dir) / np.dot(dir, dir)

        return HitRecord(
            True,
            t_world,
            Vector3D(point_world[0], point_world[1], point_world[2]),
            Vector3D(normal_world[0], normal_world[1], normal_world[2])
        )
    
#============================================
# Parte 3 da Tarefa
#============================================

class Surface(Shape):

    def __init__(self, func, center=Vector3D(0,0,0)):

        super().__init__("implicit")
        self.func = func
        self.center = center
        self.box_min = center + Vector3D(-2,-2,-2)
        self.box_max = center + Vector3D(2,2,2)

    #Função para calcular g(t) = f(r(t))
    def g(self, ray, t):
        p = ray.point_at_parameter(t)
        p_local = p - self.center
        return self.func(p_local.x, p_local.y, p_local.z)

    #Função para calcular o gradiente
    def gradient(self, x, y, z):

        eps = 1e-5

        dx = (self.func(x+eps,y,z) - self.func(x-eps,y,z))/(2*eps)
        dy = (self.func(x,y+eps,z) - self.func(x,y-eps,z))/(2*eps)
        dz = (self.func(x,y,z+eps) - self.func(x,y,z-eps))/(2*eps)

        return Vector3D(dx,dy,dz).normalize()

    #Função para retornar o tempo que o raio entra e sai do box (se intersectar)
    def intersect_box(self, ray):

        tmin = -float("inf")
        tmax = float("inf")

        #Para cada eixo
        for axis in ['x','y','z']:

            origin = getattr(ray.origin, axis)
            direction = getattr(ray.direction, axis)
            bmin = getattr(self.box_min, axis)
            bmax = getattr(self.box_max, axis)

            if abs(direction) < 1e-8:
                if origin < bmin or origin > bmax:
                    return None, None
            else:
                t1 = (bmin-origin)/direction
                t2 = (bmax-origin)/direction
                tmin = max(tmin, min(t1,t2))
                tmax = min(tmax, max(t1,t2))

        if tmax < max(tmin, 0):
            return None, None

        return tmin, tmax

    #Metodo da bisseção para encontrar g(t) = 0
    def bisection(self, ray, a, b):

        for _ in range(25):
            mid = (a+b)/2
            if abs(self.g(ray,mid)) < 1e-6:
                return mid
            if self.g(ray,a)*self.g(ray,mid) < 0:
                b = mid
            else:
                a = mid

        return (a+b)/2


    def hit(self, ray):

        #Tempo de entrada e de saída da caixa
        t_entry, t_exit = self.intersect_box(ray)

        if t_entry is None:
            return HitRecord(False, float('inf'), None, None)

        dt = (t_exit - t_entry)/100

        t_prev = t_entry
        g_prev = self.g(ray, t_prev)

        for i in range(1, 100):
            
            t_curr = t_entry + i*dt
            g_curr = self.g(ray, t_curr)

            if g_prev*g_curr <= 0:

                t_root = self.bisection(ray, t_prev, t_curr)

                point = ray.point_at_parameter(t_root)
                p_local = point - self.center
                normal = self.gradient(p_local.x,
                                       p_local.y,
                                       p_local.z)

                return HitRecord(True, t_root, point, normal)

            t_prev = t_curr
            g_prev = g_curr

        return HitRecord(False, float('inf'), None, None)
