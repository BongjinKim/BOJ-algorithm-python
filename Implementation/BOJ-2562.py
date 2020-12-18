import sys
max_tup = max(list(enumerate(int(line.strip()) for line in sys.stdin)), key=(lambda x: x[1]))
print('{}\n{}'.format(max_tup[1], max_tup[0] + 1))
