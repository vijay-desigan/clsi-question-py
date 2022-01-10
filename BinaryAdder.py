# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bia=a[::-1]
        bib=b[::-1]
        inta=0
        intb=0
        for i in range(len(bia)):
            inta+=int(bia[i])*(2**i)

        for i in range(len(bib)):
            intb+=int(bib[i])*(2**i)

        val=inta+intb
        if val==0:
            return "0"
        rev=''
        while val>=1:
            rem=val%2
            rev=str(rem)+rev
            val=int(val/2)
        return rev
