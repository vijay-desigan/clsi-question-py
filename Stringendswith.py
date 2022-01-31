# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    if ending=="":
        return True
    if len(ending)>len(string):
        return False
    if len(string)-string.rindex(ending)==len(ending):
        return True
    else :
        return False
    
