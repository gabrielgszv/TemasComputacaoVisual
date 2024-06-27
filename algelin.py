#Função para transformar matriz em identidade

def identidade(matriz):
    tamanho = len(matriz)
    identidade = []
    for i in range(tamanho):
        linha = []
        for n in range(tamanho):
            if i == n:
                linha.append(1)
            else:
                linha.append(0)
        identidade.append(linha)
    matriz = identidade
    return matriz  

#Função para transformar o pivô de uma linha em 1

def um(linha, divisor):
    result = []
    for i in range(len(linha)):
        result.append(linha[i]/divisor)
    return result

#Função para fazer uma operação elementar

def elementar(linha, divisor,linha2):
    result = []
    for i in range(len(linha)):
        linha[i] = linha[i] - divisor * linha2[i]
        result.append(linha[i])
    return result 

#Função para multiplicar duas matrizes

def multmatriz(matriz1, matriz2):
    a = matriz1
    b = matriz2
    result = []

    for i in range(len(a)):
        linha = []
        for o in range(len(a[0])):
            num = 0            
            for k in range(len(b)):
                num +=(a[i][k] * b[k][o])
            linha.append(num) 
        result.append(linha)       

    return result            



def gaussian_elimination(matriz):
    a = matriz
    p = identidade(matriz)
    l = identidade(matriz)
    iden = identidade(matriz)
    u = matriz
    coluna = len(u[0])
    linha = len(u)

    for i in range(linha):
        for c in range(coluna):
            if c > linha -1:
                break

            if u[i][c] == 0 and i==c:
                if i == linha -1 and c == coluna-1:
                    break
                for k in range(linha):
                    if c+k < linha -1:
                        break
                    if k == 0:
                        continue
                    if u[c+k][i] != 0:
                        u[c], u[c+k] = u[c+k], u[c]
                        p[c],p[c+k] = p[c+k], p[c]
                        print(p)
                        break
                break        

            pivol = iden[c]
            pivo = u[c]

            if i == c:
                div = u[i][c]
                u[i] = um(u[i],div)
                x = identidade(l)
                x[i][c] = div
                l = multmatriz(l,x)

            elif c < i:
                divisor = u[i][c] 
                u[i] = elementar(u[i],divisor,pivo) 

                x = identidade(l)

                x[i] = elementar(x[i],-1*divisor,pivol)
                l = multmatriz(l,x)
                

    return u

matriz = [[2,4,-1],
          [-3,0,5],
          [1,1,1]]

matriz = [[1,1,0],
          [2,9,0]]

def is_basis(vetores):
    u = gaussian_elimination(vetores)
    print(u)
    cont = 0
    for i in range(len(u)):
        for j in range(len(u[0])):
            if u[i][j] != 0:
                break
            cont +=1
        if cont == len(u[0]):
            return False 
        cont = 0
    return True

print(matriz)

print(is_basis(matriz))    
