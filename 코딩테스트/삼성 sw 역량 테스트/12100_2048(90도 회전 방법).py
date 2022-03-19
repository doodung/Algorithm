from copy import deepcopy

# 12100 2048
# 2022-03-19 doodung

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]


def rotate(b, N):
    nb = deepcopy(b)
    for i in range(N):
        for j in range(N):
            nb[j][N - i - 1] = b[i][j]
    return nb


# 한 행 합쳐주기
def convert(lst, N):
    new_list = [i for i in lst if i]
    for i in range(1, len(new_list)):
        # 합치기
        if new_list[i - 1] == new_list[i]:
            new_list[i - 1] *= 2
            new_list[i] = 0

    new_list = [i for i in new_list if i]
    # 나머지 부분을 0으로 다 채워줌
    return new_list + [0] * (N - len(new_list))


def dfs(N, b, cnt):
    # 최대값
    ret = max([max(i) for i in b])
    # 횟수 사용 다 했을 때
    if cnt == 0:
        return ret

    # 회전1번 컨버트1번 -> 4 방향
    for _ in range(4):
        # 행 합친 것을 반복하여 모든 행에 대해서 수행한 x 배열
        x = [convert(i, N) for i in b]
        # 기존의 모양과 다른 경우 -> 합치기 가능한 경우
        if x != b:
            # 기존의 배열과 같은 경우 나올때까지 dfs
            ret = max(ret, dfs(N, x, cnt - 1))
        # 기존의 배열과 같은 경우 회전 -> 더이상 합치기가 수행안될 떄
        b = rotate(b, N)
    return ret


print(dfs(N, board, 5))
