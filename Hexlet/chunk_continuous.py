def summary_ranges(nums):
    
    if len(nums) < 2:
        return []
    
    start_index = 0
    result = []
    
    for i in range(len(nums)):
        if i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
            continue
        if start_index != i:
            result.append(str(nums[start_index]) + "->" + str(nums[i]))
        start_index = i + 1

    return result


print(summary_ranges([1,2,3,4,5,6,10,13,14,15,9]))
