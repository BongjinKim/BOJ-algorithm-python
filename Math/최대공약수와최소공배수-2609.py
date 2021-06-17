import sys

'''
1회 12:46
'''
def euclidean_algorithm(a,b):
    a, b = max(a,b), min(a,b)
    while True:
        a %= b
        if a==0: return b
        b %= a
        if b==0: return a
#유클리드 호제법
a, b = list(map(int,sys.stdin.readline().split()))

gcd = euclidean_algorithm(a,b)
lcm = int(a*b/gcd)
print(gcd)
print(lcm)