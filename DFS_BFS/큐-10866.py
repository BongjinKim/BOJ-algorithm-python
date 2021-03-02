import sys
que = []
for ele in range(int(input())):
    arr = sys.stdin.readline().split()
    #print(arr)
    if arr[0] == 'push':
        que.append(int(arr[1]))
    elif arr[0] == 'front':
        print(que[0] if que else -1)
    elif arr[0] == 'back':
        print(que[-1] if que else -1)
    elif arr[0] == 'size':
        print(len(que))
    elif arr[0] == 'empty':
        print(0 if que else 1)
    elif arr[0] == 'pop':
        print(que.pop(0) if que else -1)
