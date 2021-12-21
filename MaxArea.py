class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                if min(height[i],height[j])*(j-i)>=area:
                    area=min(height[i],height[j])*(j-i)
                    # print(area)
        return area
                
                
        
