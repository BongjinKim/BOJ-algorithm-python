'''
해당 문제를 BFS로 풀었지만, 조건에 따른 DP문제로도 풀 수 있다.
'''
def BFS(N, K):
    queue = []
    visited = [0 for _ in range(100001)]
    queue.append((N, 0)) #loc 삽입
    visited[N] = 1
    while len(queue):
        loc, step = queue.pop(0)
        #print(loc, step)
        if loc == K:
            return step
        for next_loc in (loc+1, loc-1, loc*2):
            if 0 > next_loc or next_loc > 100000 or visited[next_loc]:
                continue
            queue.append((next_loc, step+1))
            visited[next_loc] = 1
            #print(next_loc, step)
        #assert step != 100000

def solution():
    N, K = map(int, input().split())
    answer = BFS(N, K)
    print(answer)

solution()