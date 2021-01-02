# def solution(a, b):
#     answer = str(a**b)[-5:]

#     return int(answer)



memo ={0:1}
def power(x, y):
    if y in memo.keys():
        return memo[y]
    else:
        semi_result = power(x, y // 2)

        if y % 2 == 0:
            output = semi_result * semi_result
        else:
            output = x * semi_result * semi_result

        memo[y] = output
        return output 

a = 123456789
b = 12345

p = power(a,b)

print(str(p)[-5:])


