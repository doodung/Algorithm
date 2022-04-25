import sys

sys.stdin = open("input.txt", "r")


#   D(11)-> 1출력 ->  D(5) -> 1출력 -> D(2)-> 0 출력 -> D(1) -> 1출력 -> D(0) -> return


def DFS(x):
    if x == 0:
        return
    else:
        print(x % 2, end=' ')  # -> 1 1 0 1 출력
        DFS(x // 2)
        print(x % 2, end=' ')  # -> 1 0 1 1 출력


if __name__ == "__main__":
    n = int(input())
    DFS(n)
