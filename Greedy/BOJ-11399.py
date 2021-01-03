N = int(input())
arr = sorted([int(ele) for ele in input().split()])
#print(N, arr)
answer = stack = 0
for ele in arr:
    stack += ele
    answer += stack
print(answer)
        
