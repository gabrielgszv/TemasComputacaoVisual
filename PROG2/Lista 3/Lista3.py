import numpy as np
import math

'''
Do começo ate a linha 115 é a classe Vector3D do item 3 da lista 1
'''

class Field:
    pass

class VectorSpace:
    
    def __init__(self, dim: int, field: 'Field'):
        self.dim = dim
        self._field = field
        
    def getField(self):
        return self._field
    
    def getVectorSpace(self):
        return f'dim = {self.dim!r}, field = {self._field!r}'

    def __repr__(self):
        return self.getVectorSpace()
    
    def __mul__(self, f):
        raise NotImplementedError
    
    def __rmul__(self, f):
        return self.__mul__(f)
    
    def __add__(self, v):
        raise NotImplementedError
    
#-----------------------------

class RealVector(VectorSpace):
    _field = float
    def __init__(self, dim, coord):
        super().__init__(dim, self._field)
        self.coord = coord
    

    @staticmethod
    def _builder(coord):
        raise NotImplementedError

    def __add__(self, other_vector):
        n_vector = []
        for c1, c2 in zip(self.coord, other_vector.coord):
            n_vector.append(c1+c2)
        return self._builder(n_vector)
    
    def __sub__(self, other_vector):
        n_vector = []
        for c1, c2 in zip(self.coord, other_vector.coord):
            n_vector.append(c1-c2)
        return self._builder(n_vector)

    def __mul__(self, alpha):
        n_vector = []
        for c in self.coord:
            n_vector.append(alpha*c)
        return self._builder(n_vector)
    
    def iner_prod(self, other_vector):
        res = 0
        for c1, c2 in zip(self.coord, other_vector.coord):
            res += c1*c2
        return res

    def __str__(self):
        ls = ['[']
        for c in self.coord[:-1]:
            ls += [f'{c}, ']
        ls += f'{self.coord[-1]}]'
        s =  ''.join(ls)
        return s
    
    #Norma do vetor

    def __abs__(self):
        k = 0
        for i in range(len(self.coord)):
            k += self.coord[i]**2
        return math.sqrt(k)


class Vector3D(RealVector):
    _dim = 3
    eps = np.finfo(float).eps
    def __init__(self, coord):
        if len(coord) != 3:
            raise ValueError
        super().__init__(self._dim, coord)

    def __add__(self, other_vector):
        return super().__add__(other_vector)
    
    def __sub__(self, other_vector):
        return super().__sub__(other_vector)
    
    def negative(self):
        n_vec = []
        for i in self.coord:
            n_vec.append(-i)
        return n_vec

    def __mul__(self, alpha):
        return super().__mul__(alpha)
    
    @staticmethod
    def _builder(coord):
        return Vector3D(coord)

    #-----------------------------
        
    #Questão 1

    #-----------------------------

    # =
    def __eq__(self, other):
        eps = np.finfo(float).eps
        for i in range(len(self.coord)):
            if abs(self.coord[i] - other.coord[i]) > 4 * eps:
                return False
        return True

    # <
    def __lt__(self, other):
        eps = np.finfo(float).eps
        if self == other:
            return False
        if self.__abs__() - other.__abs__() > 4 * eps:
            return False
        return True
    
    # <=
    def __le__(self, other):
        eps = np.finfo(float).eps
        if self == other:
            return True
        if self.__abs__() - other.__abs__() > 4 * eps:
            return False
        return True
    
    # >
    def __gt__(self, other):
        eps = np.finfo(float).eps
        if self == other:
            return False
        if self.__abs__() - other.__abs__() < 4 * eps:
            return False
        return True
    
    # >=
    def __ge__(self, other):
        eps = np.finfo(float).eps
        if self == other:
            return False
        if self.__abs__() - other.__abs__() < 4 * eps:
            return False
        return True
    
    def __abs__(self):
        return super().__abs__()
    
#Testes    
'''
vec1 = Vector3D([0.2, 0.4, 0.3])
vec2 = Vector3D([0.6, 0.2, 0.6])
vec3 = Vector3D([0.9, 0.1, 0.7])

vecr = Vector3D([1.7, 0.7, 1.6])

print('Vetor 1: ',vec1+vec2+vec3)
print('Vetor 2: ',vecr)
print('É igual? ', vec1+vec2+vec3 == vecr)
'''


#-----------------------------
    
#Questão 2

#-----------------------------

'''
Pelo sinal teremos 1 bit.
Para escrever um digito na base b representamos com log de b na base 2,
e como temos que a precisão é p, fica entao p * (log de b na base 2) bits.
Para o expoente e, temos que o numero total de valores é emax - emin + 1,
e a quantidade de bits é log de n na base 2, sendo n = emax - emin + 1.
Então a quantidade de bits necessaria para representar um numero de ponto flutuante,
em termos de b, p, emax e emin é a soma de tudo
1 + p * (log de b na base 2) + (log de emax - emin + 1 na base 2)

'''

#-----------------------------
    
#Questão 3

#-----------------------------
'''
O epsilon começa com valor igual a 1. Comparando o 1 com o 1 + epsilon e diminuindo o epsilon
enquanto os 2 valores forem diferentes, quando nao é mais considerado diferente entao o epsilon
é suficientemente pequeno para nao fazer diferença
'''

#Escrevendo em função de n para nao reescrever na proxima questão

def calc_eps(n):
    epsilon = n
    while n + epsilon != n:
        epsilon = epsilon/2
    epsilon *= 2
    return epsilon

print('Epsilon de 1:')
print(calc_eps(1)) 

#-----------------------------
    
#Questão 4

#-----------------------------  

print('Epsilon de 10^6:')
print(calc_eps(10**6))
print('')

'''
Vemos que o epsilon de 10^6 se torna maior que o epsilon de 1,
o que poderia impactar em possiveis erros de comparação,
ja que a correcao de um é maior que a do outro
'''

#-----------------------------
    
#Questão 5

#-----------------------------  

'''
Criaria uma classe numérica que trataria essas medidas separadas,
como por exemplo, ao criar uma instancia informar que um espaco tem km == 10 e mm = 45,
assim essas medidas poderiam ser utilizadas em um unico lugar,
mas ao mesmo tempo essas mediddas estariam "separadas" para melhor tratamento,
assim evitando erros de medidas muito pequenas com muito grandes.
Como por exemplo no codigo abaixo:
'''

class ClasseNumerica:
    def __init__(self, km = 0, mm = 0):
        self.km = km 
        self.mm = mm
        

    def __str__(self):
        return f'{self.km} km e {self.mm} mm'
    

med1 = ClasseNumerica(50)
med2 = ClasseNumerica(23,6)
print(med1)
print(med2)
