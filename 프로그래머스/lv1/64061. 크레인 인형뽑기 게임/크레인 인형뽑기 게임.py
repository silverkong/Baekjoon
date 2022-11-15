def solution(board, moves):
    answer = 0
    basket = []
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] > 0:
                basket.append(board[i][m-1])
                board[i][m-1] = 0
                if basket[-1:] == basket[-2:-1]:
                    answer += 2
                    basket = basket[:-2]
                break
    
    return answer