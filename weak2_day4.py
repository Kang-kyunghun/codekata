def top_k(nums, k):
 
  count_num ={}
  set_nums = list(set(nums))
  for number in set_nums:
    count_num[nums.count(number)] = number
  print(count_num)
  sorting = sorted(list(count_num.items()), reverse=True)
  print(sorting)
  result = []
  for i in sorting[:k]:
    result.append(i[1]) 
  return result

print(top_k([3,3,3,3,2,1,1,1], 2))