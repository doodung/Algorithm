from collections import deque

# 20055 컨베이어 벨트 위의 로봇
# 2022-04-07 doodung
# 129812kb, 1540ms

N, K = map(int, input().split())
convey = deque(list(map(int, input().split())))
robot = deque([0] * N)

answer = 0
while convey.count(0) < K:
    convey.rotate(1)  # 컨베이어 queue 회전
    robot.rotate(1)  # 로봇 queue 회전
    robot[-1] = 0  # 마지막칸은 항상 내려가는 자리이므로 0
    if sum(robot):  # 로봇이 존재하면
        for idx in range(N - 2, -1, -1):  # 내려가는 부분 이전의 위치에 존재하는 로봇들을 움직인다.
            if robot[idx] and not robot[idx + 1] and convey[idx + 1]:
                convey[idx + 1] -= 1
                robot[idx + 1], robot[idx] = 1, 0
        robot[-1] = 0  # 마지막칸은 항상 내려가는 자리이므로 0

    if not robot[0] and convey[0]:  # 올라가는 자리에 로봇을 올려놓을 수 있으면 로봇을 올린다.
        robot[0] = 1
        convey[0] -= 1

    answer += 1

print(answer)