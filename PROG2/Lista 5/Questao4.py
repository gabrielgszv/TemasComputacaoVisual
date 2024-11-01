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

    '''
    Apenas não resolvi resolvi um 'problema' ao remover um vertice,
    se um vertice x estiver conectado com um y, e esse vértice y for excluido,
    o x ainda conta o y como o vizinho, mesmo ele estando apagado
    '''
