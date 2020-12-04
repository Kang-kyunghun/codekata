# 입력받은 두 자연수 a부터 b까지 모든 자연수의 합

def solution(a, b):
    answer = 0
    if a > b:
        a , b = (b, a)
    return sum(range(a, b+1))
   
# 문자열의 길이가 4 또는 6인지 확인 및 숫자로만 구성되어 있는지 확인

# 내코드 : 예외처리 사용

def solution(s):
    if len(s) not in [4, 6]:
        return False
    try:
        for i in s:
            int(i)
    except ValueError:
        return False
    return True


#한줄 코드
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6) #.isdigit() 함수 사용

# 리스트 안의 문자열을 특정 조건과 사전순서에 맞게 재정렬

#내코드
def solution(strings, n):
    
    strings.sort()
    #사전순서대로 먼저 정렬
    answer = sorted(strings, key= lambda x: (x[n]))
    #key 값을 이용하여 원하는 조건으로 정렬 
    
    return answer