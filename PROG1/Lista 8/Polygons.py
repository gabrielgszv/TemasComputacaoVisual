import turtle
import csv
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
        pontos = []
        cor = []
        nome = []
        with open(filename, 'r') as f:
            reader = csv.reader(f,delimiter=';')
            for i in reader:
                padrao = r'-?\d+' 
                numeros = re.findall(padrao, i[0])
                j = 0
                p = []
                while j < len(numeros):
                    p.append((float(numeros[j]),float(numeros[j+1])))
                    j+=2  
                pontos.append(p)    
                cor.append(i[1])
                nome.append(i[2])

        return pontos, cor, nome       



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
        cor = c[p.index(i)][1:]
        
        t.fillcolor(cor)
        t.begin_fill()
        for k in i:
            t.goto(k)
        t.end_fill()

    screen.exitonclick()      








if __name__ == '__main__':

    poligonos = Polygons()

    p1 = Point2D(0,0)
    p2 = Point2D(100,0)
    p3 = Point2D(0,245)

    poligono = Polygon([p1,p2,p3],'yellow')
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
