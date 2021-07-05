import sys
from queue import PriorityQueue

N, E = map(int, sys.stdin.readline().split())
nodes = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    nodes[a].append((c, b))
    nodes[b].append((c, a))

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(s):
    queue = PriorityQueue()
    visited = [0] * (N + 1)
    distance = [float('inf')] * (N + 1)
    distance[s] = 0
    queue.put((0, s))  # distance, node
    while queue.qsize():
        cur_dist, cur_node = queue.get()
        if visited[cur_node]: continue
        visited[cur_node] = 1
        # log[cur_node].add(cur_node)
        # print(cur_node)
        for target_dist, target_node in nodes[cur_node]:
            if distance[target_node] > target_dist + cur_dist:
                queue.put((target_dist + cur_dist, target_node))
                distance[target_node] = min(distance[target_node], target_dist + cur_dist)
    return distance


dij_v1 = dijkstra(v1)
dij_start = dijkstra(1)
dij_v2 = dijkstra(v2)
a1 = dij_start[v1] + dij_v1[v2] + dij_v2[N]
a2 = dij_start[v2] + dij_v2[v1] + dij_v1[N]
answer = min(a1, a2)
print(answer if answer != float('inf') else -1)
