# Given an array(0-based indexing), you have to find the max sum of i*A[i] where A[i] is the element at index i in the array. 
# The only operation allowed is to rotate(clock-wise or counter clock-wise) the array any number of times.
# Input:
# N = 4
# A[] = {8,3,1,2}
# Output: 29
# Explanation: Above the configuration
# possible by rotating elements are
# 3 1 2 8 here sum is 3*0+1*1+2*2+8*3 = 29
# 1 2 8 3 here sum is 1*0+2*1+8*2+3*3 = 27
# 2 8 3 1 here sum is 2*0+8*1+3*2+1*3 = 17
# 8 3 1 2 here sum is 8*0+3*1+1*2+2*3 = 11
# Here the max sum is 29 

def max_sum(a,n):
    arr=[]
    for i in a:
        arr.append(i)
    for i in a:
        arr.append(i)
    max_sum=0
    # check sum
    
    for i in range(n):
        s=0
        new_arr=[]
        for k in range(i,i+n):
            new_arr.append(arr[k])
        # print("new arr ",new_arr)
        for j in range(n):
            s+=j*new_arr[j]
        # print(s)
        if s>max_sum:
            max_sum=s
    return max_sum
