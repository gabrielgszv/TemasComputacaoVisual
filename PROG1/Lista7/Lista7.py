import csv
import matplotlib.pyplot as plt

#1 Questão

#----------------------------------------

#Criar um arquivo com 1000 pontos

with open('pontos.txt','w') as f:
    for i in range(0,1000):
        x = -3/2 + i * 3/999
        y = x**8 - 3*x**4 + 2*x**3 - 2*x**2 - x + 2
        f.write(f'{x}, {y}\n')

#Ler os 1000 pontos
      
vx = []
vy = []

with open('pontos.txt') as f:
    reader = csv.reader(f,delimiter=',')
    for i in reader:
        vx.append(float(i[0]))
        vy.append(float(i[1]))

#Construir o gráfico

plt.plot(vx,vy)
plt.show()

#----------------------------------------

#2 Questão

#----------------------------------------

def merge_intervals(lista):
    listac = lista
    for i in listac:
        for j in listac:
            if j[0] > i[0] and j[0] <= i[1]:
                if j[1] > i[1]:
                    l = [i[0], j[1]]
                else:
                    l = [i[0], i[1]]
                listac.remove(j)
                indice = listac.index(i)
                listac[indice] = l
                
              
    return listac 

#----------------------------------------

#3 Questão

#----------------------------------------

def missing_int(nums):
    tamanho = len(nums) -1
    comeco = 0
    final = tamanho
    while comeco < final:
       meio = (comeco + final) // 2
       if nums[meio] > meio + nums[0]:
           final = meio
       else:
           comeco = meio + 1
    return comeco + nums[0]

#----------------------------------------

#4 Questão

#----------------------------------------

#Lista encadeada da Lista 6 Questão 3

class List_Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linked_List:
    def __init__(self, head = None):
        self.head = head
        self.length = 0
        pointer = self.head
        while pointer is not None:
            self.length += 1
            pointer = pointer.next
    
#Aproveitando a função inverte ordem da Lista 5 Questão 1
                
    def inverte_ordem(self):
        newList = Linked_List()
        atual = self.head

        while atual:
            novo_no = List_Node(atual.val)
            if newList.head is None:
                newList.head = novo_no
            else:
                novo_no.next = newList.head
                newList.head = novo_no
            newList.length += 1    
            atual = atual.next

        return newList

#---------------------------

'''
A ideia é receber um no e criar uma lista, criar uma segunda lista sendo o inverso da primeira,
após isso comparar de nó em nó se sao todos iguais, caso sejam todos iguais retorna True,
se tiverem algum nó diferente recebe False
'''

def is_palindrome(no):
    lista1 = Linked_List(no)
    lista2 = lista1.inverte_ordem()
    pointer1 = lista1.head
    pointer2 = lista2.head

    while pointer1 is not None:
        print(pointer1.val,pointer2.val)
        if pointer1.val != pointer2.val:
            return False
        pointer1 = pointer1.next
        pointer2 = pointer2.next
        
    return True

#---------------------------
