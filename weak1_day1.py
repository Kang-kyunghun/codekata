# 내코드

def two_sum(nums, target):
    for index1 in range(len(nums)):
        for index2 in range(len(nums)):
            if index1 != index2:
                if nums[index1] + nums[index2] == target:
                    return index1, index2

numbers = [4, 9, 11, 14]
target = 13

print(list(two_sum(numbers, target)))



#지선님 코드

def two_sum(nums, target):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]

print(two_sum([4,9,11,14], 13))
print(two_sum([3,2,11,4], 13))