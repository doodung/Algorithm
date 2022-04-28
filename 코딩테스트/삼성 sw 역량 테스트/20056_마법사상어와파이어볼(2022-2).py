# 20056 마법사 상어와 파이어볼
N, M, K = map(int, input().split())
fireball = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r - 1, c - 1, m, s, d])

# 파이어볼 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    board = [[[] for i in range(N)] for j in range(N)]
    # 파이어볼 이동
    for m in range(len(fireball)):
        x, y, mi, si, di = fireball[m]
        nx = (N +x+dx[di]*si)%N
        ny = (N+y + dy[di] * si)%N
        board[nx][ny].append([mi, si, di])
        fireball[m][0] = nx
        fireball[m][1] = ny

    # 파이어볼 이동 끝난 후
    L = 0
    temp, dir, new_fireball = [], [], []

    for i in range(N):
        for j in range(N):
            L = len(board[i][j])
            if L >= 2:
                all_m, all_s = 0, 0
                odd, even = 0, 0
                for mf, sf, df in board[i][j]:
                    all_m += mf
                    all_s += sf
                    if df % 2 == 0:
                        odd += 1
                    if df % 2 == 1:
                        even += 1
                if odd == L or even == L:
                    dir = [0, 2, 4, 6]
                else:
                    dir = [1, 3, 5, 7]
                if all_m//5:
                    for d in dir:
                        new_fireball.append([i, j, all_m // 5, all_s // L, d])
            if L==1:
                for mf, sf, df in board[i][j]:
                    new_fireball.append([i, j, mf, sf, df])
    fireball = new_fireball

ans = 0
for i in range(len(fireball)):
    ans += fireball[i][2]

print(ans)
