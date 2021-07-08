import sys;

input = sys.stdin.readline

N, L = map(int, input().split())
location = sorted(map(int, input().split()))
i, j, count = 0, 1, 0
while j < N:
    if abs(location[i] - location[j]) + 1 <= L:
        j += 1
    elif abs(location[i] - location[j]) + 1 > L:
        i = j
        j += 1
        count += 1
print(count + 1)
