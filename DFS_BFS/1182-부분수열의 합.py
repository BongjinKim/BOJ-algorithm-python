import sys;

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * N
answer = 0


# print(arr)
def dfs(s, i):
    global answer
    if i == N:
        return
    if s + arr[i] == S:
        answer += 1

    # print(s+arr[i], s, 0)
    dfs(s + arr[i], i + 1)
    dfs(s, i + 1)


dfs(0, 0)
print(answer)