import sys

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#1 회의 끝시간을 sort 한다.
arr = sorted(arr, key=lambda x : (x[1], x[0]))
answer = stack = 0
for start, end in arr:
    if stack <= start:
        stack = end
        answer += 1
print(answer)
