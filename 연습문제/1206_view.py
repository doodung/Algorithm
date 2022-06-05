T = 10
dx = [-2, -1, 1, 2]
for test_case in range(1, T + 1):
    N = int(input())
    apartment = list(map(int, input().split()))
    apart = [0] * N
    for a in range(2, N):
        temp = apartment[a - 2:a]
        temp.extend(apartment[a + 1:a + 3])
        m_temp = max(temp)
        if apartment[a] > m_temp:
            apart[a] = apartment[a] - m_temp
    print('#%d %d' %(test_case,sum(apart)))
