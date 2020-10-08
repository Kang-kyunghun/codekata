# 모법답안
def reverseString(str):
  if len(str) == 0:
    return str
  else:
    return reverseString(str[1:]) + str[0]

#특정 인덱스를 지정 할 때는 인덱스 범위에서 지정 해줘야 하지만, 슬라이싱을 할 때는 범위를 넘어서도 상관 없음