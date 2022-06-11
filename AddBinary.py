# Given two binary strings a and b, return their sum as a binary string.
 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        result=[]
        i=len(a)-1
        j=len(b)-1
        
        while i>=0 or j>=0 or carry:
            total=carry
            
            if i>=0:
                total+=int(a[i])
                i-=1
            if j>=0:
                total+=int(b[j])
                j-=1
            result.append(str(total%2))
            carry=total//2
        return ''.join(reversed(result))
            
        
        
        
        
#         dec_a=0
#         dec_b=0
#         bi_s=[]
        
#         rev_a=a[::-1]
#         rev_b=b[::-1]
        
#         for i in range(len(rev_a)):
#             dec_a+=int(rev_a[i])*(2**i)
#         print(dec_a)
#         for i in range(len(rev_b)):
#             dec_b+=int(rev_b[i])*(2**i)
#         print(dec_a)
#         s=dec_a+dec_b
#         print(s)
        
#         while s>=2:
#             r=s%2
#             bi_s.append(r)
#             s=int(s/2)
     
#         bi_s.append(s)
#         print(bi_s[::-1])
#         rev_bi=bi_s[::-1]
#         str1=""
#         for i in rev_bi:
#             str1+=str(i)
#         return str1


        
