import sys
E, S, M = list(map(int, sys.stdin.readline().split()))

for i in range(1, 15*28*19+1):
    if (i%15 if i%15 else 15)==E and (i%28 if i%28 else 28)==S and (i%19 if i%19 else 19)==M:
        print(i)
        break