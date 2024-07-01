class Vector3D:
    def __init__(self, val = []):
        self.val = val   

    def __add__(self, other_vector):
        result = []
        for i in range(len(self.val)):
            result.append(self.val[i] + other_vector.val[i])
        return Vector3D(result)
    
    def __mul__(self, scalar):
        result = []
        for i in range(len(self.val)):
            result.append(self.val[i] * scalar)
        return Vector3D(result)
    
    def __str__(self):
        return str(self.val)   
    
    

if __name__ == '__main__':

    v1 = Vector3D([3,2,1])
    v2 = Vector3D([5,7,3])
    print('Vetor 1: ', v1)
    print('Vetor 2: ', v2)
    print('Soma dos vetores 1 e 2: ', v1+v2)
    print('Multicação do vetor 1 por escalar 3: ', v1*3)

    
