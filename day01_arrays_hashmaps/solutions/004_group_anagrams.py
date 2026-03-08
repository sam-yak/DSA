"""
Day 1, Problem 4: Group Anagrams (LC 49)
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group the anagrams together.

YOUR APPROACH:
  Key insight — what makes a good hash map key for anagrams?
  Time:
  Space:
"""

def group_anagrams(strs):
    pass  # your code here

# TESTS
if __name__ == "__main__":
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    result_sorted = sorted([sorted(g) for g in result])
    expected = sorted([sorted(g) for g in [["eat","tea","ate"],["tan","nat"],["bat"]]])
    assert result_sorted == expected, f"Got {result_sorted}"
    print("✅ All tests passed!")

# REFERENCE:
# from collections import defaultdict
# def group_anagrams(strs):
#     groups = defaultdict(list)
#     for s in strs:
#         key = tuple(sorted(s))
#         groups[key].append(s)
#     return list(groups.values())
#
# Time: O(n * k log k) where k = max string length
# Space: O(n * k)
