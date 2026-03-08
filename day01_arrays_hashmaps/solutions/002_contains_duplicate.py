"""
Day 1, Problem 2: Contains Duplicate (LC 217)
https://leetcode.com/problems/contains-duplicate/

Return True if any value appears at least twice in the array.

YOUR APPROACH:
  Data structure:
  Time:
  Space:
"""

def contains_duplicate(nums):
    pass  # your code here

# TESTS
if __name__ == "__main__":
    assert contains_duplicate([1,2,3,1]) == True
    assert contains_duplicate([1,2,3,4]) == False
    assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True
    assert contains_duplicate([]) == False
    print("✅ All tests passed!")

# REFERENCE (don't look until you've tried!):
# def contains_duplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False
#
# Time: O(n)  Space: O(n)
