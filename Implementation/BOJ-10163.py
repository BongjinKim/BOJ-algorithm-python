arr = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())
for n in range(N):
    s_i, s_j, w, h = map(int, input().split())
    for i in range(s_i, s_i + w):
        for j in range(s_j, s_j + h):
            arr[i][j] = n + 1
for n in range(N):
    answer = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == n+1: answer+=1
    print(answer)
