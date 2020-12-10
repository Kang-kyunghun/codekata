def solution(answers):
    supoja = {
        "1" : [1, 2, 3, 4, 5],
        "2" : [2, 1, 2, 3, 2, 4, 2, 5],
        "3" : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    result = []
    temp = 0
    answer = []
    for supo_person in supoja.values():
        for i in range(len(answers)):
            if answers[i] == supo_person[i%len(supo_person)]:
                temp += 1
        result.append(temp)
        temp = 0
    max_answer = max(result)
    for index in range(len(result)):
        if result[index] == max_answer:
            answer.append(index+1)
    
    return answer

# answers = [1,2,3,4,5,1,2,3,4,5]
answers = [1,1,1,1,1,1,1,1,1,1]
print(solution(answers))

