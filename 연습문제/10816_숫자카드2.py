import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
m_list = list(map(int, sys.stdin.readline().split()))

d = dict()
for i in n_list:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in m_list:
    if i in d.keys():
        print(d[i], end=' ')
    else:
        print(0, end=' ')