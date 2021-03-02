from collections import deque

def BFS(S):
    #initialize
    step = 0
    queue = deque([(1, 0, 0)])
    visited = [[0 for _ in range(1001)] for _ in range(1001)]
    while len(queue):
        input_emo, copy_emo, step = queue.popleft()
        if input_emo == S:
            return step
        for next_input, next_copy in (input_emo+copy_emo, copy_emo), (input_emo, input_emo), (input_emo-1, copy_emo):
            if next_copy == 0 or next_input>1000 or next_input<0 or visited[next_input][next_copy]: #copy한게 아무것도 없으면
                continue
            queue.append((next_input, next_copy, step+1))
            visited[next_input][next_copy] = 1
        #print(queue)
        #assert step != 10
            
def solution():
    S = int(input())
    answer = BFS(S)
    print(answer)
    
solution()