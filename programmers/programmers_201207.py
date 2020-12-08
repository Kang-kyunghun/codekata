#hash

import itertools

def solution(clothes):
    hash_table = {}
    total = 0
    for hash_input in clothes:
        try:
            hash_table[hash_input[1]].append(hash_input[0])
        except KeyError:
            hash_table[hash_input[1]] = [hash_input[0]]
    hash_values = list(hash_table.values())
    
    for count_case in range(1, len(hash_values)+1):
        result = list(itertools.combinations(hash_values, count_case))
        for i in result:
            caselist = list(itertools.product(*i))
            total += len(caselist)
    return total

def solution(clothes):
    hash_table = {}
    total = 1
    for hash_input in clothes:
        try:
            hash_table[hash_input[1]].append(hash_input[0])
        except KeyError:
            hash_table[hash_input[1]] = [hash_input[0]]

    hash_keys = list(hash_table.keys())

    for index in hash_keys:
        print(len(hash_table[index]))
        total *= (len(hash_table[index]) + 1)
    return total - 1

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))