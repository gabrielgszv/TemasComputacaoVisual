#Questão 1

'''
A função vai receber um array de pontos "data" e um ponto "point",
assim vai calcular a norma da distancia dos pontos e 
vai retornar o ponto do array mais proximo do point.

Como a função vai passar por cada ponto do array "data", a complexidade é O(n)
'''

#---------------------------------------------------------------------------------------
    
#Questão 2

#---------------------------------------------------------------------------------------
'''
A ideia para substituir a recursão da função é usar uma pilha para guardar os pontos visitados,
para quando chegar no final, usar o "last in, first out" para voltar e encontrar outros caminhos
'''

import random

#Codigo do CodigosExcercicios/maze builder.py

def generate_maze(m, n, room = 0, wall = 1, cheese = '.' ):
    
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y):

        pilha = [(x,y)]        
        maze[2 * x + 1][2 * y + 1] = room

        while pilha:
            cx, cy = pilha.pop()
            
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy  

                if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                    
                    maze[2 * cx + 1 + dx][2 * cy + 1 + dy] = room
                    
                    maze[2 * nx + 1][2 * ny + 1] = room
                    
                    pilha.append((nx,ny))

    dfs(0, 0)

    while True: 
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese 
            break

    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

#Exemplo do labirinto no fim da Questão 3

#---------------------------------------------------------------------------------------

#Questão 3

#---------------------------------------------------------------------------------------

'''
Acho que nao é a melhor implementação, mas a ideia que tive foi passar por todos os caminhos,
guardar todos os pontos que passou em uma lista para nao passar novamente,
e o caminho que chega ao queijo vai sendo adicionado em uma pilha, retirando os pontos em que passou mas voltou.
E teve uso de busca em profundidade, ja que teve pilha para guardar o caminho percorrido ate encontrar o queijo
'''

def achar_caminho(maze):
    pinicio = (1, 1)
    lista = []

    # Direções na ordem: esquerda, baixo, direita, cima
    direcoes = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    pilha = [(pinicio, [pinicio])]

    while pilha:
        (x, y), caminho = pilha.pop()

        if (x, y) in lista:
            continue
        lista.append((x, y))

        if maze[x][y] == '*':
            for k in caminho:
                xs, ys = k
                maze[xs][ys] = '+'
            print('Caminho:')
            print_maze(maze)
            break

        for dx, dy in direcoes:
            xn, yn = x + dx, y + dy
            if maze[xn][yn] != 'H':
                pilha.append(((xn, yn), caminho + [(xn, yn)]))

if __name__ == '__main__':
    m, n = 5, 7
    room = ' '
    wall = 'H'
    cheese = '*'
    maze = generate_maze(m, n, room, wall, cheese)
    print('\nLabirinto:')
    print_maze(maze)                
    achar_caminho(maze)

#---------------------------------------------------------------------------------------
    
#Questão 4

#---------------------------------------------------------------------------------------

class Grafo:
    def __init__(self):
        self.grafo = {}

    def adjacent(self, x, y):
        if x in self.grafo:
            if y in self.grafo[x]:
                return True
        return False    

    def neighbors(self, x) -> list:
        return list(self.grafo[x]['Vizinhos'])

    def add_vertex(self, x):
        if x in self.grafo:
            return False
        else:
            self.grafo[x] = {'Vizinhos': []}
            return True
        
    def remove_vertex(self, x):
        if x in self.grafo:
            self.grafo.pop(x)
            return True    
        else:
            return False

    def add_edge(self, x, y):
        if y in self.grafo[x]:
            return False
        self.grafo[x]['Vizinhos'].append(y)
        return True
        
    def remove_edge(self, x, y):
        if y in self.grafo[x]:
            self.grafo[x].pop(y)
            return True
        return False
    
    def get_vertex_value(self, x):
        if x in self.grafo:
            if 'Valor' in self.grafo[x]:
                return self.grafo[x]['Valor']
            else:
                return None

    def set_vertex_value(self, x, v):
        if x in self.grafo.keys():
            self.grafo[x]['Valor'] = v    

#Testes da questão 4

if __name__ == '__main__':

    #Criando o Grafo
    grafot = Grafo()

    #Adicionando vértices ao grafo
    grafot.add_vertex('A')
    grafot.add_vertex('B')
    grafot.add_vertex('C')
    grafot.add_vertex('D')
    grafot.add_vertex('E')

    #Adicionando arestas entre alguns vértices
    grafot.add_edge('A','B')
    grafot.add_edge('A','C')
    grafot.add_edge('B','E')
    grafot.add_edge('B','C')
    grafot.add_edge('D','B')
    grafot.add_edge('D','E')

    #Verificando se os vértices são adjacentes
    print(grafot.adjacent('A','B'))
    print(grafot.adjacent('B','C'))

    #Verificando os vizinhos 
    print(grafot.neighbors('A'))

    #Removendo vértice (Se existir)
    print(grafot.remove_vertex('E'))

    #Removendo aresta (Se existir)
    print(grafot.remove_edge('D','C'))

    #Adicionando valores aos vértices
    grafot.set_vertex_value('A', 10)
    grafot.set_vertex_value('B', 20)
    grafot.set_vertex_value('C', 30)
    grafot.set_vertex_value('D', 40)

    #Retornando o valor do vértice
    print(grafot.get_vertex_value('A'))

    #Grafo inteiro
    print(grafot.grafo)

    '''
    Apenas não resolvi resolvi um 'problema' ao remover um vertice,
    se um vertice x estiver conectado com um y, e esse vértice y for excluido,
    o x ainda conta o y como o vizinho, mesmo ele estando apagado
    '''
