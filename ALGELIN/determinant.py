def determinant(A):
   
    u = A
    det = 1

    for i in range(len(u)):
        for c in range(len(u[0])):

            if u[i][c] == 0 and i==c:
                
                #1
                for k in range(len(u)):
                    if u[k][c] != 0:
                        break
                    if k == len(u) - 1:
                        return 0

                for k in range(len(u)):
                    if k == 0:
                        continue
                    #2
                    if u[c+k][i] != 0:
                        u[c], u[c+k] = u[c+k], u[c]
                        det *= -1
                        break
                    
                break        

            if c < i and u[c][i] != 0:
                divisor = u[i][c]/u[c][c] 
                for w in range(len(u[i])):
                    u[i][w] = u[i][w] - divisor * u[c][w]

    for i in range(len(u)):
        det *= u[i][i]
    return det   
