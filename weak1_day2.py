def reverse(x):
    x_str   = str(x) #int을 itable하게 변형
    x_list  = list(x_str) # list method을 사용하기 위해 list로 변헝
    new_x   = []
    
    while x_list: # 뒤집기
        new_x.append(x_list.pop(-1))
    
    if len(new_x) == 1:
        return int(''.join(new_x))
    if new_x[0] == '0':
        new_x.pop(0)
    if new_x[-1] == '-' :
        new_x.insert(0, new_x.pop(-1))
  
    return int(''.join(new_x))


x = 0

print(reverse(x))

def reverse(number):
	string = str(number)
	if string[0] == '-':
		string = string[::-1]
		new_string = string[-1]+string[:-1]
		return int(new_string)
	string = string[::-1]
	return int(string) 