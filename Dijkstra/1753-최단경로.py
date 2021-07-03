import sys
from queue import PriorityQueue

V, E = map(int, sys.stdin.readline().split())
K = int(input())
visited = [False] * (V + 1)
distance = [float('inf')] * (V + 1)
queue = PriorityQueue()
nodes = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    nodes[u].append((w, v))
distance[K] = 0
queue.put((0, K))

while queue.qsize():
    cur_dist, cur_node = queue.get()
    if visited[cur_node]: continue

    visited[cur_node] = True
    for dist, i in nodes[cur_node]:
        queue.put((dist + cur_dist, i))
        distance[i] = min(dist + cur_dist, distance[i])
for ele in distance[1:]:
    print(ele if ele != float('inf') else 'INF')