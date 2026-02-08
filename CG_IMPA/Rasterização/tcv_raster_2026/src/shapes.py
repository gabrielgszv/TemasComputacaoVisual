from .base import Shape

class Circle(Shape):
    def __init__(self, center, radius):
        super().__init__("circle")
        self.center = center
        self.radius = radius

    def in_out(self, point):
        dx = point[0] - self.center[0]
        dy = point[1] - self.center[1]
        return (dx * dx + dy * dy) <= (self.radius * self.radius)

class Triangle(Shape):
    def __init__(self, vertex1, vertex2, vertex3):
        super().__init__("triangle")
        self.v1 = vertex1
        self.v2 = vertex2
        self.v3 = vertex3

    def in_out(self, point):

        def cross(u, v):
            return u[0] * v[1] - u[1] * v[0]
        
        #Vetores
        v0 = (point[0]-self.v1[0], point[1]-self.v1[1]) #P-A
        v1 = (self.v2[0]-self.v1[0], self.v2[1]-self.v1[1]) #B-A
        v2 = (self.v3[0]-self.v1[0], self.v3[1]-self.v1[1]) #C-A

        #Calculo das coordenadas baricentricas
        beta = cross(v0,v2)/cross(v1,v2)
        gamma = cross(v1,v0)/cross(v1,v2)
        alpha = 1 - beta - gamma

        return alpha >= 0 and beta >= 0 and gamma >= 0

class ImplicitFunction(Shape):
    def __init__(self, function):
        super().__init__("implicit_function")
        self.func = function

    def in_out(self, point):
        return self.func(point) <= 0
    

#==========================================
#Desafio
#==========================================

class Mandelbrot(Shape):
    def __init__(self, max_iter=100):
        super().__init__("mandelbrot")
        self.max_iter = max_iter

    def in_out(self, point):
        x, y = point
        c = complex(x, y)
        z = 0 + 0j

        for _ in range(self.max_iter):
            z = z*z + c
            if abs(z) > 2:
                return False

        return True