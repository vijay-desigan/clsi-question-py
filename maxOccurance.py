A=[ 3,1,1,2 ]
occur=int(len(A)/2)
print("occur ",occur)
maxcount=0
for i in A:
    print("count ",A.count(i))
    print("max ",maxcount)
    if A.count(i)>=occur and A.count(i)>=A.count(maxcount):
        maxcount=i 
print("max count ",maxcount)
print(type(maxcount))
