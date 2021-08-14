import sys;

input = sys.stdin.readline
from collections import defaultdict


def calculate_date(M, N, x, y):
    dic = {}
    for i in range(0, 40001):
        # x = x if x!=M else 0
        dic[M * i + x] = 1
    # print(dic[10])
    for i in range(0, 40001):
        # y = y if y!=N else 0
        try:
            if dic[N * i + y]:
                return N * i + y
        except Exception:
            pass
    return -1


for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    print(calculate_date(M, N, x, y))

