class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        g.sort()
        s.sort()
        for i in g:
            for j in s:
                if j>=i:
                    count+=1
                    s.remove(j)
                    break
        return count
                    
                    
