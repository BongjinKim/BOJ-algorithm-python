from collections import deque
import pprint
def solution():
    def rotate_arr(A, operate):
        if operate == 1:
            A = [A[i] for i in range(len(A)-1,-1,-1)]
            #print(A)
        elif operate == 2:
            A = [[A[j][i] for i in range(len(A[j])-1,-1,-1)] for j in range(len(A))]
            #print(A)
        elif operate == 3:
            A = [[A[i][j] for i in range(len(A)-1,-1,-1)] for j in range(len(A[0]))]
            #print(A)
        elif operate == 4:
            A = [[A[i][j] for i in range(len(A))] for j in range(len(A[0])-1,-1,-1)]
            #pprint.pprint(A)
        elif operate == 5:
            for i in range(len(A)//2):
                for j in range(len(A[0])//2):
                    n, m = len(A)//2, len(A[0])//2
                    A[i][j], A[i][j+m], A[i+n][j+m], A[i+n][j] = A[i+n][j], A[i][j], A[i][j+m], A[i+n][j+m]
            #pprint.pprint(A)
        elif operate == 6:
            for i in range(len(A)//2):
                for j in range(len(A[0])//2):
                    #print(i,j)
                    n, m = len(A)//2, len(A[0])//2
                    A[i][j], A[i][j+m], A[i+n][j+m], A[i+n][j] = A[i][j+m], A[i+n][j+m], A[i+n][j], A[i][j]
            #pprint.pprint(A)
        return A
    
    N, M, R = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(N)]
    
    for operate in map(int, input().split()):
        A = rotate_arr(A, operate)
    
    for ele in A:
        print(*ele)
    
#solution()


#공부해야할코드
o,f,R=open(0).readline,lambda:map(int,o().split()),range
c=lambda i,j:[[M[m*i+v][n*j+w]for w in R(n)]for v in R(m)]
def t(s):
    i=[j[::[1,-1][D]]for j in s][::[1,-1][U]]
    return[i,zip(*i)][T]
D=U=T=0
x,y,n=f()
m,n=x//2,y//2
M=[[*f()]for i in R(x)]
m=[c(0,0),c(0,1),c
(1,0),c(1,1)]
for k in f():
    a,b,c,d=m
    if k==1:m=[c,d,a,b]
    elif k==2:m=[b,a,d,c]
    elif k in (3,5):m=[c,a,d,b]
    else:m=[b,d,a,c]
    if k<5:
        if(k&1^1)^(T&1):D^=1
        else:U^=1
        T^=k>2
a,b,c,d=map(t,m)
for i,j in zip(a,b):print(*i,*j)
for i,j in zip(c,d):print(*i,*j)
