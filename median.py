# median of an array on numbers

arr=[5,3,1,2,4]

arr.sort()

if len(arr)%2!=0:
    ind=int((len(arr)-1)/2)
    print(arr[ind])
else:
    ind1= len(arr)/2
    ind2=len(arr)/2-1
    median=(arr[ind1]+arr[ind2])/2
    print(median)

