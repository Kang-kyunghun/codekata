
def get_max_area(height):

  y = [0] + height # 실제 좌표랑 똑같이 생각하기 위해서 (0,0)을 추가
  
  x1 = 1 # 앞쪽 막대, 첫번째 막대 선택
  x2 = len(y) -1 #뒷쪽 막대, 마지막 막대 선택
  area = 0 # 처음에는 넓이가 없으니까 0으로 초기화
  #무한 루프
  while True :
    # 선택된 막대에 대하서 넓이 구하고 임시 저장
    temp_area = (x2-x1) * min(y[x1], y[x2])
    # area에 저장된 넚이와 temp_area에 저장된 임시 넚이 중 큰 값을 area에 저장
    area = max(area, temp_area)
    #앞쪽 막대와 뒷쪽 막대 중 더 큰 막대를 기준으로 다음 막대로 어떤 막대를 선택 할 지 결정
    if y[x1] < y[x2]:
      x1 = x1 + 1 #뒷쪽 막대가 더 크면 앞쪽 막대를 변경 (첫번째 -> 두번째)
    else:
      x2 = x2 -1 #앞쪽 막대가 더 크면 뒷쪽 막대를 변경 (마지막 막대 -> 마지막에서 두번째 )
    if x2 <= x1: #뒷쪽 막대가 앞쪽 막대를 역전하면 루프 종료
      break
  return area #루프 종료 후 넚이 반환

height = [1,8,6,2,5,4,8,3,7]
print(get_max_area(height))



import itertools #경우의 수를 구할 때 사용할 수 있는 모듈 (combinations 사용)

def get_max_area(height):

  #key=x축 값, #value=y축 값으로 dictionary 생성
  points ={}
  for x in range(1, len(height)+1):
    points[x] = height[x-1]  
  #2가지 막대를 뽑는 경우의 수를 case에 담음
  case = list(itertools.combinations(points.keys(), 2))
  #각 경우의 수에 대한 넓이들을 계산 하고 list에 담음
  areas = []
  for point in case:
    x1 = point[0]
    y1 = points[x1]

    x2 = point[1]
    y2 = points[x2]

    area = (x2 - x1) * min(y1, y2)
    areas.append(area)
  return max(areas) # 담은 값 중 가장 큰 값 반환

height = [1,8,6,2,5,4,8,3,7]
print(get_max_area(height))



