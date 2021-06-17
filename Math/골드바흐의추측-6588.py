import sys
'''
시간초과 다시 풀 문제
'''
def find_prime_nums(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False
    n_sqrt = int(n ** 0.5)
    for i in range(2, n_sqrt+1):
        if not is_prime[i]: continue
        count = 2
        while i*count<=n:
            is_prime[i*count] = False
            count += 1
    return is_prime

def is_right_goldbah(n, prime_nums):
    for i in range(3,1000001):
        # print(prime_nums[n-i])
        if prime_nums[i] and prime_nums[n-i]: #i가 prime
            return (i,n-i)
    return 0

prime_nums = find_prime_nums(1000000)
input_list = list(map(int, sys.stdin.read().split()[:-1]))

for n in input_list:
    if n==0: break
    answer = is_right_goldbah(n, prime_nums)
    if answer:
        print('{0} = {1} + {2}'.format(n, answer[0], answer[1]))
    else:
        print("Goldbach's conjecture is wrong.")