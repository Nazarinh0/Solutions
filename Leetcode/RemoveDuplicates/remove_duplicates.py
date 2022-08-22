def remove_duplicates(nums):
    """remove the duplicates in sorted array in-place"""
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1

print(remove_duplicates([1,1,2]))
