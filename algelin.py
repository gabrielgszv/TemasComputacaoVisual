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

def um(linha, divisor):
    result = []
    for i in range(len(linha)):
        result.append(linha[i]/divisor)
    return result

def elementar(linha, divisor,linha2):
    result = []
    for i in range(len(linha)):
        linha[i] = linha[i] - divisor * linha2[i]
        result.append(linha[i])


    return result 

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

def gaussiana(matriz):
    a = matriz
    p = identidade(matriz)
    l = identidade(matriz)
    iden = identidade(matriz)
    u = matriz

    coluna = len(u[0])
    linha = len(u)

    for i in range(linha):
        for c in range(coluna):
            
            #pra funcionar com numero de coluna maior que o de linha

            if c > linha -1:
                break
            print(i,c)
            if u[i][c] == 0 and i==c:
                if i == linha -1 and c == coluna-1:
                    break
                u[c], u[c+1] = u[c+1], u[c]
                p[c],p[c+1] = p[c+1], p[c]



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





    print(p)
    print(l)
    print(u)
       
       
   

                       
            
                      




salve = [[1,2,2],
         [3,2,9],
         [2,3,5]
]

gaussiana(salve)
