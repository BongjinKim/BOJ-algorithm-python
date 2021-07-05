import sys
from queue import PriorityQueue

N = int(input())
M = int(input())
nodes = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    nodes[a].append((c, b))

queue = PriorityQueue()
visited = [0] * (N + 1)
distance = [float('inf')] * (N + 1)
s, t = map(int, sys.stdin.readline().split())
distance[s] = 0
queue.put((0, s))  # distance, node

while queue.qsize():
    cur_dist, cur_node = queue.get()

    if visited[cur_node]: continue
    visited[cur_node] = 1

    for target_dist, target_node in nodes[cur_node]:
        queue.put((target_dist + cur_dist, target_node))
        distance[target_node] = min(distance[target_node], target_dist + cur_dist)
print(distance[t])