def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("aa") == True
    print("All tests passed!")
