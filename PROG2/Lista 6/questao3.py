
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


