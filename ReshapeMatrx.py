# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
# Example 2:


# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l=len(mat)
        l2=len(mat[0])
        
        if r*c!=l*l2:
            return mat
        
        lst=[]
        
        for i in mat:
            for j in i:
                lst.append(j)
                print(j)
        lst2=[]
        n=0
        for i in range(r):
            k=[]
            for j in range(c):
                k.append(lst[n])
                n+=1
            lst2.append(k)
        return lst2
                
        
        
        
        
        
        
