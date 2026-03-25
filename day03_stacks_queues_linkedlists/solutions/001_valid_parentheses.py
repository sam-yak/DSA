def is_valid(s):
    matches = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char not in matches:
            stack.append(char)
        elif not stack or stack[-1] != matches[char]:
            return False
        else:
            stack.pop()
    return not stack

if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    assert is_valid("") == True
    assert is_valid("(") == False
    print("All tests passed!")
