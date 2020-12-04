#2020 카카오 인턴쉽 키패드 누르기

def solution(numbers, hand):
    answer = ''
    location ={
        '*' : (0,0),
        '0' : (0,1),
        '#' : (0,2),
        '7' : (1,0),
        '8' : (1,1),
        '9' : (1,2), 
        '4' : (2,0),
        '5' : (2,1),
        '6' : (2,2),
        '1' : (3,0),
        '2' : (3,1),
        '3' : (3,2),   
    }
    now_left = location['*']
    now_right = location['#']

    for number in numbers:
        point = location[str(number)]
        print(point)
        if number in [1,4,7]:
            answer += 'L'
            now_left = location[str(number)]
        elif number in [3,6,9]:
            answer += 'R'
            now_right = location[str(number)]
        elif number in [2,5,8,0]:
            distance_left = abs((now_left[0] - point[0])) + abs((now_left[1] - point[1]))  
            distance_right = abs((now_right[0] - point[0])) + abs((now_right[1] - point[1]))
            if distance_left > distance_right:
                answer += 'R'
                now_right = location[str(number)]
            elif distance_left < distance_right:
                answer += 'L'
                now_left = location[str(number)]
            else:
                if hand == 'left':
                    answer += 'L'
                    now_left = location[str(number)]
                else:
                    answer += 'R'
                    now_right = location[str(number)]
                    
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))