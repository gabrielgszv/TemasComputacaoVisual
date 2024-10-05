import random
import numpy as np
import scipy


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

#Função do Emílio para criar árvores de busca binaria

#---------------------------------------------------------------------------------------

# Function to create a BST from a list of nodes
def create_tree(nodes):
    if not nodes:  # Handle edge case when nodes list is empty
        return None
    
    root = TreeNode(nodes[0])
    
    def insert_node(root, value):
        current_node = root
        while current_node:
            if value < current_node.val:
                if current_node.left is None:
                    current_node.left = TreeNode(value)
                    break
                current_node = current_node.left
            elif value > current_node.val:
                if current_node.right is None:
                    current_node.right = TreeNode(value)
                    break
                current_node = current_node.right
            else:
                # Duplicate value found, return None to indicate an error
                print(f"Duplicate value {value} found. BST cannot have duplicate values.")
                return None
        return root

    for n in nodes[1:]:
        if insert_node(root, n) is None:
            return None  # Return None if a duplicate is found
    
    return root

# Create a BST and populate it with values
tbs = create_tree([128, 64, 256, 32, 96, 80, 112, 512, 384])

# Simple function to print the tree in-order (for testing purposes)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        # print(node.val, end=" ")
        inorder_traversal(node.right)

# Test the tree structure
inorder_traversal(tbs)

#---------------------------------------------------------------------------------------

#-----------------------------

#Questão 1

#-----------------------------


'''
A função height() verifica a altura de cada nó passando por cada um desde a raiz da árvore.
Assim a função balanced() passa por cada nó e verifica o tamanho do nó da esquerda e da direita,
caso a diferença de tamanho seja maior que 1, a funçao retorna False, caso passe por todos os elementos
e nao ache uma diferença maior que 1, entao retorna True

'''

def height(x):
    if x is None:
        return 0
    height_esq = height(x.left)
    height_dir = height(x.right)
    return max(height_esq, height_dir) + 1


def balanced(tree):
    if tree is None:
        return True
    height_left = height(tree.left)
    height_right = height(tree.right)
    if abs(height_left - height_right) > 1:
        return False
    
    return balanced(tree.left) and balanced(tree.right)

#-----------------------------

#Questão 2

#-----------------------------
import time 

class Pilha:
    def __init__(self, elements = []):
        self.elements = elements

    '''
    Como para remover o ultimo elemento de uma lista, metodo pop do python tem complexidade O(1) que é constante,
    aproveitando disso essa função escolhe um indice aleatorio e troca ele para colocar no ultimo elemento,
    assim usando o metodo pop para remover e ter tempo constante.
    '''    

    def pop(self):
        random_index = random.randint(0, len(self.elements) - 1)
        element = self.elements[random_index]
        self.elements[random_index], self.elements[-1] = self.elements[-1], self.elements[random_index]
        self.elements.pop()
        return element
    
    def push(self, element):
        self.elements.append(element)

pilha1 = Pilha()
list1 = []

#Adicionar 1000000 elementos na pilha

inicio = time.time()

for i in range(1000000):
    pilha1.push(i)

fim = time.time()

final = fim - inicio
print(final)

#Adicionar 1000000 elementos na lista do python

inicio = time.time()

for i in range(1000000):
    list1.append(i)

fim = time.time()

final = fim - inicio
print(final)
'''
tempo do pop
'''
for i in range(3):
        
    inicio = time.time()

    pilha1.pop()

    fim = time.time()

    final = fim - inicio
    print(final)

#-----------------------------

#Questão 4

#-----------------------------

'''
Para as distribuições uniforme e normal, a biblioteca random ja tem as funções,
e para a distribuição student t, a biblioteca scipy tem a função.
A função recebe o número de pontos e o tipo de distribuição de x e y separadamente
'''

def uniforme(N):
    k = np.random.uniform(-1, 1 ,N)
    return k

def normal(N):
    k = np.random.normal(0, 0.5, N)
    return k

def student_t(N):
    k = scipy.stats.t.rvs(df=2, size=N) * 0.5
    return k

def sorteio(N, tx ,ty):
    x = tx(N)
    y = ty(N)
    return np.column_stack((x, y))

pontoos = sorteio(10, normal, student_t)

#-----------------------------

#Questão 5

#-----------------------------

def fecho_convexo(pontos):
    fecho = scipy.spatial.ConvexHull(pontos)
    '''
    Fecho é um obejto da classe ConvexHull, que tem atributos como esse usado no retorno,
    que tem o indice dos vertices do poligono convexo
    '''
    return pontos[fecho.vertices]
