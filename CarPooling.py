# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# Example 2:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        length=0
        for i in trips:
            if i[2]>length:
                length=i[2]+1
        route=[]
        for i in range(length):
            route.append(0)

        for i in trips:
            for j in range(i[1],i[2]):
                route[j]+=i[0]
        for i in route:
            if i>capacity:
                return False
        return True  
