memo = {}
def f(n):
    if n in memo:
        return memo[n]
    else:
        output = []
        ex = f(n-1)
        if len(ex) < 2:
            output.append(ex[0] + tri_numbers[n-1][0])
            output.append(ex[0] + tri_numbers[n-1][1])
        else:
            output.append(ex[0] + tri_numbers[n-1][0])
            k = 0
            for i in tri_numbers[n-1][1:-1]:
                tmp = []
                for j in ex[0+k:2+k]:
                    tmp.append(i + j)
                output.append(max(tmp[0], tmp[1]))
                k += 1
            output.append(ex[-1] + tri_numbers[n-1][-1])
        

        memo[n] = output
        return output

num = int(input(''))
tri_numbers = []
for i in range(num):
    i = [int(x) for x in input('').split()]
    tri_numbers.append(i)

memo[1] = tri_numbers[0]

print(max(f(num)))


    
   

        
