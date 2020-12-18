#문자열 붙이기 join 사용, 또 문자열 반복 * 연산자 사용
for _ in range(int(input())):
    input_str = input().split()
    print(''.join(c * int(input_str[0])  for c in input_str[1]))
