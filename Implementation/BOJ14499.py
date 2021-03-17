import sys
#45분.... 후덜덜....
input_line = lambda: map(int,sys.stdin.readline().split())
n, m, x, y, k = input_line()
board = [[ele for ele in input_line()] for _ in range(n)]
#동 서 북 남
dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
direction = [(3,1,0,5,4,2), (2,1,5,0,4,3), (4,0,2,3,5,1), (1,5,2,3,0,4)]
dice = [0,0,0,0,0,0]
#print(board)
for i in input_line():
    cur_dir = direction[i-1]
    if 0<=x+dx[i-1]<n and 0<=y+dy[i-1]<m:
        #이동
        x += dx[i-1]
        y += dy[i-1]
        temp = [dice[d] for d in cur_dir]
        if board[x][y]:
            temp[5] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = temp[5]
        dice = temp.copy()
        print(dice[0])
