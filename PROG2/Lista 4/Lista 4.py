import random

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

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
    
  

print(balanced(tbs))

#-----------------------------

#Questão 2

#-----------------------------
import time 

class Pilha:
    def __init__(self, elements = []):
        self.elements = elements

    def pop(self):
        ran_element = random.choice(self.elements)
        print(ran_element)
        self.elements.remove(ran_element)
        return ran_element
    
    def push(self, element):
        self.elements.append(element)

pilha1 = Pilha()
list1 = []

#Adicionar 1000000 elementos na pilha

inicio = time.time()

for i in range(0,100000):
    pilha1.push(i)

fim = time.time()

final = fim - inicio
print(final)

#Adicionar 1000000 elementos na lista do python

inicio = time.time()

for i in range(0,100000):
    list1.append(i)

fim = time.time()

final = fim - inicio
print(final)

inicio = time.time()

pilha1.pop()

fim = time.time()

final = fim - inicio
print(final)

