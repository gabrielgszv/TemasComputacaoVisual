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
    while cont < len(lista1) + len(lista2):
        if l1 != len(lista1) and lista1[l1] > lista2[l2]:
            newList.append(lista1[l1])
            l1 += 1
        else:
            newList.append(lista2[l2])
            l2 += 1         
        cont += 1        
    return newList    

#Exemplo:

print(decrescente([10,9,5,4,1],[8,7,5,3]))     

#----------------------------------------

#2 Questão

def questao2(N:int, K:int, Nd:list) -> int:

    return True

#To fazendo ainda
