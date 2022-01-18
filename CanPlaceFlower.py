# 605. Can Place Flowers
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
        # flowerbed = [1,0,0,0,1]
        # n = 2
        count=0
        i=0
        while i<=len(flowerbed)-2:
            # print(i)
            if flowerbed[i]==1:
                 i+=2
            else:
                # i+=1
                if i==0:
                    if flowerbed[i+1]==0:
                        i+=1
                        count+=1
                    else:
                        i+=1
                else:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0 :
                        count+=1
                        i+=1
                    else:
                        i+=1

        # print(count)
        if count==n:
            return 'true' 
        else:
            return 'false'


        
