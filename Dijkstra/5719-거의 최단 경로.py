import sys
from queue import PriorityQueue

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0: break
    S, D = map(int, sys.stdin.readline().split())
    nodes = [[] for _ in range(N)]
    distance = [float('inf') for _ in range(N)]
    visited = [0 for _ in range(N)]
    queue = PriorityQueue()
    min_route = [[] for _ in range(N)]
    for _ in range(M):
        U, V, P = map(int, sys.stdin.readline().split())
        nodes[U].append((P, V))

    distance[S] = 0
    queue.put((0, S))  # distance, start_node
    # print(nodes)
    while queue.qsize():
        cur_distance, cur_node = queue.get()
        # print(cur_node, cur_distance)
        if visited[cur_node]: continue
        visited[cur_node] = 1
        for target_id, (target_dist, target_node) in enumerate(nodes[cur_node]):
            queue.put((cur_distance + target_dist, target_node))
            if distance[target_node] > cur_distance + target_dist:
                distance[target_node] = cur_distance + target_dist
                min_route[target_node] = min_route[cur_node] + [(cur_node, target_id)]
            elif distance[target_node] == cur_distance + target_dist:
                min_route[target_node] = min_route[target_node] + min_route[cur_node] + [(cur_node, target_id)]
            # print(distance)
    # print(nodes)
    for i, j in min_route[D]:
        # print(nodes[i][j])
        nodes[i][j] = ()
    nodes = [[n for n in node if n] for node in nodes]
    # print(nodes)

    distance = [float('inf') for _ in range(N)]
    visited = [0 for _ in range(N)]
    distance[S] = 0
    queue.put((0, S))  # distance, start_node
    while queue.qsize():
        cur_distance, cur_node = queue.get()
        # print(cur_node, cur_distance)
        if visited[cur_node]: continue
        visited[cur_node] = 1
        for target_id, (target_dist, target_node) in enumerate(nodes[cur_node]):
            queue.put((cur_distance + target_dist, target_node))
            distance[target_node] = min(distance[target_node], cur_distance + target_dist)
            # print(distance)
    print(distance[D] if distance[D] != float('inf') else -1)
    # print()