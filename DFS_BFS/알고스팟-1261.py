from collections import deque

def BFS(N, M, board):
    #initialize
    queue = deque([(0, 0, 0)]) #(i, j, count_of_crushed)
    visited = [[0 for _ in range(M)] for _ in range(N)]
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    answer = []
    visited[0][0] = 1
    while len(queue):
        i, j, count_of_crushed = queue.popleft()
        if i==N-1 and j==M-1:
            answer.append(count_of_crushed)
            
        for d_i, d_j in direction:
            if i+d_i<0 or j+d_j<0 or i+d_i>=N or j+d_j>=M or visited[i+d_i][j+d_j]:
                continue
            if board[i+d_i][j+d_j]:
                 queue.append([i+d_i, j+d_j, count_of_crushed+1])
                 #print(i+d_i, j+d_j)
            else:
                queue.appendleft([i+d_i, j+d_j, count_of_crushed])
            #print(i+d_i, j+d_j)
            visited[i+d_i][j+d_j] = 1
    return min(answer)

def solution():
    M, N = map(int, input().split())
    board = [[int(i) for i in input()] for _ in range(N)]
    #print(board)
    answer = BFS(N, M, board)
    print(answer)
    
solution()