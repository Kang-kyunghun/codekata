def search(num, target):
    left_index = 0
    right_index = len(num) - 1
    while True:
        if target < num[0] or target > num[-1]:
            return -1
        
        target_index = (left_index + right_index) // 2 
        if left_index == target_index:
            return len(num) - 1
        if num[target_index] == target:
            return target_index
        elif num[target_index] > target:
            right_index = target_index
        else:
            left_index = target_index
        

num = [-1,0,3,5,9,12,13]
target = 13

print(search(num, target))