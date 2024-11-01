#---------------------------------------------------------------------------------------
    
#Questão 1

#---------------------------------------------------------------------------------------

def caminho(grafo, ponto):
    visitados = []
    fila = [ponto]

    while fila:
        vertice = fila.pop(0)
        visitados.append(vertice)

        for k in grafo[vertice]:
            if k not in visitados:
                fila.append(k)
    print(visitados)            

grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

caminho(grafo, 2)
