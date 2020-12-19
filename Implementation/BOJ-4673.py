#규칙에 맞는 수를 구하고 중복을 없애기 위해 배열 사용, DP 기초 개념 사용
arr = [0] + [1 for _ in range(11000)]
for i in range(1, 10001):
    if arr[i]: print(i)
    while i <= 10000:
        i = i  + i // 1000 + i % 1000 // 100 + i % 100 // 10 + i % 10
        if arr[i]: arr[i] = 0
