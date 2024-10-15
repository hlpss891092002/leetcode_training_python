from math import *
def isPalindrome(s):
        ans_list = []
        for i in s:
            if i.isalpha():
                letter = i.lower()
                ans_list.append(letter)
            if i.isnumeric():
                ans_list.append(i)
        ans = "".join(ans_list)
        last_index = len(ans) - 1
        for j in range(len(ans)):
            if j == floor(len(ans)/2) and ans[j] == ans[last_index - j]:
                return True
            if ans[j] == ans[last_index - j]:
                continue
            else:
                return False
        return True
isPalindrome("race a car")