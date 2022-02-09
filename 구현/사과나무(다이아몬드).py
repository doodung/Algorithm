import sys

#sys.stdin = open("input.txt", "rt")
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

start = N // 2
end = N // 2
apple = 0

for i in range(N):
    for j in range(start, end + 1):
        apple += board[i][j]

    if i < N // 2:
        start -= 1
        end += 1

    else:
        start += 1
        end -= 1

print(apple)
