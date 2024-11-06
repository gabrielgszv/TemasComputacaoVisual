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

#---------------------------------------------------------------------------------------

#Questão 3

#---------------------------------------------------------------------------------------


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

    #Transformar em uma matriz novamente

    matrix = txt_para_matriz(txt)    

    #Agora passando por todos os elementos da matriz par acontar as ilhas

    visitados = []
    direcoes = [(0, -1), (1,-1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    qilha = 0
    
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            
            def ilhar(m, n):
                if (m,n) not in visitados:
                    visitados.append((m, n))
                    if matrix[m][n] == '1':
                        for p, q in direcoes:
                            if (m+p >= 0 and n+q >= 0) and (m+p < len(matrix[0]) and n+q < len(matrix)):
                                ilhar(m+p, n+q)   
            if matrix[x][y] == '1' and (x,y) not in visitados:
                qilha +=1

            ilhar(x,y)    

    return qilha               
    

print(numero_de_ilhas('test_map.txt'))

#---------------------------------------------------------------------------------------

#Questão 4

#---------------------------------------------------------------------------------------
   
'''
Mesmo codigo que a questao anterior so que com as modificações para retornar
as coordenadas do centroide da maior e menor ir
'''


def numero_de_ilhas_modificado(txt):

    matrix = txt_para_matriz(txt)    

    visitados = []
    direcoes = [(0, -1), (1,-1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    qilha = 0
    ilhas = []

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            ilha = []
            def ilhar(m, n):
                if (m,n) not in visitados:
                    visitados.append((m, n))
                    if matrix[m][n] == '1':
                        ilha.append((m, n))
                        for p, q in direcoes:
                            if (m+p >= 0 and n+q >= 0) and (m+p < len(matrix[0]) and n+q < len(matrix)):
                                ilhar(m+p, n+q)   
     
            ilhas.append(ilha)                          

            if matrix[x][y] == '1' and (x,y) not in visitados:
                qilha +=1

            ilhar(x,y)

    ilhasf = []

    for ilha in ilhas:
        if len(ilha) > 0:
            ilhasf.append(ilha)

    menor_ilha = min(ilhasf, key=len)      
    maior_ilha = max(ilhasf, key=len)

    return qilha         



print(numero_de_ilhas('test_map.txt'))


#---------------------------------------------------------------------------------------

#Questão 5

#---------------------------------------------------------------------------------------
   
def ilha(txt):

    matrix = txt_para_matriz(txt)   
    direcoes = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ilhas = []

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            c = 0
            for p, q in direcoes:
                if (x+p >= 0 and y+q >= 0) and (x+p < len(matrix[0]) and y+q < len(matrix)):
                    if matrix[x+p][y+q] == '1':
                        c += 1
                else:
                    c+=1        
            if c == 4:
                ilhas.append((x,y)) 

    if ilhas:
        return ilhas
    else:
        return None            

print(ilha('test_map.txt'))

