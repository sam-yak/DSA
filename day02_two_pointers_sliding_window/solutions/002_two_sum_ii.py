def two_sum_ii(numbers, target):
    left = 0 
    right = len(numbers) - 1
    while left < right :
          total = numbers[left]+numbers[right]
          if total == target:
             return [left+1, right+1]
          elif total > target:
             right -=1
          elif total< target:
             left +=1
    return []
if __name__ == "__main__":
    assert two_sum_ii([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_ii([2, 3, 4], 6) == [1, 3]
    assert two_sum_ii([-1, 0], -1) == [1, 2]
    print("All tests passed!")
