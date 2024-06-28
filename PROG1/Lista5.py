#Questao 1

#---------------------------------------------------

#Criacao da lista encadeada

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, v):
        no = Node(v)
        if self.head is not None:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = no   
        else:
            self.head = no

    #Função da Questao 1
            
    def inverte_ordem(self):
        anterior = None
        atual = self.head
        while atual is not None:
            n = atual.next
            atual.next = anterior
            anterior = atual
            atual = n
        self.head = anterior 
        
    #A complexidade desse código é O(N)          
                            
#---------------------------------------------------

#Questao 2

#---------------------------------------------------

def romanos(num: int):
    
    #Declaraçâo das variáveis
    
    n = num
    result = []
    algarismos = {
    	1000: 'M',
    	500: 'D',
    	100: 'C',
    	50: 'L',
    	10: 'X',
    	5: 'V',
    	1: 'I'
    	}
    	
    i=0
    	
    for chave in algarismos:
        i+= 1
        
        '''
        Esse if e else serve para ver o proximo e o anterior de cada numero,
        já que o próximo do número de indice impar é 5 vezes maior que ele e o anterior é a metade,
        o mesmo raciocinio serve para o numero de indice par, so que o contrário dos valores
        '''

        if i % 2 == 0:
            anterior = chave/5
            proximo = chave*2
            p = proximo * 0.9
            f = anterior
        else:
            anterior = chave/2
            proximo = chave*5
            p = proximo * 0.8
            f = chave  
            
        while(n >= chave):
            
            '''
            Esse if e else verificará se o número esta entre o numero e 0.9 ou 0.8 vezes o proximo numero,
            dependendo do indice, para definir números como 9 que é IX ou o número 90 que é XC
            '''
            
            if n >= p:
                result += algarismos[f] + algarismos[proximo]
                n -= proximo - f
            else:
                n -= chave
                result += algarismos[chave]            
            
    final = ''
    for i in result:
        final += i
    
    return final   

#---------------------------------------------------

#Questao 3

#---------------------------------------------------

def potencia(x: float, n: int):
    r = 1
    for i in range(n):
        r *= x
    return r

#---------------------------------------------------

#Questao 4

#---------------------------------------------------

def elemento_unico(lista):
    
    soma_lista = sum(lista)
    unicos = set(lista)
    soma_unicos = sum(unicos)
    result = 2 * soma_unicos - soma_lista
    return result

#---------------------------------------------------

#Questão 5

#---------------------------------------------------

def longest_common_prefix(lista):
    result=''
    
    #Verificar o tamanho da menor palavra da lista
    
    tamanho = len(lista[0])
    for i in lista:
        if len(i) < tamanho:
            tamanho = len(i)    
            
    while tamanho > 0:
        prefixo = lista[0][:tamanho]
        
        '''
        Essa repetição irá comparar as n primeiras letras de todas as palavras da lista,
        caso encontre uma palavra com as n primeiras letras diferentes haverá um break e passara para as n-1 primeiras letras,
        quando verificar que as n primeiras letras são iguais a repetição é parada e o prefixo recebe as n primeiras letras
        '''
                        
        for n in range(len(lista)):
            if lista[n][:tamanho] == prefixo:
                pass
            else:
                tamanho -= 1
                break
            if n+1 == len(lista):
                result = prefixo
                
            
        if result != '':
            break                     
    return result 
    
#A complexidade desse codigo é O(n*m), em que n é o numero de palavras e m é o numero de letras da menor palavra       
    
#---------------------------------------------------    
            
