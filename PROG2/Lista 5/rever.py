'''
Essa bomba funciona mas n sei como vou revisar depois
'''



import time

def seila(maze):
    start = (1, 1)  # Ponto inicial
    print_maze(maze)
    lista = []  # Lista de posições visitadas

    # Direções na ordem: esquerda, baixo, direita, cima
    direcoes = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    # Pilha para controlar a exploração do labirinto, com o caminho até cada ponto
    stack = [(start, [start])]  # Cada item é uma tupla (posição, caminho até essa posição)

    while stack:
        (x, y), path = stack.pop()

        # Se já foi visitado, pula para a próxima iteração
        if (x, y) in lista:
            continue
        
        # Marca como visitado
        lista.append((x, y))
        print(x, y)
        print_maze(maze)

        # Se encontrar o queijo, imprime o caminho e termina a busca
        if maze[x][y] == '*':
            print("Achou o queijo!")
            print("Caminho até o queijo:", path)
            for k in path:
                xs, ys = k
                maze[xs][ys] = '-'
                print_maze(maze)
            return path  # Retorna o caminho até o queijo

        # Adiciona as direções à pilha (esquerda, baixo, direita, cima)
        for dx, dy in direcoes:
            xn, yn = x + dx, y + dy
            # Verifica se está dentro dos limites do labirinto e não é uma parede
            if 0 <= xn < len(maze) and 0 <= yn < len(maze[0]) and maze[xn][yn] != 'H':
                # Adiciona a nova posição e o caminho atualizado à pilha
                stack.append(((xn, yn), path + [(xn, yn)]))
    
    print("Queijo não encontrado.")
    return None

# Exemplo de uso
if __name__ == '__main__':
    random.seed(10110)    
    m, n = 5, 7
    room = ' '
    wall = 'H'
    cheese = '*'
    maze = generate_maze(m, n, room, wall, cheese)
    print('\nMaze 2')
    seila(maze)
