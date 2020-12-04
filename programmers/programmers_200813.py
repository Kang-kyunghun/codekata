# list 안에 중복 없에고, 순서 유지하기 (set을 사용하면 자동으로 정렬 되어 사용 못함)
# 처음 코드 : 제거하는 방식 => 효율성이 떨어짐
# 나중 코드 : 빈 list에 추가하는 방식 => 효율성 증가
my_list = [4,4,4,4,3,3,3,3,3]
i = 0
result =[]
while i <len(my_list):
    if i == len(my_list)-1:
        result.append(my_list[-1])
    else:
        if my_list[i] != my_list[i+1]:
            result.append(my_list[i])
    i +=1

print(result)

# 배열 안에 나누어 떨어지는 수들을 찾고 오름 차순 정리 (없으면 -1 출력)

# arr : 나눌 수들의 배열
# Divisor : 나누는 수

# 내코드

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            answer = sorted(answer)
    if len(answer) == 0:
        answer.append(-1)
    return answer

#한 줄 코드
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

