#modedl

def is_valid(string):
	left = ['(', '{', '[']
	right = [')', '}', ']']
	stack = [ ]
    
	for letter in string:
		if letter in left:
			stack.append(letter)
		elif letter in right:
			if len(stack) <= 0:
				return False
			if left.index(stack.pop()) != right.index(letter):
				return False
	return len(stack) == 0

'''
  stack 의 LIFO 특징을 이용해서 문제를 해결 할 수 있다.
  먼저 빈 리스트stack을 생성한다. 여기에 for문으로 체크한 string의 요소가 들어 갈 것이다.
딕셔너리dict에 괄호를 종류별로 저장한다. 이 때, key에는 열림괄호, value에는 닫힘괄호를 저장한다.
string의 길이가 1 일때는 False를 리턴한다.
for문에서 string의 각각의 요소를 확인한다.
요소가 dict에 있는지를 확인한다 (딕셔너리이므로 key값에 있는지가 확인된다.)
존재할 경우, stack에 해당 요소를 더해준다.
존재하지 않을 경우(닫힘괄호), stack의 길이가 0이거나, stack에 들어가 있는 요소의 value값으로 존재 하지 않는 경우, False를 리턴한다.
stack.pop은 마지막 요소를 지우고 불러온다. 따라서 dict[stack.pop()]은, 현재 요소가 stack에 저장된 열림괄호에 해당하는 value인지를 체크한다.
stack의 길이가 0인지 확인을 조건에 넣은 이유는, 닫힘괄호로 시작하는 경우를 확인하기 위해서이다.
for문이 다 돌고 난 후, 유효한 string이라면 길이가 0이어야 한다. 따라서, True를 리턴하고 계산을 마친다.
닫힘괄호가 등장했을 때, elif문의 stack.pop이 실행되어, stack에서 요소가 제거되기 때문에, 최종 string의 길이는 0이어여만 유효하다.
/
만약 괄호가 이렇게 여러개 열렸다면 ([{, 마지막에 열린 괄호부터 차례차례 닫혀야한다.
일단 left에 해당하는 괄호(열린 괄호)가 나오면 stack에 append해준다. 그리고 right 괄호가 등장한다면 이 괄호는 가장 마지막에 등장한 괄호를 닫아주어야 하기 때문에 pop을 사용하여 가장 마지막으로 등장한 left괄호의 짝인지 확인한다(서로의 리스트의 index가 동일해야함).

하지만 여기서도 예외가 발생할 수 있다. 만약 stack에 담긴 left괄호가 없는데 비교할 right괄호만 있다면 오류상황 2번에 해당하는 경우이므로 False를 return해준다.

그리고 주어진 string을 다 돌았는데 stack에 요소가 남아있다면 해당 left에 해당하는 right가 등장하지 않은 것이므로 오류상황 2번에 해당하므로 len(stack)이 0이 아니면 False를 return하고 0이면 True를 return한다.

'''