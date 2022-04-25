import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline()


#   중복순열 구하기
#   1부터 N까지 번호가 적힌 구술이 있다.
#   이 중 중복을 허락하여 M번을 뽑아 나열하는 방법을 모두 출력하라
#   구슬 1 2 3 -> 두개를 뽑음
def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            res[L] = i
            DFS(L + 1)


#         D(0)       -> dfs
#      1   2   3     -> i
#     D(1)
#   1  2  3
# D(2)
# ----- stack -------
#   3. D(2)  ---> 출력 1 1
#   2. D(1)
#   1. D(0) ---> 15line


if __name__ == "__main__":
    n, m = map(int, input.split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)
