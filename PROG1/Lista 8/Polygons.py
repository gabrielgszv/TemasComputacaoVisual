import turtle
import re

class Point2D:
    def __init__(self, x, y):
        self.coord = (x, y)

    def __str__(self):
        return f'{self.coord}'

class Polygon:
    def __init__(self, points, color):
        self.points = points
        self.color = color

    def __str__(self):
        pontos = []
        for i in self.points:
            pontos.append(i.coord)
        pontos = str(pontos)    
        return f'Pontos: {pontos[1:-1]}\nCor: {self.color}'

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
            #O for passará por cada linha
            for linha in f:
                #Em cada linha criar um objeto do tipo polygon
                pontospoligono = []

                #Separar as linhas para definir o que é nome, cor e pontos
                partes = linha.split('; ')
                cor = partes[1]
                nome = partes[2]
                if partes[2][-1] == '\n':
                    nome = partes[2][0:-1] 
                pontos = re.findall(padrao, partes[0])
                
                #Como os pontos sao salvos em uma string de tupla com parenteses e virgula,
                #se adiciona elemento a elemento das tuplas em uma lista 'p' utilizando o padrao regex, ficando os numeros um apos o outro
                j = 0
                p = []
                for tupla in pontos:
                    for i in tupla:
                        p.append(int(i)) 

                #Como a lista esta em numeros seguidos do tipo [x1, y1, x2, y2, ...] os x1, y1, define um ponto
                #e assim com todos os numeros da lista, criando um objeto do tipo Point2D
                l = []  
                while j < 2* len(pontos) :
                    l.append(p[j])
                    if len(l) == 2:
                        point = Point2D(l[0], l[1])
                        l = []
                        pontospoligono.append(point)
                    j += 1   
                #Criando o poligono com os dados coletados da linha e adicionando aos poligonos    
                poligono = Polygon(pontospoligono, cor)
                self.add_polygon(poligono, nome)  

                    

#5 Questao

def plot_polygons(poligono: Polygons):
    screen = turtle.Screen()

    t = turtle.Turtle()
    poligonos = poligono.polygons
    p = []
    for k in poligonos:
        p = poligonos[k].points
        t.penup()
        t.goto(p[0].coord)
        t.pendown()

        for i in p:
            t.goto(i.coord)

        t.goto(p[0].coord) 
        cor = poligonos[k].color
        t.fillcolor(cor)
        t.begin_fill()
        for i in p:
            
            t.goto(i.coord)
        t.end_fill()
        
    screen.exitonclick()  
    
        

if __name__ == '__main__':
    #Função apenas para deixar mais facil de printar varias vezes
    def pri():
        for key in poligonos.polygons:
            print('Nome: ', key)
            print(poligonos.polygons[key])
            print('------------')
        print(' ')

    #Criação do objeto Polygons
    poligonos = Polygons()
    
    #Criação dos pontos
    p1 = Point2D(100,100)
    p2 = Point2D(200,100)
    p3 = Point2D(150,300)

    #Criação do Poligono
    poligono = Polygon([p1,p2,p3],'green')
    poligonos.add_polygon(poligono,'triangulo')

    #Printar Poligonos
    print('Poligonos')
    pri()

    #Criação de outros pontos
    p1 = Point2D(-100,100)
    p2 = Point2D(-100,200)
    p3 = Point2D(-200,200)
    p4 = Point2D(-200,100)

    #Criação de Outro Poligono
    poligono = Polygon([p1,p2,p3,p4],'blue')

    #Adicionando Poligono
    print('Adicionar o poligono quadrado na classe Poligonos')
    poligonos.add_polygon(poligono,'quadrado')
    pri()

    #Removendo Poligono
    print('Remover o poligono triangulo da classe Poligonos')
    poligonos.remove_polygon('triangulo')
    pri()

    #Funçao save_to_file()
    poligonos.save_to_file('poligonos.txt')  

    #Função load_from_file()
    poligonos.load_from_file('outrospoligonos.txt')
    print('Poligonos depois de ler outro arquivo')
    pri()

    poligonos.save_to_file('poligonos.txt') 

    #plot_polygons(poligonos)
    
