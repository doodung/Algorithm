# 17140 이차원 배열과 연산
# pypy:168ms python:92ms

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

i = 0
rLen, clen = 3, 3

def rCal(A, m):
    x = len(A)  # 행
    y = len(A[0])  # 열
    t = []
    for i in range(x):
        dic = {}
        temp = []
        cnt = 1
        for j in range(y):
            if A[i][j] != 0:
                if A[i][j] in dic.keys():
                    dic[A[i][j]] += 1
                else:
                    dic[A[i][j]] = cnt
        for k, v in sorted(dic.items(), key=lambda x: (x[1], x[0])):
            temp.append(k)
            temp.append(v)

        t.append(temp)
        m = max(len(temp), m)

    new_A = []
    for o in range(x):
        new_A = t
        for p in range(0, (m - len(t[o]))):
            new_A[o].append(0)
    return new_A, m


for time in range(101):
    if r <= rLen and c <= clen and A[r - 1][c - 1] == k:
        print(time)
        break

    if rLen >= clen:
        A, clen = rCal(A, clen)
    else:
        A, rLen = rCal(list(zip(*A)), rLen)
        A = list(zip(*A))

else:
    print(-1)
