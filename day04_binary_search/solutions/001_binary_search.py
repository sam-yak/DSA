def search(nums, target):
    lo = 0 
    hi = len(nums) - 1
    while lo <= hi :
      mid = (lo + hi)//2
      if nums[mid] == target:
         return mid 
      elif nums[mid] < target :
         lo = mid +1
      else :
         hi = mid -1
    return -1

if __name__ == "__main__":
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([5], 5) == 0
    assert search([1], 2) == -1
    print("All tests passed!")
