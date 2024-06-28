#1 Questao

def search_insert(nums, value):
    comeco = 0
    final = len(nums) - 1
    while comeco < final:
        meio = (comeco+final)//2
        if nums[meio] == value:
            return meio
        elif nums[meio] > value:
            final = meio 
        else:
            comeco = meio
            if comeco == final - 1:
                return final 
    return comeco  
    
#---------------------------
	
#2 Questao
	
def triangulo(n):
    triangulo = []
    for i in range(n):
        if i == 0:
            triangulo.append([1])
            continue 
        u = []      
        u.append(1)        
        for k in range(len(triangulo[i-1])):         
            if k+1 < len(triangulo[i-1]):                
                u.append(triangulo[i-1][k] + triangulo[i-1][k+1])                            
        u.append(1)
        triangulo.append(u)    
    return triangulo 

#--------------------------- 
	
#3 Questão

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

    def __add__(self, otherList):
        newList = Linked_List()
        pointer1 = self.head
        pointer2 = otherList.head

        while pointer1 is not None:
            valor = pointer1.val + pointer2.val
            newNode = List_Node(valor) 
            if newList.head is None:
                newList.head = newNode 
                anterior = newList.head 
            else:
                anterior.next = newNode
                anterior = anterior.next  
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            

        return newList    

            
    def delete_node(self, value):
        pointer = self.head
        anterior = List_Node()
        if self.length == 0 or self.length == 1:
            pointer = None
        while pointer is not None:
            if pointer.val == value:
                if pointer == self.head:
                    self.head = pointer.next
                    pointer = self.head
                else:
                    anterior.next = pointer.next
                    pointer = anterior.next                    
                self.length -= 1    
            else:
                anterior = pointer
                pointer = pointer.next
                                              

#---------------------------

#4 Questão

def polinomio(poli):
    myDict = {}
    graus = []
    coeficientes = []
    for i in range(len(poli)):
        
        #Quando i é o ultimo elemento da string
        if i+1 == len(poli):
            if poli[i] not in '+-x^':
                if poli[i-1] == '-':
                    coeficientes.append(int(poli[i])*-1)
                else:
                    coeficientes.append(int(poli[i])) 
                graus.append(0) 
          
        #Quando i é um numero             
        if poli[i] not in '+-x^':
            if poli[i-1] in '+-' or poli[i+1] == 'x':
                if poli[i-1] == '-':
                    coeficientes.append(int(poli[i])*-1)
                else:
                    coeficientes.append(int(poli[i]))    
            elif poli[i-1] != '^':
                graus.append(int(poli[i]))
         
        #Quando i é igual a x       
        elif poli[i] == 'x':
            if poli[i-1] in '+-': 
                if poli[i-1] == '-':
                    coeficientes.append(-1)
                else:
                    coeficientes.append(1)
            if poli[i+1] != '^':
                graus.append(1) 
                       
        elif poli[i] == '^':
            graus.append(int(poli[i+1]))             
                              
    for i in range(len(graus)):
        myDict[graus[i]] = coeficientes[i]       

    return myDict
    
#---------------------------  

#5 Questão 

def dict_polinomio(myDict):
    valores = list(myDict.values())
    chaves = list(myDict.keys())
    polinomio = ''
    for i in range(len(valores)):
        if valores[i] != 0 and valores[i] != 1:
            if valores[i] > 0:
                polinomio += '+'   
            polinomio += str(valores[i])
        if chaves[i] > 0:
            polinomio += 'x'
            if chaves[i] != 1:
                polinomio += '^'+str(chaves[i])

    return polinomio  
    
#---------------------------      
