# 1288. Remove Covered Intervals LEETCODE
# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

# Return the number of remaining intervals.

 

# Example 1:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
                                                
# Example 2:

# Input: intervals = [[1,4],[2,3]]
# Output: 1

def compare(l1,l2):
    if l2[0]<=l1[0] and l2[1]>=l1[1]:
        return l1
    elif l1[0]<=l2[0] and l1[1]>=l2[1]:
        return l2
    else:
        return 0
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        run=len(intervals)
        l=[]
        for i in range(run):
            for j in range(i+1,run):
                # try:
                # print(i,j)
                #     # print(intervals[i])
                #     # print(intervals[j])
                temp=compare(intervals[i],intervals[j])
                # print(temp)
                l.append(temp)
                # print(l)11
                # except:
                #     print("ece")
                #     pass
        for i in l:
            try:
                intervals.remove(i)
            except:
                pass
        return len(intervals)
                    
        
