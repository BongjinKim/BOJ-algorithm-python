import sys

n = int(input())
total = 0
numbers = list(map(int, sys.stdin.readline().split()))
total_nums = [0] * n
answer = -1001
# 전에 것이 음수면 더해서 이어서 표현 아니면 새로시작
for i in range(n):
    total_nums[i] = max(total_nums[i - 1] + numbers[i], numbers[i])
    answer = max(answer, total_nums[i])
print(answer)
