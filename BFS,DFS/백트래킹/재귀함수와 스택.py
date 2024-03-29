import sys

sys.stdin = open("input.txt", "r")


# 재귀함수와 스택
def DFS(x):
    if x > 0:
        print(x)  # 3,2,1 호출
        DFS(x - 1)
        print(x)  # 1,2,3 호출


if __name__ == "__main__":
    n = int(input())
    DFS(n)

# DFS(3) 작동
#             |                  |
#             |                  |
#             |                  |
#             | 매개변수 x=3      |
#             | 지역변수          |
#             | 복귀주소 main-12  |   --->  스택영역에 기록된다.
#             |_________________|
#
# DFS(3) 작동 후 DFS(3-1)-> DFS(2) 호출
# DFS(2) 작동
#             |                  |
#   DFS(2)    | x=2              |
#             | 복귀주소 D(3)     |
#   DFS(3)    | 매개변수 x=3-6라인 |
#             | 지역변수          |
#             | 복귀주소 main-12  |   --->  스택영역에 기록된다.
#             |_________________|
#
# DFS(2) 작동 후 DFS(2-1)-> DFS(1) 호출
# DFS(1) 작동
#             |                  |
#   DFS(1)    | x= 1             |
#             | 복귀주소 D(2)-6라인|
#   DFS(2)    | x= 2             |
#             | 복귀주소 D(3)-6라인|
#   DFS(3)    | 매개변수 x=3-6라인 |
#             | 지역변수          |
#             | 복귀주소 main-12  |   --->  스택영역에 기록된다.
#             |_________________|
#
# DFS(1) 작동 후 DFS(1-1)-> DFS(0) 호출
# DFS(0) 작동
#             |                  |
#   DFS(0)    | x= 0             |
#             | 복귀주소 D(1)-6라인|
#   DFS(1)    | x= 1             |
#             | 복귀주소 D(2)-6라인|
#   DFS(2)    | x= 2             |
#             | 복귀주소 D(3)-6라인|
#   DFS(3)    | 매개변수 x=3-6라인 |
#             | 지역변수          |
#             | 복귀주소 main-12  |   --->  스택영역에 기록된다.
#             |_________________|
# 호출 끝난 후 복귀주소를 보면서 복귀
# DFS(0) -> DFS(1) print(1) -> DFS(2) print(1) -> DFS(3) print(3)
# main 12 라인으로 최종 복귀
