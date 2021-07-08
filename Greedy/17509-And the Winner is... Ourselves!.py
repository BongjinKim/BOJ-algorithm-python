import sys;

input = sys.stdin.readline

arr = []
for _ in range(11):
    D, V = map(int, input().split())
    arr.append((D, V))
# print(sorted(arr))

now = 0
penalty = 0
for d, v in sorted(arr):
    now += d
    penalty += now
    penalty += v * 20
print(penalty)
