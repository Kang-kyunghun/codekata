def moveZeroes(nums):
  zero = nums.count(0)
  count = 0
  i = 0
  while count < zero:
    if nums[i] == 0:
      nums.append(nums.pop(i))
      count += 1
    else:
      i += 1
  return nums


nums = [0,1,0,3,12]
print(moveZeroes(nums))