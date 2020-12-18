#code comprehension이 중요한 파트, 적절하게 split과 sum을 이용하여 품
for _ in range(int(input())):
    print(sum(sum(j for j in range(1, len(i) + 1)) for i in input().split('X')))
