"""
Day 1, Problem 5: Longest Consecutive Sequence (LC 128)
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest
consecutive elements sequence. Must run in O(n) time.

Example: [100, 4, 200, 1, 3, 2] -> 4  (the sequence is [1, 2, 3, 4])

YOUR APPROACH:
  Why can't you sort? What data structure gives O(1) lookup?
  How do you avoid counting from EVERY number (which would be O(n^2))?
  Time:
  Space:
"""

def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for num in num_set:
        if num-1 not in num_set:
           length = 1
           while num + length in num_set:
                 length +=1
           best = max(best, length)
    return best

# TESTS
if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1]) == 1
    assert longest_consecutive([1, 2, 0, 1]) == 3
    print("✅ All tests passed!")

# REFERENCE:
# def longest_consecutive(nums):
#     num_set = set(nums)
#     best = 0
#     for num in num_set:
#         if num - 1 not in num_set:  # only start from sequence beginnings
#             length = 1
#             while num + length in num_set:
#                 length += 1
#             best = max(best, length)
#     return best
#
# Time: O(n) — each number visited at most twice
# Space: O(n) — the set
