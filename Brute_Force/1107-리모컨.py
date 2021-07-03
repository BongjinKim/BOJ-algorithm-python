import sys
'''
다시풀기
'''
channel = input()
M = int(input())
wrong_buttons = list(map(int, sys.stdin.readline().split()))
buttons = [b for b in range(10) if b not in wrong_buttons]
answer = abs(100 - int(channel))
cc = ''

for num in channel:
    num = int(num)
    min_num = 11
    cur_num = 0
    for b in buttons:
        if abs(num - b) < min_num:
            min_num = abs(num - b)
            cur_num = b
    cc += str(cur_num)
cur_channel = cc

for num in range(1000001):
    num = str(num)
    flag = False
    for b in wrong_buttons:
        if str(b) in num:
            flag = True
            break
    if flag: continue

    answer = min(answer, len(num) + abs(int(channel) - int(num)))
print(answer)