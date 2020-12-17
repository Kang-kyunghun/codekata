def solution(board, moves):
    basket = []
    answer = 0
   
    for move in moves:
        for check in range(len(board)):
            if board[check][move-1] != 0:
                temp = board[check][move-1]
                
                if basket and basket[-1] == temp:
                    basket.pop()
                    answer += 2
                    print(temp, answer)
                else:
                    basket.append(temp)
                
                board[check][move-1]= 0
                break 

    
    return answer
board = [
            [0,0,0,0,0],
            [0,0,1,0,3],
            [0,2,5,0,1],
            [4,2,4,4,2],
            [3,5,1,3,1]
        ]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))