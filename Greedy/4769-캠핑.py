import sys; input = sys.stdin.readline

i = 1
while True:
    L, P, V = map(int, input().split())
    if not L and not P and not V: break
    print("Case {}: {}".format(i, (V//P*L) + (V%P if V%P<L else L)))
    i += 1