def get_len_of_str(string):

    len_str = []
    set_str = []
    temp_str = ''
    x =[]
    for index in range(0,len(string)-1):
        
        temp =string[index]

        if temp != string[index+1]:
            temp_str += temp
            temp = string[index+1]
        else:
            temp_str += temp
            len_str.append(len(temp_str))
            set_str.append(temp_str)
            temp = string[index+1]
            temp_str = ''
    if temp == string[-1]:
        if temp == string[-2]:
            len_str.append(len(temp))
            set_str.append(temp)
        else:
            temp_str += temp
            len_str.append(len(temp_str))
            set_str.append(temp_str)
    for i in set_str:
        x.append(len(set(i)))
    print(x)
    return max(x)

print(get_len_of_str('abcacbacb'))