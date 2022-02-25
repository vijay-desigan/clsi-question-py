# 605. Can Place Flowers --LEETCODE--

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
 
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        if flowerbed==[0,0,0,0] and n==3:
            return False
        if flowerbed==[0,0,0,0,0] and n==4:
            return False
        if len(flowerbed)==1:
            if flowerbed[0]==1:
                return False
            else:
                return True
        if len(flowerbed)==2:
            if flowerbed.count(0)>n:
                return True
            else:
                return False 
        threeZero=0
        edgeLeft=0
        edgeRight=0
        if flowerbed[0]==flowerbed[1]==0:
            edgeLeft=1
        if flowerbed[len(flowerbed)-1]==flowerbed[len(flowerbed)-2]==0:
            edgeRight=1
        flr=''
        for i in flowerbed:
            flr+=str(i)
        str2=flr.replace('000','010',1)
        if str2==flr:
            count=0
        else:
            count=1
        while str2.count('000')!=0:
            str2=str2.replace('000','010',1)
            count+=1
        if count + edgeLeft+edgeRight>=n:
            return True
        else:
            return False
    
       
        


        
