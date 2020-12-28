#math problem, sum of A * sum of B
A, B = map(list, input().split())
print(sum(int(i) for i in A) * sum(int(i) for i in B))
