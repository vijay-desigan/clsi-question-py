arr=[-4,3,-9,0,1]
zero=0
posetive=0
negative=0
total=len(arr)
for i in arr:
    if i==0:
        zero+=1
    elif i<0:
        negative+=1
    elif i>0:
        posetive+=1
print(round(posetive/total))
print(round(negative/total))
print(round(zero/total))