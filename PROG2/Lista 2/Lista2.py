import numpy as np

#-----------------------------

#Questao 1

#-----------------------------

class My_Array:
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
  
#-----------------------------

#Questao 2

#-----------------------------

class ToroArray(My_Array):
    def __init__(self, elements):
        super().__init__()
        for i in elements:
            self.append(i)

    def __getitem__(self, index):
        if index < 0:
            while index < 0:
                index += self.size
        else:
            index = index % (self.size)
        return self.elements[index]         



tr = ToroArray([10, 11, 12, 13, 14])
i = True
print(tr[-1])
while(i):
    print('add')
    tr.append(input())
    print(tr.elements[:toro.size])
    print(tr.size)
    print(tr.capacity)
    print(' ')
