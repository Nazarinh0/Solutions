def remove_element(nums, val):
    nums[:] = list(filter(lambda x: x != val, nums))

