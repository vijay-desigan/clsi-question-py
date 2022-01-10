# 1616. Split Two Strings to Make Palindrome
# You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

# When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

# Return true if it is possible to form a palindrome string, otherwise return false.

# Notice that x + y denotes the concatenation of strings x and y.

# Example 1:

# Input: a = "x", b = "y"
# Output: true
# Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
# aprefix = "", asuffix = "x"
# bprefix = "", bsuffix = "y"
# Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
# Example 2:

# Input: a = "xbdef", b = "xecab"
# Output: false
# Example 3:

# Input: a = "ulacfd", b = "jizalu"
# Output: true
# Explaination: Split them at index 3:
# aprefix = "ula", asuffix = "cfd"
# bprefix = "jiz", bsuffix = "alu"
# Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.

a="ulacfd"
b="jizalu"
aplusb=""
def isPalin(s):
    temp=s[::-1]
    if s==temp:
        return 1
    else:
        return 0
if isPalin(a) or isPalin(b):
    print("True")
t1=b[::-1]
i=0
count=0
while i<len(a):
    if a[i]==t1[i]:
        count+=1
        i+=1
    else :
        i+=1
for i in range(count):
    aplusb=aplusb+a[i]
for i in range(count,len(b)):
    aplusb=aplusb+b[i]
if isPalin(aplusb):
    print("True")
t2=b
i=0
count=0
while i<len(a):
    if a[i]==t2[i]:
        count+=1
        i+=1
    else :
        i+=1
for i in range(count):
    aplusb=aplusb+a[i]
for i in range(count,len(b)):
    aplusb=aplusb+b[i]
if isPalin(aplusb):
    print("True")
