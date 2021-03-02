from collections import deque

def BFS(N, K):
    #initialize
    visited = [0 for _ in range(100001)]
    queue = deque([(N, 0)])
    while len(queue):
        loc, step = queue.popleft()
        if K == loc:
            return step
            
        for next_loc in (loc+1, loc-1, loc*2):
            if next_loc<0 or next_loc>100000 or visited[next_loc]:
                continue
            if next_loc != loc*2:
                queue.append((next_loc, step+1))
            else:
                queue.appendleft((next_loc, step))
            visited[next_loc] = 1

def solution():
    N, K = map(int, input().split())
    answer = BFS(N, K)
    print(answer)
    
solution()