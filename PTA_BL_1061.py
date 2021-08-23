N, M = map(int, input().split())
# N, M = map(int, "3 6".split())
fenshuList = list(map(int, input().split())) #分数数组
# fenshuList = list(map(int, "2 1 3 3 4 5".split()))
duicuoList = list(map(int, input().split())) #对错数组
# duicuoList = list(map(int, "0 0 1 0 1 1".split()))

for i in range(N):
    studentList = list(map(int, input().split()))
    # studentList = list(map(int, "0 1 1 0 0 1".split()))
    score = 0
    for index, val in enumerate(studentList):
        if val == duicuoList[index]:
            score += fenshuList[index]
    print(str(score))