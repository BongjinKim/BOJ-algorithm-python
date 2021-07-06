import sys;

input = sys.stdin.readline

N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: [x[1], x[0]], reverse=True)
answer = [0] * 1001

for d, w in arr:
    while d > 0:
        if answer[d]:
            d -= 1
        else:
            answer[d] = w
            break

print(sum(answer))