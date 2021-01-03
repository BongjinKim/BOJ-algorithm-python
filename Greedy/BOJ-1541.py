import re

p = re.compile('[0-9]+|[-|+]')
arr = p.findall(input())
answer = []
i = 0
while i < len(arr):
    if arr[i] != '-' and arr[i] != '+':
        answer.append(int(arr[i]))
    elif arr[i] == '+':
        a = answer.pop()
        b = int(arr[i+1])
        answer.append(a+b)
        i += 1
    i += 1
print(answer[0] - sum(answer[1:]))
