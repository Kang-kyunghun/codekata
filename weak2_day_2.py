def more_than_half(nums):


    set_list = list(set(nums))  

    for number in set_list:
        if nums.count(number) >=len(nums) / 2:
            return number
  


nums = [2,2,2,3,3,3,3]
print(more_than_half(nums))