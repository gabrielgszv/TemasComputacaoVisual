"""
Exercício 1 

a)1
  2
  
b) Value is bad

c)que massa!

d)[1,2,5,4]

Exercício 2

a) Na linha 2, alterar nome do método "_ints" para "init_"

b)
[]
[2.0, 1.0]

c)
Linha 20, alterar de:
new_vector[i] = self.values[i] + self.values[i]

para:
new_vector[i] = self.values[i] + other_vector.values[i]
"""

"""
Exercício 3 letra a
"""
import math

class Circle():

    def _init_(self, point: list, radius: float) -> None:
        self.point = point
        self.radius = radius

    def check(self, point: list) -> int:
        # obter distância dos dois pontos
        d = math.sqrt((self.point[0] - point[0])*2 + (self.point[1] - point[1])*2)

        # comparar com o raio
        if (d < self.radius):
            return -1
        elif (d == self.radius):
            return 0
        else:
            return 1
        
"""
#Exercicio 3 letra b
"""

class Line_Segment():
    def _init_(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def check(self, point3):
        if ((point3[1] < self.point1[1]) == (point3[1] < self.point2[1])):
            return False
            
        if ((point3[0] < self.point1[0]) == (point3[0] < self.point2[0])):
            return False
            
        if ((self.point2[0]-self.point1[0])(point3[1]-self.point1[1])) != ((self.point2[1]-self.point1[1])(point3[0]-self.point1[0])):
            return False
        
        return True  

"""
Exercicio 4
"""

def verif(a:Circle, b:Line_Segment):
    return c.check(b.point1) == -1 and c.check(b.point2) == -1


"""
Exercicio 5
"""

class Vector():
    
    def __init__(self, vector: list) -> None:
        self.vector = vector
        
    def dyadic_product(self, other_vector: 'Vector') -> list:
        u = []
        for i in range(len(self.vector)):
            result = []
            for j in range(len(other_vector.vector)):
                result.append(self.vector[i] * other_vector.vector[j])
            u.append(result)
        return u
