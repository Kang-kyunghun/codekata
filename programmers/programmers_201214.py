#2018 KAKAO BLIND RECRUITMENT  > dart
def solution(dartResult):
    dart = dartResult[0]
    dart_10 = False
    score = []
    bonus = {
        "S" : lambda x : x**1,
        "D" : lambda x : x**2,
        "T" : lambda x : x**3,
    }
    option = {
        "*" : lambda x : x*2,
        "#" : lambda x : x*(-1)
    }
    for index in range(len(dartResult)):
        dart = dartResult[index]
        if dart_10:
            dart = '10'
            dart_10 = False

        if dart == '1' and dartResult[index+1] == '0':
            dart_10 = True
            continue
        print(dart)
        if dart in '0123456789' or dart == '10':
            score.append(int(dart))
        if dart in 'SDT':
            temp = score.pop()
            score.append(bonus[dart](temp))
        if dart == '*':
            if len(score) == 1:
                temp = score.pop()
                score.append(option[dart](temp))
            else:
                temp_first = score.pop()
                temp_second = score.pop()
                score.append(option[dart](temp_second))
                score.append(option[dart](temp_first))
        if dart == '#':
            temp = score.pop()
            score.append(option[dart](temp))
    answer = score
    return sum(answer)

#2018 KAKAO BLIND RECRUITMENT  > [1차] 비밀지도

def solution(n, arr1, arr2):
    bin1 = []
    bin2 = []
    results = [] 
    for dec in arr1:
        temp = bin(dec)[2:]
        binary = '0'*(n-len(temp)) + temp
        bin1.append(binary)
    for dec in arr2:
        temp = bin(dec)[2:]
        binary = '0'*(n-len(temp)) + temp
        bin2.append(binary)
    for x in range(0,n):
        result = ''
        for y in range(0,n):
            if bin1[x][y] == '0' and bin2[x][y] == '0':
                result += ' '
            else:
                result += '#'
        results.append(result)

    answer = results
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
