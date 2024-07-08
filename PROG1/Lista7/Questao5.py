import Vector3D as V

Vetor1 = V.Vector3D([3,6,7])
Vetor2 = V.Vector3D([3,2,1])

#Funcao de produto escalar entre dois vetores

def produtoEscalar(v1: V.Vector3D, v2: V.Vector3D):
    result = 0
    for i in range(len(v1.val)):
        result += v1.val[i] * v2.val[i]
    return result

print(produtoEscalar(Vetor1,Vetor2)) 
