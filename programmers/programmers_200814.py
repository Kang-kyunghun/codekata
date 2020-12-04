# 입력 받은 n이 어떤 양의 정수 x의 제곱근인지 판별

from math import sqrt
def solution(n):
    x = int(sqrt(n))
    if x*x == n:
        return (x+1)**2
    else:
        return -1

# commands의 조건에 맞게 list 슬라이싱 후 값 출력
#내코드

def solution(array, commands):
    arr = []
    answer = []
    for com in commands:
        arr = array[com[0]-1:com[1]]
        arr.sort()
        answer.append(arr[com[2]-1])
    return answer

# #한 줄 코드

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


# 기타 정답 코드

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# 문자열 정수로 바꾸기

def solution(s):
    if s[0] == ['-']:
        s = s[1:]
        answer = int(s)*(-1)
    else:
        answer = int(s)
    return answer

    #string s의 인자들은 n칸 만큼 밀기(아스키코드사용)

    def solution(s, n):
    answer = ''
    for word in s:
        if word != ' ':
            new = ord(word)
            if word.isupper():
                new = new + n
                if new > ord('Z'):
                    new -= 26
            if word.islower():
                new = new + n
                if new >ord('z'):
                    new -= 26
            answer = answer + chr(new)
        else:
            answer += ' '
    return answer