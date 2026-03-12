def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, {0, 1}),
        ([3, 2, 4], 6, {1, 2}),
        ([3, 3], 6, {0, 1}),
        ([4, 5, 11, 3], 8, {1, 3}),
    ]
    for nums, target, expected in tests:
        result = two_sum(nums, target)
        assert set(result) == expected, f"FAIL: two_sum({nums}, {target}) = {result}"
    print("All tests passed!")
