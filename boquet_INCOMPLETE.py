bloomDay = [7,7,7,7,12,7,7]
# A=bloomDay
m = 2
k = 3
total_flowers=m*k
last_flower=0
days=[]
bloomed=[]
if total_flowers>len(bloomDay):
    print(-1)
# for i in range(total_flowers):
#     last_flower=min(bloomDay)
#     bloomDay.remove(last_flower)
for i in bloomDay:
    if days.count(i)==0:
        days.append(i)
print(days)
for i in days:
    print("bloomDay ",bloomDay)
    A=[]
    for j in range(len(bloomDay)):
        print("A[j]= ",bloomDay[j])
        if bloomDay[j]<=i:
            A.append("x")
        else:
            A.append("_")
    print(A)
    bloomed.append(A)
    print(bloomed)
print(bloomed)
for i in bloomed:
    while True:
        j=0
        
            
    
    

