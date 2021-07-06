import sys; input = sys.stdin.readline
import copy
N = int(input())
min_prev = list(map(int, input().split()))
max_prev = copy.deepcopy(min_prev)
for i in range(N-1):
    next = list(map(int, input().split()))
    min_prev = [next[0]+min(min_prev[:2]), next[1]+min(min_prev), next[2]+min(min_prev[1:])]
    max_prev = [next[0]+max(max_prev[:2]), next[1]+max(max_prev), next[2]+max(max_prev[1:])]
print(max(max_prev), min(min_prev))