import sys;

input = sys.stdin.readline
from queue import PriorityQueue
import heapq

N = int(input())
queue = []
arr = []
for _ in range(N):
    s, t = map(int, input().split())
    arr.append((s, t))
arr = sorted(arr)
# print(arr)
heapq.heappush(queue, (arr[0][1], arr[0][0]))

for i in range(1, N):
    cur_t, cur_s = queue[0]
    new_s, new_t = arr[i]
    # print((new_t, new_s))
    if cur_t > new_s:
        heapq.heappush(queue, (new_t, new_s))
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, (new_t, cur_s))
    # print(queue)

print(len(queue))
