# 2212 센서
# 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야함
# 0 이상
N = int(input())
# N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야함
K = int(input())
# 최대 K개의 집중국을 세울 수 있음
board = sorted(list(map(int, input().split())))
temp = []
if K >= N:
    print(0)
else:
    for i in range(1, N):
        temp.append(board[i] - board[i-1])
    temp.sort(reverse=True)
    for _ in range(K-1):
        temp.pop(0)
    print(sum(temp))