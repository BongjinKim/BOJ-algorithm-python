import sys
import copy

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dir_i = [0, 1, 0, -1]
dir_j = [1, 0, -1, 0]
visited = [[False for _ in range(M)] for _ in range(N)]
max_sum = 0

def dfs(i, j, visited, length, count):
    global max_sum
    if length==4:
        #print(max_sum)
        max_sum = max(max_sum, count)
        return
    for d in range(4):
        #board를 넘어가면 continue
        if i+dir_i[d]<0 or i+dir_i[d]>=N or j+dir_j[d]<0 or j+dir_j[d]>=M or visited[i+dir_i[d]][j+dir_j[d]]:
            continue
        visited[i+dir_i[d]][j+dir_j[d]] = True
        dfs(i+dir_i[d], j+dir_j[d], visited, length+1, count+board[i+dir_i[d]][j+dir_j[d]])
        visited[i+dir_i[d]][j+dir_j[d]] = False

#dfs로 length가 4가 나오는 도형
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,visited,1,board[i][j])
        visited[i][j] = False
#ㅗ, ㅓ, ㅏ , ㅜ 도형 --> 구현문제
#ㅏ모양
j_dir = [[0, 0, 0, 1],[1, 1, 1, 0],[1, 0, 1, 2],[0, 1, 2, 1]]
i_dir = [[0, 1, 2, 1],[0, 1, 2, 1],[0, 1, 1, 1],[0, 0, 0, 1]]

for i in range(N):
    for j in range(M):
        for i_d, j_d in zip(i_dir, j_dir):
            count = 0
            for i_s, j_s in zip(i_d, j_d):
                if i+i_s<0 or i+i_s>=N or j+j_s<0 or j+j_s>=M: continue
                count += board[i+i_s][j+j_s]
            max_sum = max(max_sum, count)
print(max_sum)