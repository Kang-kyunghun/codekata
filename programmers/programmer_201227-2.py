def solution(plain):
    index = 0
    add = ''
    for index in range(len(plain)):
        re_plain = plain+add[::-1]
        print( re_plain, re_plain[::-1])
        if re_plain == re_plain[::-1]:
            return re_plain
        add += plain[index]
       



plain = 'abcde'


print(solution(plain))