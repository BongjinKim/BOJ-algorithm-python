#배열 돌리기1
import sys

input_example = lambda:map(int, sys.stdin.readline().split())
n, m, r = input_example()
A = [list(input_example()) for _ in range(n)]
# B = [[0 for _ in range(m)] for _ in range(n)]
depth = min(n,m)//2 #min(N,M)은 짝수

for i in range(depth):
    #print(s,n,m)
    B = []
    for a in range(i,n-1-i):
        B += [A[a][i]]
    for c in range(i,m-1-i):
        B += [A[n-i-1][c]]
    for b in range(n-i-1,i,-1):
        B += [A[b][m-i-1]]
    for d in range(m-i-1,i,-1):
        B += [A[i][d]]
    length = r%len(B)
    B = iter(B[-length:]+B[:-length])
    for a in range(i,n-1-i):
        A[a][i] = next(B)
    for c in range(i,m-1-i):
        A[n-i-1][c] = next(B)
    for b in range(n-i-1,i,-1):
        A[b][m-i-1] = next(B)
    for d in range(m-i-1,i,-1):
        A[i][d] = next(B)
#print(A)
for i in A:
    print(*i)
