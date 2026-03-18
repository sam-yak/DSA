def three_sum(nums):
    nums.sort()
    n=len(nums)
    result=[]
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]:
           continue
        left= i+1
        right = n-1
        target =-nums[i]
        while left<right:
              value_sum = nums[left]+nums[right]
              if value_sum == target:
                 result.append([nums[i], nums[left], nums[right]])
                 while left<right and nums[left]==nums[left+1]:
                       left +=1
                 while left<right and nums[right]==nums[right-1]:
                       right -=1
                 left +=1
                 right -=1
              elif value_sum > target:
                   right -=1
              else:
                   left +=1
    return result
                   
                   

if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([0, 1, 1]) == []
    print("All tests passed!")
