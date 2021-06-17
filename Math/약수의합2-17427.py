import sys

'''
실패 다시풀기
'''
sum_of_measures = [0] * 1000001
for i in range(1,1000001):
    for j in range(i,1000001,i):
        sum_of_measures[j] += i
    sum_of_measures[i] += sum_of_measures[i-1]
print(sum_of_measures[int(sys.stdin.readline())])