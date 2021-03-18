import sys
input_line = lambda: map(int, sys.stdin.readline().split())
N = input_line()
arr = sorted(input_line())
target = 1

for ele in arr:
    if target<ele:
        break
    target += ele
print(target)