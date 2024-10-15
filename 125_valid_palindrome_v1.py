from math import *
def isPalindrome(s):
        ans_list = []
        for i in s:
            if i.isalpha():
                letter = i.lower()
                ans_list.append(letter)
            if i.isnumeric():
                ans_list.append(i)
        last_index = len(ans_list) - 1
        for j in range(len(ans_list)):
            if j == floor(len(ans_list)/2) and ans_list[j] == ans_list[last_index - j]:
                return True
            if ans_list[j] == ans_list[last_index - j]:
                continue
            else:
                return False
        return True
isPalindrome("race a car")