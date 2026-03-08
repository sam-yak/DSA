"""
Day 1, Problem 6: Product of Array Except Self (LC 238)
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array where answer[i] is the product
of all elements EXCEPT nums[i]. You must do it WITHOUT using division.

Follow-up: Can you solve it in O(1) extra space? (output array doesn't count)

Example: [1,2,3,4] -> [24,12,8,6]

YOUR APPROACH:
  What are prefix and suffix products?
  How can you build the answer in two passes?
  Time:
  Space:
"""

def product_except_self(nums):
    pass  # your code here

# TESTS
if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([2, 3]) == [3, 2]
    print("✅ All tests passed!")

# REFERENCE:
# def product_except_self(nums):
#     n = len(nums)
#     answer = [1] * n
#
#     # Pass 1: left products (prefix)
#     left_product = 1
#     for i in range(n):
#         answer[i] = left_product
#         left_product *= nums[i]
#
#     # Pass 2: right products (suffix), multiply into answer
#     right_product = 1
#     for i in range(n - 1, -1, -1):
#         answer[i] *= right_product
#         right_product *= nums[i]
#
#     return answer
#
# Time:  O(n) — two passes
# Space: O(1) extra — output array doesn't count
