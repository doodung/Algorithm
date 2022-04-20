import sys
# pypy : 564ms, python : 시간초과

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]  # 겨울에 뿌릴 양분
board = [[5] * N for j in range(N)]  # 현재 양분 board
tree = [[[] for i in range(N)] for j in range(N)]  # 트리 정보

for i in range(M):
    x, y, age = map(int, input().split())
    tree[x - 1][y - 1].append(age)

ans = 0
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]


def springAndSummer():
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()
                temp_tree, dead_tree = [], 0
                for a in tree[i][j]:
                    if board[i][j] >= a:
                        board[i][j] -= a
                        a += 1
                        temp_tree.append(a)
                    else:
                        dead_tree += a // 2
                board[i][j] += dead_tree
                tree[i][j] = []
                tree[i][j].extend(temp_tree)

    if not tree:
        print(0)
        sys.exit()


def autumn():
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for a in tree[i][j]:
                    if a % 5 == 0:
                        for d in range(8):
                            nx = i + dx[d]
                            ny = j + dy[d]
                            if 0 <= nx < N and 0 <= ny < N:
                                tree[nx][ny].append(1)


def winter():
    for i in range(N):
        for j in range(N):
            board[i][j] += A[i][j]


while K > 0:
    springAndSummer()
    autumn()
    winter()
    K -= 1

for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])

print(ans)
