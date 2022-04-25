import sys

sys.stdin = open("input.txt", "r")


# a = 1,3,5,6,7,10
# L은 a의 인덱스 번호 0~5이자 레벨을 뜻함.
#                          D(0,0)
#                       /        \
#                    D(1,1)      D(1,0)
#                   /     \     /     \
#                D(2,4) D(2,1) ..     ..
#               /     \
#           D(3,9)  D(3,4)

def DFS(L, sum):
    if L == n:
        if sum > total//2:
            return
        if sum == (total - sum):  # 부분집합의 합 == 또다른 부분집합의 합
            print("YES")
            sys.exit(0)  # 프로그램 종료
    else:
        DFS(L + 1, sum + a[L])  # a[L] 원소 사용
        DFS(L + 1, sum)  # a[L] 원소 사용하지 않겠다


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")
