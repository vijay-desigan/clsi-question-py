# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        
        l=0
        r=m*n-1
        
        print(l,r)
        
        while(l<=r):
            mid=int((l+r)/2)
            
            r=int(mid/n)
            c=mid%n
            
            print(r,c)
            
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                r=mid
            else:
                l=mid
        return False
        
        
        # for i in matrix:
        #     for j in i:
        #         if j==target:
        #             return True
        # return False
#         m=len(matrix)-1
#         n=len(matrix[0])-1
        
        
        
#         print(n,m)
        
#         row=None
#         for i in range(m):
#             if matrix[i][n]>=target:
#                 row=i
#                 break
#         print(row)
#         l=0
#         r=n
#         while(l<r):
#             mid=int((l+r)/2)
#             if matrix[row][mid]==target:
#                 return True
#             elif matrix[row][mid]>target:
#                 l=mid+1
#                 pass
#             elif matrix[row][mid]<target:
#                 r=mid-1
#                 pass
#         return False

                
        
                
        
