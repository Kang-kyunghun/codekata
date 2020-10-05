def selectionSort(nums):
    for nums_index in range(len(nums)):
        min_value = nums[nums_index]
        for i  in range(nums_index, len(nums)):
            min_value = min(min_value, nums[i])
        min_index = nums.index(min_value)
        nums[nums_index], nums[min_index] = nums[min_index] , nums[nums_index] 
    return nums

nums = [7, 4, 5, 2]

print(selectionSort(nums))