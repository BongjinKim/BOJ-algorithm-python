import sys
from collections import deque
from pprint import pprint

N, M = map(int, sys.stdin.readline().split())
board = [[int(s) for s in sys.stdin.readline() if s != '\n'] for _ in range(N)]
visited = [[[float('inf'), float('inf')] for _ in range(M)] for _ in range(N)] #N, M, Type
visited[0][0][0] = 1

queue = deque()
queue.append((0, 0, 0)) #i, j, type

dir = [(1,0), (-1,0), (0,1), (0,-1)]
while len(queue):
    y, x, type = queue.popleft()
    #print(y, x, type)
    for i, j in dir:
        ny = y+i
        nx = x+j
        if 0<=ny<N and 0<=nx<M and visited[ny][nx][type]==float('inf'):
            if board[ny][nx]==0:
                queue.append((ny,nx,type))
                visited[ny][nx][type] = visited[y][x][type] + 1
            elif board[ny][nx] and type==0:
                queue.append((ny,nx,type+1))
                visited[ny][nx][type+1] = visited[y][x][type] + 1
            #pprint(visited)
answer = min(visited[N-1][M-1])
print(-1 if answer == float('inf') else answer)