"""
Day 1, Problem 3: Valid Anagram (LC 242)
https://leetcode.com/problems/valid-anagram/

Return True if t is an anagram of s.

YOUR APPROACH:
  Data structure:
  Time:
  Space:
"""

def is_anagram(s, t):
    pass  # your code here

# TESTS
if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("", "") == True
    assert is_anagram("a", "ab") == False
    print("✅ All tests passed!")

# REFERENCE:
# from collections import Counter
# def is_anagram(s, t):
#     return Counter(s) == Counter(t)
#
# Time: O(n)  Space: O(1) — at most 26 chars
