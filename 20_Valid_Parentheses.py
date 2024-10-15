def test(s) :
    stack = []
    pair ={")" : "(", "]" : "[", "}" : "{"}
    for char in s:
        if char in pair.values():           
            stack.append(char)
        elif char in pair.keys() :
            if stack[-1] == pair[char]:
                stack.pop()
            else :
                return False
    return not stack


# test("(){}}{")         
# test("()[]{}")
test("([])")