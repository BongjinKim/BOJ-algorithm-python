from collections import deque
from pprint import pprint
import sys

'''
28:59 - 다시 풀기
'''
n = int(input())


def BFS(queue):
    while len(queue):
        i, j, time, type = queue.popleft()
        for d in range(4):
            next_i = i + dir_y[d]
            next_j = j + dir_x[d]
            if type == 1 and (0 <= next_i < h and 0 <= next_j < w and visited_fire[next_i][next_j] == False):
                visited_fire[next_i][next_j] = True
                visited_sanguen[next_i][next_j] = True
                queue.append((next_i, next_j, time + 1, type))
            elif type == 0:
                # 안에 있으면 이동
                if 0 <= next_i < h and 0 <= next_j < w:
                    if not visited_sanguen[next_i][next_j]:
                        visited_sanguen[next_i][next_j] = True
                        queue.append((next_i, next_j, time + 1, type))
                else:  # 밖으로 나가면
                    return time + 1
    return "IMPOSSIBLE"


for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    visited_fire = [[False for _ in range(w)] for _ in range(h)]
    visited_sanguen = [[False for _ in range(w)] for _ in range(h)]
    dir_x = [1, 0, -1, 0]
    dir_y = [0, 1, 0, -1]
    queue = deque()
    board = []

    for i in range(h):
        arr = []
        for j, s in enumerate(sys.stdin.readline()):
            if s == '*':
                visited_fire[i][j] = True
                visited_sanguen[i][j] = True
                queue.appendleft((i, j, 0, 1))
            elif s == '@':
                visited_sanguen[i][j] = True
                queue.append((i, j, 0, 0))
            elif s == '#':
                visited_sanguen[i][j] = True
                visited_fire[i][j] = True
            elif s == '\n':
                continue
            arr.append(s)
        board.append(arr)
    print(BFS(queue))
