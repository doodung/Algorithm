import sys

sys.stdin = open("input.txt", "r")


def DFS(L, s, tsum):
    global result
    # 판단을 한 바둑이들을 따로 누적을 한다.:tsum
    # total-tsum -> 앞으로 판단할 바둑이들의 무게가 나온다.
    # sum + (total-tsum) : 이랬는데 result 보다 작다면, 내려갈 필요가 없다.
    if s+(total-tsum)<result:
        return
    if s > c:
        return
    if L == n:
        if s > result:
            result = s  # 전체집합의 값
    else:
        DFS(L + 1, s + a[L], tsum+a[L])  # 참여시킴
        DFS(L + 1, s, tsum+a[L])  # 참여시키지 않음


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0] * n  # 바둑이 각각의 무게 저장
    result = -214700000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)
