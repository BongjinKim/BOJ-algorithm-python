N, K = map(int, input().split())
arr_coin = [int(input()) for _ in range(N)]
answer = 0
while K:
    now = max(ele for ele in arr_coin if K//ele != 0) #10회
    answer += K//now
    K -= K//now * now
print(answer)
