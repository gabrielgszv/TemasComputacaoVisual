#---------------------------------------------------------------------------------------

#Questão 1

#---------------------------------------------------------------------------------------

def find_judge(n, trust):

    #Ver o indice 0 de cada par, para saber quem confia em alguém

    pessoas_0 = set()

    for k in trust:
        pessoas_0.add(k[0])

    #Ver o indice 1 para saber quem é confiado por alguém

    pessoas_1 = set()

    for k in trust:
        pessoas_1.add(k[1])

    #Ver quem é que é confiado por alguem, mas nao confia em ninguém

    possivel_juiz = pessoas_1 - pessoas_0

    #Verificar se o possível juiz é confiado por todos
    
    for p in possivel_juiz:
        count = 0
        for i in range(1, n+1):
            m = [i, p]
            if m in trust:
                count += 1             
        if count == n-1:
            
            return p
        
    return -1            
    
#Exemplo da Questão    
t = [[1, 2], [1, 3], [2, 3]]
n = 3    
print(find_judge(n, t))
#3
t = [[1, 3], [2, 3], [3, 1]]
n = 3    
print(find_judge(n, t))
#-1
