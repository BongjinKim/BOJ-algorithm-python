#평범한 문제
answer = 0
board = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(int(input())):
    w, h = map(int, input().split())
    for i in range(w, w+10):
        for j in range(h, h+10):
            board[i][j] = 1
for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            answer += 1
print(answer)
