def solution(n, lost, reserve):
    answer = 0
    max_studendt = n

    for student_lost in lost[:]:
        if student_lost in reserve:
            reserve.remove(student_lost)
            lost.remove(student_lost)
    
    for student_reserve in reserve:
        if student_reserve -1 in lost:
            lost.remove(student_reserve -1)
        elif student_reserve + 1 in lost:
            if student_reserve + 1 in lost:
                lost.remove(student_reserve + 1)
    
    return max_studendt - len(lost)

n = 8	 
lost = [5,6]	
reserve = [5,6]

print(solution(n, lost, reserve))