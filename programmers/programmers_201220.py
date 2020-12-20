#2016년

def solution(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED" ]
    num = (a//2)*31 + ((a-1)//2)*30 + b
    if a > 2:
        num = num -1
    if a in [9,11]:
        num += 1
    answer = day[num%7]
    return answer

    