import sys

sys.stdin = open("input.txt.", "r")


def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ')  # 전위 순회 방식 (DFS의 대부분 방식)
        DFS(v * 2)  # 왼쪽자식
        print(v, end=' ')  # 중위 순회 방식
        DFS(v * 2 + 1)  # 오른쪽자식
        print(v, end=' ')  # 후위 순회 방식 (병합정렬)


if __name__ == "__main__":
    DFS(1)
