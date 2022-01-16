# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to the closest person.

# Example 1:


# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.

# Example 2:

# Input: seats = [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.

# Example 3:

# Input: seats = [0,1]
# Output: 1

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # seats = [1,0,0,0,1,0,1]
        distance=[]
        length=len(seats)
        # print(length)
        for i in range(length):
            j=i+1
            k=i-1
            # print("j k ",j,k)
            left=0
            right=0
            if seats[i]==0:
                if i==length-1:
                    right=1
                else:
                    while j<length:
                        if seats[j]==1:
                            j=length+1
                            break
                        else:
                            right+=1
                            j+=1
                # print("right ",right)
                if i==0:
                    left=1
                else:
                    while k>=0:
                        if seats[k]==1:
                            k=-1
                            break
                        else:
                            left+=1
                            k-=1
                # print("left ",left)
                distance.append((left,right))
                # print(distance)
            else:
                distance.append((0,0))

            # while j<length:
            #     if seats[j]==1:
            #         j=length+1
            #         break
            #     else:
            #         right+=1
            #     j+=1
            # print("right ",right)
            # while k>=0:
            #     if seats[k]==1:
            #         k=-1
            #         break
            #     else:
            #         left+=1
            #     k-=1
            # print("left ",left)
            # distance.append((left,right))
            # print(distance)
        # print(distance)
        proDistance=[]
        for i in distance:
            proDistance.append(i[0]*i[1])
        # print(proDistance)
        return proDistance.index(max(proDistance))



        
