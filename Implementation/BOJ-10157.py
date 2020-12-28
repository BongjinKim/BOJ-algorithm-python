import pprint
H, W = map(int, input().split())
hall = [[0 for _ in range(W+1)] for _ in range(H+1)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
d, i, j = 0, 1, 1
n = int(input())
if H * W < n:
    print(0)
else:
    #if count == n, loop break
    hall[1][1] = 1
    '''
    i, j 값이 hall 밖으로 넘어가거나, hall[i][j]가 1이면 loop break
    1 loop 당 1 count
    '''
    for k in range(n-1):
        if i+dir_y[d] >= H+1 or i+dir_y[d] < 1 or j+dir_x[d] >= W+1 or j+dir_x[d] < 1 or hall[i+dir_y[d]][j+dir_x[d]]:
            #rotate
            d = (d+1) % 4
        i += dir_y[d]
        j += dir_x[d]
        hall[i][j] = 1
    #pprint.pprint(hall)
    print(i, j)
