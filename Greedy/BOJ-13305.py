N = int(input())
min_city = 1000000001
answer = 0
'''
zip을 사용하면 길이가 더 짧은 list로 맞춰지므로, 거리, 도시가 1:1 매핑 가능함
(주유비 * 거리)를 도시마다 비교하여 짧으면 갱신, 아니면 비갱신
타 문제에서는 더해준 비용을 빼주는 경우도 있는데, 일단 이동을 위해선 주유가
필요하므로 이번 문제는 더해진 비용을 빼지는 않음
'''
for length, city in zip(input().split(), input().split()):
    if min_city > int(city):
        min_city = int(city)
    answer += min_city*int(length)
print(answer)
