def solution(plain):
    index = 0
    add = ''
    while True:
        l = len(plain) // 2
        re_plain = plain+add[::-1]
        print( re_plain, re_plain[::-1])
        if re_plain == re_plain[::-1]:
            return re_plain
        add += plain[index]
        index += 1



plain = 'abcde'


print(solution(plain))