import csv
import matplotlib.pyplot as plt

#1 Questão

#Criar um arquivo com 1000 pontos

def write(file):
    with open(file,'w') as f:
        for i in range(0,1000):
            x = -3/2 + i * 3/999
            y = x**8 - 3*x**4 + 2*x**3 - 2*x**2 - x + 2
            f.write(f'{x}, {y}\n')

write('texto.txt')

#Ler os 1000 pontos
      
vx = []
vy = []

with open('texto.txt') as f:
    reader = csv.reader(f,delimiter=',')
    for i in reader:
        vx.append(float(i[0]))
        vy.append(float(i[1]))

plt.plot(vx,vy)
plt.show()

#----------------------------------------

      
