#경사로 구현문제
import sys
input_line = lambda: map(int, sys.stdin.readline().split())
N, L = input_line()
board = [[ele for ele in input_line()] for _ in range(N)]
answer = 0

def find_road(board):
    #가로줄
    count = 1
    answer = 0
    for a, b in board:
        if a == b:
            count += 1
        elif a+1 == b and count>=L: #언덕
            count = 1
        elif a == b+1 and count>=0: #내리막
            count = -L + 1
        else:
            break
    else:
        if count>=0:
            answer +=1
    return answer

for i in range(N):
    answer += find_road(zip(board[i],board[i][1:]))
    answer += find_road(zip([ele[i] for ele in board], [ele[i] for ele in board[1:]]))

print(answer)