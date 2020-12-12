def solution(citations):
    h = 0 
    h_list = []
    count = 0
    citations.sort()
    while True:
        for citation in citations:
            if citation >= h:
                count += 1
        if count >= h:
            h += 1
            count = 0
        else:
            return h - 1
        
    


citations = [0,1,1]
# citations = [2, 2, 2, 2, 2, 2]

print(solution(citations))
# print(citations.index(2))