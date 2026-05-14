def combination_sum(candidates, target):
    result = []
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()
    backtrack(0, [], target)
    return result

if __name__ == "__main__":
    result = combination_sum([2, 3, 6, 7], 7)
    assert len(result) == 2
    assert [2, 2, 3] in result
    assert [7] in result
    print("All tests passed!")
