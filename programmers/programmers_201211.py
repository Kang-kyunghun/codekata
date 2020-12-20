def solution(n):
    if n == 2:
        return 1
    prime_numbers = []
    prime = 0
    numbers = []
    for i in range(2, n+1):
        numbers.append(i)
    while prime**2 < n:
        prime = numbers[0]
        prime_numbers.append(prime)
        for num in numbers:
            if num % prime == 0:
                numbers.remove(num)
      
    return len(prime_numbers) + len(numbers)

n = 100
print(solution(n))