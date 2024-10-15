from math import *
# two point
def isPalindrome(s):
        s = [i for i in s.lower() if i.isalnum()]
        i, j = 0, len(s) - 1
        while i < j:
                if s[i] == s[j]:
                        i += 1
                        j -= 1
                        continue
                else :
                        return False
        return True
isPalindrome("race a car")