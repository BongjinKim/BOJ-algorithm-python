from collections import defaultdict
import copy

'''
30:14 시간 초과임 다시 풀어야 함, 문제 똑바로 읽기
'''
N = int(input())
board = [[i for i in input()] for _ in range(N)]
dir_x = [1, 0]
dir_y = [0, 1]


def eat_row_candy(board):
    max_count = 1
    for row in board:
        count = 1
        for i in range(N - 1):
            if row[i] == row[i + 1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
    return max_count


def eat_column_candy(board):
    max_count = 1
    for i in range(N):
        column = [row[i] for row in board]
        count = 1
        for i in range(N - 1):
            if column[i] == column[i + 1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
    return max_count


def eat_candy(board):
    ate_candies = []
    # row 방향으로 개수 세기
    ate_candies.append(eat_row_candy(board))
    ate_candies.append(eat_column_candy(board))
    return max(ate_candies)


answer = []
for i in range(N):
    for j in range(N):
        # 2방향 서치
        for d in range(2):
            if i + dir_y[d] < 0 or j + dir_x[d] < 0 or i + dir_y[d] >= N or j + dir_x[d] >= N:
                continue
            board[i][j], board[i + dir_y[d]][j + dir_x[d]] = board[i + dir_y[d]][j + dir_x[d]], board[i][j]
            # print(board)
            answer.append(eat_candy(board))
            board[i][j], board[i + dir_y[d]][j + dir_x[d]] = board[i + dir_y[d]][j + dir_x[d]], board[i][j]
print(max(answer))