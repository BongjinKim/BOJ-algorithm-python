#python generator 학습, generator expression은 next로 찾기때문에 한번 다돌고나면 가리키는 데이터가 없게 됨. 자주쓸거면 list가 나음
s = [input() for _ in range(5)]
if 'FBI' not in ','.join(s): print('HE GOT AWAY!')
else:
    for j in (i+1 for i, v in enumerate(s) if 'FBI' in v):
        print(j, end=' ')
