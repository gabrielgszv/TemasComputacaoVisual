import turtle
import re

class Point2D:
    def __init__(self, x, y):
        self.coord = (x, y)

class Polygon:
    def __init__(self, points, color):
        self.points = points
        self.color = color

class Polygons:
    def __init__(self):
        self.polygons = {}

    def add_polygon(self, polygon: Polygon, name: str):    
        self.polygons[name] = polygon

    def remove_polygon(self, name: str):
        self.polygons.pop(name)

    def save_to_file(self, filename: str):
        with open(filename, 'w') as f:
            for p in self.polygons:
                for i in self.polygons[p].points:
                    f.write(str(i.coord))
                f.write(f'; {self.polygons[p].color}; {p}\n')

    def load_from_file(self, filename: str):
        with open(filename, 'r') as f:
            padrao = r'\((-?\d+),\s*(-?\d+)\)'
            for linha in f:
                #em cada linha criar um objeto do tipo polygon
                poligono = []
                pontos = re.findall(padrao, linha)
                j = 0
                while j < len(pontos) -1:
                    point = Point2D(pontos[j], pontos[j+1])
                    poligono.append(point)
                    j += 1
                print(poligono)

        
        return True      



#5 Questao

def plot_polygons(poligono: Polygons):
    screen = turtle.Screen()

    t = turtle.Turtle()

    p, c, n = poligono.load_from_file('texto.txt')
    for i in p:
        t.penup()
        t.goto(i[0])
        t.pendown()

        for k in i:
            t.goto(k)

        t.goto(i[0]) 
        cor = c[p.index(i)]
        t.fillcolor(cor)
        t.begin_fill()
        for k in i:
            t.goto(k)
        t.end_fill()

    screen.exitonclick()      




if __name__ == '__main__':

    poligonos = Polygons()

    p1 = Point2D(0,0)
    p2 = Point2D(100,1)
    p3 = Point2D(0,245)
    p4 = Point2D(-100,214)

    poligono = Polygon([p1,p2,p3,p4],'green')
    poligonos.add_polygon(poligono,'primeiro')

    p1 = Point2D(140,-65)
    p2 = Point2D(33,-21)
    p3 = Point2D(12,-92)

    poligono = Polygon([p1,p2,p3],'red')
    poligonos.add_polygon(poligono,'segundo')

    p1 = Point2D(-123,-234)
    p2 = Point2D(24,365)
    p3 = Point2D(-310,92)

    poligono = Polygon([p1,p2,p3],'blue')
    poligonos.add_polygon(poligono,'terceiro')
    
    poligonos.save_to_file('texto.txt')

    print(plot_polygons(poligonos))
    
