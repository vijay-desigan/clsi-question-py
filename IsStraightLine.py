# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
#   Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        cor=coordinates
        # cor.sort()
        dx=cor[1][0]-cor[0][0]
        dy=cor[1][1]-cor[0][1]
        if dx==0:
            h=cor[1][0]
            for i in cor:
                if i[0]==h:
                    pass
                else:
                    return False
            return True
        slope=dy/dx
        
        for i in range(len(cor)-1):
            x=cor[i+1][0]-cor[i][0]
            y=cor[i+1][1]-cor[i][1]
            if x==0:
                return False
            if y/x==slope:
                pass
            else:
                return False
        return True
