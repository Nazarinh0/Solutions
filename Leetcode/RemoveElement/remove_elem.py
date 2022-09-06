def remove_element(nums, val):
    nums[:] = list(filter(lambda x: x != val, nums))


nums = [3,2,2,3]
value = 3

remove_element(nums, value)
print(nums)
