def two_sum(nums, target):
    """Returns indices of numbers that sums into target"""
    
    result = []
    
    for i, num in enumerate(nums):
        if (target - num) in nums[i+1:]:
            result.append(nums.index(num))
            result.append(nums.index((target - num), i + 1))
            break
    return result


nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))
