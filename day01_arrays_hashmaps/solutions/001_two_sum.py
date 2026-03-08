"""
Day 1, Problem 1: Two Sum (LC 1)
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

Constraints:
- Exactly one solution exists
- Can't use the same element twice
- Return indices in any order

Example:
  Input:  nums = [2,7,11,15], target = 9
  Output: [0, 1]  (because nums[0] + nums[1] = 9)

BEFORE CODING — answer these:
  1. What data structure will you use and why?
  2. What is the time complexity of your approach?
  3. What is the space complexity?
"""


# YOUR SOLUTION — try to write it without looking below
def two_sum(nums, target):
    pass  # your code here


# =========================================================
# TESTS — run these to verify your solution
# =========================================================
if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, {0, 1}),
        ([3, 2, 4], 6, {1, 2}),
        ([3, 3], 6, {0, 1}),
        ([1, 5, 3, 7, 2], 9, {1, 3}),
    ]

    for nums, target, expected in tests:
        result = two_sum(nums, target)
        assert set(result) == expected, f"FAIL: two_sum({nums}, {target}) = {result}, expected {expected}"
    print("✅ All tests passed!")


# =========================================================
# REFERENCE SOLUTION (don't look until you've tried!)
# =========================================================
# def two_sum(nums, target):
#     seen = {}  # value -> index
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i
#     return []
#
# Time:  O(n) — single pass, O(1) hash map lookups
# Space: O(n) — hash map stores up to n elements
