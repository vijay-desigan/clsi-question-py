# print(matrix)
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        row=len(matrix)
        col=len(matrix[0])
        sideLenRange=min([row,col])
        sumListBySideLen=[]
        sum_list=[]
        result=0
        for sideLen in range(1,sideLenRange+1,1):
            for start_i in range(0,(col - sideLen+1),1):
                for start_j in range(0,(row - sideLen+1),1):
                    sum=0
                    for i in range(start_i,start_i+sideLen,1):
                        for j in range(start_j,start_j+sideLen,1):               
                            sum=sum+int(matrix[j][i])                         
                    sum_list.append(sum)
                    if sum==sideLen*sideLen:
                        result=sum           
        print( result)
