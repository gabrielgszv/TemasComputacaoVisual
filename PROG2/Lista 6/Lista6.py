#---------------------------------------------------------------------------------------

#Questão 1

#---------------------------------------------------------------------------------------

'''
Até a linha 60 é a mesma classe grafo da lista anterior para facilitar
'''

class Grafo:
    def __init__(self):
        self.grafo = {}

    def adjacent(self, x, y):
        if x in self.grafo:
            if y in self.grafo[x]['Vizinhos']:
                return True
        return False    

    def neighbors(self, x) -> list:
        return list(self.grafo[x]['Vizinhos'])

    def add_vertex(self, x):
        if x in self.grafo:
            return False
        else:
            self.grafo[x] = {'Vizinhos': [],'Valor': None}
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

#Função da questão     

def bfs(grafo, v_inicial = None):

    if v_inicial is None:
        v_inicial = list(grafo.grafo.keys())[0]

    visitados = []
    fila = [v_inicial]

    while fila:
        vertice = fila.pop(0)
        visitados.append(vertice)

        for k in grafo.grafo[vertice]['Vizinhos']:
            if k not in visitados:
                fila.append(k)
    return visitados           

#Exemplo para teste
'''
grafo1 = Grafo()
grafo1.add_vertex('A')
grafo1.add_vertex('B')
grafo1.add_vertex('C')
grafo1.add_vertex('D')
grafo1.add_vertex('E')
grafo1.add_edge('A','B')
grafo1.add_edge('A','C')
grafo1.add_edge('B','A')
grafo1.add_edge('B','D')
grafo1.add_edge('B','E')
grafo1.add_edge('C','A')
grafo1.add_edge('D','B')
grafo1.add_edge('E','B')

bfs(grafo1, 'D')
'''
#---------------------------------------------------------------------------------------

#Questão 2

#---------------------------------------------------------------------------------------

'''
Aproveitando da função da questão passada para ter o caminho,
agora é so percorrer o caminho e achar qual vertice tem essa propriedade,
caso nao tenha a função retorna None
'''

def busca_propriedade(G, value):

    caminho = bfs(G)

    for vertice in caminho:
        if G.grafo[vertice]['Valor'] == value:
            return vertice
        
    return None    

#Exemplo para teste
'''
grafo1.set_vertex_value('A', 10)
grafo1.set_vertex_value('B', 20)
grafo1.set_vertex_value('C', 30)
grafo1.set_vertex_value('D', 40)
grafo1.set_vertex_value('E', 50)
print('Vértice',busca_propriedade(grafo1, 30))
'''
#---------------------------------------------------------------------------------------

#Questão 3

#---------------------------------------------------------------------------------------

'''
Função apenas para transformar o txt em uma matriz
'''

def txt_para_matriz(matriz):

    matrix = []
    with open(matriz, "r") as f:
        for linha in f:
            new_line = []
            linha = linha.strip()
            for i in linha:
                new_line.append(i)
            matrix.append(new_line) 

    return matrix        

def numero_de_ilhas(txt):

    matrix = txt_para_matriz(txt)    

    visitados = []
    direcoes = [(0, -1), (1,-1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    qilha = 0

    #Função para percorrer uma ilha inteira

    def ilhar(m, n):
        if (m,n) not in visitados:
            visitados.append((m, n))

            if 0 <= m < len(matrix) and 0 <= n < len(matrix[0]):
                if matrix[m][n] == '1':

                    for p, q in direcoes:
                        if 0 <= m+p < len(matrix) and 0 <= n+q < len(matrix[0]):
                            ilhar(m+p, n+q)  

    #Percorrer todos os elementos da matriz                        

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):

            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):                              
                if matrix[x][y] == '1' and (x,y) not in visitados:
                    qilha +=1

            ilhar(x,y)  

    return qilha               
    

#---------------------------------------------------------------------------------------

#Questão 4

#---------------------------------------------------------------------------------------
   
'''
Mesmo codigo que a questao anterior so que com as modificações para retornar
as coordenadas do centroide da maior e menor ilha
'''

def numero_de_ilhas_modificado(txt):

    matrix = txt_para_matriz(txt)    

    visitados = []
    direcoes = [(0, -1), (1,-1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    qilha = 0

    ilhas = []

    #Função para percorrer uma ilha inteira

    def ilhar(m, n):
        if (m,n) not in visitados:
            visitados.append((m, n))
            
            if 0 <= m < len(matrix) and 0 <= n < len(matrix[0]):
                if matrix[m][n] == '1':
                    ilha.append((m, n))

                    for p, q in direcoes:
                        if 0 <= m+p < len(matrix) and 0 <= n+p < len(matrix[0]):
                            ilhar(m+p, n+q)

    #Percorrer todos os elementos da matriz                           

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):

            #Sempre que achar uma ilha, vai salvar o caminho inteiro dessa ilha na lista ilhas

            ilha = []
            ilhas.append(ilha)  
                        
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                if matrix[x][y] == '1' and (x,y) not in visitados:
                    qilha +=1

            ilhar(x,y)

    #Esse for é apenas para tirar as listas nulas 

    ilhasf = []
    for ilha in ilhas:
        if len(ilha) > 0:
            ilhasf.append(ilha)

    #Ver qual a menor e a maior ilha        

    menor_ilha = min(ilhasf, key=len)      
    maior_ilha = max(ilhasf, key=len)

    #Calcular o centroide

    #Menor
    x, y = 0, 0

    for p, q in menor_ilha:
        x += p
        y += q

    x = x/len(menor_ilha)   
    y = y/len(menor_ilha) 

    centroide_menor = (x, y)
    
    #Maior
    x, y = 0, 0

    for p, q in maior_ilha:
        x += p
        y += q

    x = x/len(maior_ilha)   
    y = y/len(maior_ilha) 

    centroide_maior = (x, y)

    return centroide_menor, centroide_maior   


#---------------------------------------------------------------------------------------

#Questão 5

#---------------------------------------------------------------------------------------
'''
A função vai passar por cada elemento da matriz e olhar nas quatro direções
para ver se tem terra, só sera considerado ilha se tiver exatamente nas quatro direções,
não será considerado por exemplo um lago que esteja na primeira linha e tenha terra na
esquerda, direita e abaixo(o que deu a entender da questão)

E não sei se era pra retornar apenas se a matriz tinha lago ou nao,
então coloquei para retornar todos os lagos encontrados(caso exista)
'''


def lago(txt):

    matrix = txt_para_matriz(txt)  

    direcoes = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ilhas = []

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            c = 0
            for p, q in direcoes:
                if (x+p > 0 and y+q > 0) and (x+p < len(matrix) and y+q < len(matrix[0])):
                    if matrix[x+p][y+q] == '1':
                        c += 1
                     
            if c == 4:
                if matrix[x][y] == '1':
                    continue
                ilhas.append((x,y)) 

    if ilhas:
        return ilhas
    else:
        return None            
