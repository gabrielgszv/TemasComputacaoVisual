#1 Questão

'''
A função começará comparando o índice 0 das 2 listas,
o que tiver o maior valor será adicionado ao newList,
e o índice da lista que teve o maior número passará para o próximo,
assim passando por todos da lista 1 de tamanho n e todos da lista 2 de tamanho m,
tendo assim a complexidade O(n+m)
'''

def decrescente(lista1, lista2):
    newList = []
    cont = 0
    l1, l2 = 0, 0
    tamanho = len(lista1) + len(lista2)
    while cont < len(lista1) + len(lista2):
        if l1 == tamanho - l2 - 1:
            print('i')
            newList.append(lista1[l1])
            break
        if l1 != len(lista1) and lista1[l1] > lista2[l2]:
            newList.append(lista1[l1])
            l1 += 1
            
        else:
            newList.append(lista2[l2])
            l2 += 1         
        cont += 1      
    return newList    

#Exemplo:

print(decrescente([10,9,5,4,1],[8,7,5,1]))     

#----------------------------------------


#2 Questão

def questao2(N:int, K:int, Nd:list) -> int:
    anteriores = []
    qtd = 0
    for i in range(N):
        if Nd[i] in anteriores:
            continue
        else:
            if len(anteriores) == K:
                anteriores.pop(0)
            anteriores.append(Nd[i])
            qtd += 1
    return qtd

print(questao2(6,2,[1,1,1,3,4,1]))

#----------------------------------------
