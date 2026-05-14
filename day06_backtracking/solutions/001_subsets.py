def subsets(nums):
    result = []
    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result

if __name__ == "__main__":
    result = subsets([1, 2, 3])
    assert len(result) == 8
    assert [] in result
    assert [1, 2, 3] in result
    assert [1, 2] in result
    assert [2, 3] in result
    print("All tests passed!")
