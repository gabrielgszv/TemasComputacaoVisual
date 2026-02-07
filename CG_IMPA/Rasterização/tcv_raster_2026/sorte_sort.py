import random
import time
def sorte_sort(lista):

    n_lista = random.sample(lista, len(lista))
    t_inicio = time.time()
    while True:
        k = 0

        for i in range(len(lista)-1):
            if n_lista[i] <= n_lista[i+1]:
                k += 1

        if k == len(lista)-1:
            break

        n_lista = random.sample(lista, len(lista))

    t_final = time.time()
    print(f"Tempo para ordenação {(t_final-t_inicio):.2f} s.")
    return n_lista

lista = [13,5,4113,11,13,2,0,3,56,7,8]

ordenada = sorte_sort(lista)

print(ordenada)