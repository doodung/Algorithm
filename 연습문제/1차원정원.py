T = int(input())
for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    D = D * 2 + 1
    answer = N // D
    if N % D != 0:
        answer += 1
    print('#%d %d' % (test_case, answer))
