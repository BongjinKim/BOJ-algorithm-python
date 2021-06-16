'''
1회 - 11:24
'''
answer = []
while True:
    try:
        n = int(input())
    except EOFError:
        break
    num_count = 1
    while True:

        if int('1'*num_count)%n == 0:
            answer.append(num_count)
            print(num_count)
            break
        else:
            num_count += 1
    if not n:
        break