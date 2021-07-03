import sys
import copy
from queue import PriorityQueue

n, m, f, s, t = map(int, sys.stdin.readline().split())
nodes = [[] for _ in range(n)]
answer = float('inf')
visited = [[False] * n for _ in range(2)]
distance = [[float('inf')] * n for _ in range(2)]

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    nodes[u].append((w, v))
    nodes[v].append((w, u))

queue = PriorityQueue()
for _ in range(f):
    u, v = map(int, sys.stdin.readline().split())
    nodes[u].append((0, v))

distance[0][s] = 0
queue.put((0, s, 0))
while queue.qsize():
    cur_dist, cur_node, is_plane = queue.get()
    if visited[is_plane][cur_node]: continue

    visited[is_plane][cur_node] = True
    # print(cur_node, cur_dist, is_plane, nodes[cur_node])
    for dist, i in nodes[cur_node]:
        if dist:
            queue.put((dist + cur_dist, i, is_plane))
            distance[is_plane][i] = min(dist + cur_dist, distance[is_plane][i])
        elif not dist and is_plane == 0:
            queue.put((dist + cur_dist, i, is_plane + 1))
            distance[1][i] = min(dist + cur_dist, distance[is_plane][i])
        # print(distance)
    # print(visited)
answer = min(distance[0][t], distance[1][t])
print(answer)