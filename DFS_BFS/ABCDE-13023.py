def dfs(i, count):
    global ans
    print(1)
    visited[i] = 1
    #print(visited)
    if count == 4:
        ans = 1
        #print(ans)
        return
    for ele in arr[i]:
        if visited[ele] == 0:
            dfs(ele, count+1)
    visited[i] = 0
ans = 0
N, M = map(int, input().split())
arr = [[] for i in range(N)]
visited = [0 for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(N):
    #시작부터 끝까지 친구가 4명인 경우를 구하는 것, 시작이 다르므로 loop
    dfs(i, 0)#시작점과 친구수
print(ans)
