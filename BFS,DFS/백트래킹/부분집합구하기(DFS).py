import sys

sys.stdin = open("input.txt", "r")


# 1을 넣을건지 ,넣지 않을건지
# 2를 넣을건지 ,넣지 않을건지
# 3을 넣을건지 ,넣지 않을건지
# 총 8가지

def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1  # 1 사용한다 -> dfs 호출 -> 2 사용한다 -> dfs 호출 -> 3 사용한다 -> dfs 호출 -> 1 2 3 출력
        DFS(v + 1)  # dfs(2) 호출 -> dfs(3) 호출
        ch[v] = 0
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)  # 원소를 선택할건지, 안할건지 체크
    DFS(1)
