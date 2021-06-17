'''
1회 - 11:12
'''
import sys
N = int(input())
arr = sorted(int(n) for n in sys.stdin.readline().split())

if len(arr)>=2:
    print(arr[0]*arr[-1])
else:
    print(arr[0]**2)