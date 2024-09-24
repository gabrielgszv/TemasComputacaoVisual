import time

import numpy as np

#-----------------------------
    
#Questão 1

#-----------------------------

class My_Array():
    def __init__(self):
        self.elements = np.empty(1)
        self.size = 0   
        self.capacity = 1

    def append(self, element):
        if self.size >= self.capacity:
            self.capacity = 2 * self.capacity
            new_elements = np.empty(self.capacity)
            new_elements[:self.size] = self.elements[:self.size]
            self.elements = new_elements
        self.elements[self.size] = element
        self.size += 1 

#Comparando o My_Array com a lista do python


Marray = My_Array()
lista = []

inicio = time.time()
for i in range(1000):
    Marray.append(i)
fim = time.time()
print(f"Tempo de execução do My_Array: {fim - inicio}")

inicio = time.time()
for i in range(1000):
    lista.append(i)
fim = time.time()
print(f"Tempo de execução da Lista: {fim - inicio}")


#Rodando vemos que a Lista é mais eficiente

#-----------------------------
    
#Questão 2

#-----------------------------

class ToroArray(np.ndarray):

    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)  # Convert the input array and create a view as this class
        return obj

    def __init__(self, inputArray):
        self.dim = np.prod(self.shape)  # Calculate and store the product of dimensions of the array

    def __getitem__(self, index):
        index = index % (self.dim)
        return self.item(index)         

#Exemplo da questão 2:
'''
toro = ToroArray([10, 11, 12, 13, 14])
print(toro[6])
print(toro[-20])
'''
#-----------------------------
    
#Questão 3

#-----------------------------


'''
    Temos que n² + 1000n = O(n²). Pela definição:
n² + 1000n <= c * n²
Dividindo os 2 lados por N²:
1 + 1000/n <= c
Observamos que, quanto mais n cresce, 1000/n diminui, o que implica que 1 + 1000/n será menor ou igual a uma constante c.
Escolhendo N = 1, temos que achar um c para que todo n >= N satisfaça a desigualdade, então:
c = 1 + 1000/1 = 1001

Tomando c = 1001, teremos que:
1 + 1000/n <= 1001 que é verdade para qualquer n.
Entao teremos N = 1 e c = 1001

Agora tomando os valores da questão:
c = 2 e N = 1000:

1 + 1000/n <= c
1 + 1000/1000 <= 2 -----> 1 + 1 <= 2
que é verdade, quanto mais n cresce menor o numero 1000/n vai ser, assim nunca sendo maior que 2,
analogamente será para os proximos valores

c = 101 e N = 10:

1 + 1000/10 <= 101 -----> 1 + 100 <= 101
entao podemos tomar esses valores

c = 1001 e N = 1:

1 + 1000/1 <= 1001 -----> 1 + 1000 <= 1001
entao podemos tomar esses valores

'''

#-----------------------------
    
#Questão 4

#-----------------------------

'''
Ida
    Pela definição temos que g é O(f) quando existe N e c tal que g(n) <= cf(n) para todo n >= N.
entao cf(n) >= g(n), dividindo os 2 lados por c: f(n) >= 1/c * g(n).
Como 1/c é constante fica f(n) >= c2 * g(n), que é a definicao de quando f é Omega(g).

Volta
    Analogamente a ida, pela definição f é Omega(g) quando f(n) >= cg(n).
dividindo os 2 lados por c: f(n) * 1/c >= g(n).
em que 1/c é constante, entao: f(n) * c >= g(n) que é quando g é O(f)  
    
'''

#-----------------------------
    
#Questão 5

#-----------------------------

'''
Ida
    Como g é Theta(f), que é quando g é O(f) e g é Omega(f), temos:
g(n) <= c1 * f(n) e g(n) >= c2 * f(n), entao c2 * f(n) <= g(n) <= c1 * f(n).
dividindo por f(n): c2 <= g(n) / f(n) <= c1
invertendo: 1/c2 <= f(n) / g(n) <= 1/c1
multiplicando por g(n): g(n) * 1/c2 <= f(n) <= g(n) * 1/c1
Como 1/c1 e 1/c2 sao constantes podemos chamar de c3 e c4:
g(n) c4 <= f(n) <= g(n) * c3
que é a definicao de quando f é Theta(g)

Volta
    É analogo, mudando apenas que começa com o f sendo Theta(g)

'''

