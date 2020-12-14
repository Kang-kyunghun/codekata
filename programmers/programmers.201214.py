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

dartResult = '1D2S#10S'
print(solution(dartResult))