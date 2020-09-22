def solution(N):
    value = N
    binary = []
    while value > 0 :
        binary.append(value%2)
        value = value // 2
    binary = binary[::-1]
    i = 0
    
    zero_list = []
    while i <len(binary):
        if binary[i] == 1:
            zero = 0
            i = i + 1
            while i<len(binary):
                if binary[i] == 0:
                    zero += 1
                    i = i + 1
                else:
                    zero_list.append(zero)
                    break
        return max(zero_list) if zero_list else 0   
N =32
print(solution(N))


'''
모법답안
def solution(N):
  binaryNumber = format(N, 'b')
  maximum = 0
  binaryNumberList = binaryNumber.strip('0').split('1')
  
  for x in binaryNumberList:
    if not x:
      continue
    if len(x) > maximum:
      maximum = len(x)
      
  return maximum
  
print(solution(3243))
'''