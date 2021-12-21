A=7
B=4
matrix = [[0 for i in range(A)] for j in range(B)]
matrix[1]=[1]*A 
matrix[0]=[0]*A 
for i in range(2,B):
    for j in range(A):
        sum1=0
        for k in range(j,A):
            sum1+=matrix[i-1][k]
        matrix[i][j]=sum1
print(sum(matrix[B-1]))
