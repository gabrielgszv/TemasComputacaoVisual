import random


def generateMap(m: int, n: int, ground_water_ration = .2, water = '0', ground = '1' ):
    r = int(m*n*ground_water_ration+.5)
    newMap = [[water]*m for _ in range(n)]
    coord = [(i, j) for i in range(n) for j in range(m)]
    random.shuffle(coord)
    for i, j in coord[:r]:
        newMap[i][j] = ground
    return newMap

def save_map(map_s, path = 'new_map.txt'):
    with open(path, 'wt') as f:
        for row in map_s:
            f.write("".join(map(str, row)))
            f.write('\n')

def print_map(map_p):
    for row in map_p:
        print("".join(map(str, row)))

'''
Daqui pra traz so o codigo que ta no github,
daqui pra frente so bagunça
'''
import time
def funcaoai(seila):
    #transformar numa matriz dnv pra mexer nos bagui
    matrix = []
    with open(seila, "r") as f:
        for linha in f:
            new_line = []
            linha = linha.strip()
            for i in linha:
                new_line.append(i)
            matrix.append(new_line) 

    #Aqui a matriz ta feita so falta mexer nos negocio msm

    print(matrix)
    visitados = []
    direcoes = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direcoes = [(0, -1), (1,-1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    qilha = 0
    
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            #print(x,y,'seila')
            
            #time.sleep(1)
            def recursao(m, n):
                if (m,n) not in visitados:
                    visitados.append((m, n))
                    #print((m,n))
                    if matrix[m][n] == '1':
                        # print('é agua')
                        for p, q in direcoes:
                            if (m+p >= 0 and n+q >= 0) and (m+p < len(matrix[0]) and n+q < len(matrix)):
                                recursao(m+p, n+q)   
            if matrix[x][y] == '1' and (x,y) not in visitados:
                qilha +=1

            recursao(x,y)    

    return qilha               
    

                    



if __name__ == '__main__':
    random.seed(10012)
    m1 = generateMap(50, 10, 0.1, 'w', 'G')
    print_map(m1)

    m2 = generateMap(10, 10)
    save_map(m2, 'test_map.txt')
    print(funcaoai('test_map.txt'))


