import sys

# sys.stdin = open("input.txt", "rt")
N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
money = [0] * N

for i in range(N):
    first = dice[i][0]
    second = dice[i][1]
    third = dice[i][2]

    if first == second == third:
        money[i - 1] = 10000 + first * 1000

    elif first == second or first == third:
        money[i - 1] = 1000 + first * 100

    elif second == third:
        money[i - 1] = 1000 + second * 100

    elif first != second != third:
        tmp = max(first, second, third)
        money[i - 1] = tmp * 100

print(max(money))
