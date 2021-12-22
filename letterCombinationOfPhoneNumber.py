import itertools
a="24"
keypad=[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
       ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r','s'],
       ['t', 'u','v'], ['w', 'x','y','z']]
# print(keypad)
inputList=[]
inputList[:0]=a
# print(inputList)
newKey=[]
for i in inputList:
    newKey.append(keypad[int(i)-2])
# print(newKey)
combi=list(itertools.product(*newKey))
# print(combi)
stringList=[]
for i in combi:
    str=''
    for j in i:
        str+=j 
    stringList.append(str)
print(stringList)
