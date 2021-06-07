def find_fake_dwarfs(dwarfs_height, sum_of_fake_dwarfs):
    fake_dwarfs = []
    for i in range(n):
        num = 0
        temp = [ele for ele in dwarfs_height]
        num= temp.pop(i)
        #print(temp)
        for idx, ele in enumerate(temp):
            if num+ele == sum_of_fake_dwarfs:
                temp.pop(idx)
                return sorted(temp)
    return -1

n = 9
dwarfs_height = [int(input()) for _ in range(n)]
sum_of_fake_dwarfs = sum(dwarfs_height) - 100
for ele in find_fake_dwarfs(dwarfs_height, sum_of_fake_dwarfs):
    print(ele)
