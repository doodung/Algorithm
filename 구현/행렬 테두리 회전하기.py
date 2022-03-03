def solution(rows, columns, queries):
    answer = []
    board = [[0 for i in range(columns + 1)] for j in range(rows + 1)]
    num = 1
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            board[row][column] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        tmp = board[x1][y1]
        mini = tmp

        # 좌
        for x in range(x1, x2):
            test = board[x + 1][y1]
            board[x][y1] = test
            mini = min(mini, test)

        # 아래
        for y in range(y1, y2):
            test = board[x2][y + 1]
            board[x2][y] = test
            mini = min(mini, test)

        # 우
        for x in range(x2, x1, -1):
            test = board[x - 1][y2]
            board[x][y2] = test
            mini = min(mini, test)

        # 위
        for y in range(y2, y1, -1):
            test = board[x1][y - 1]
            board[x1][y] = test
            mini = min(mini, test)

        board[x1][y1 + 1] = tmp
        answer.append(mini)

    return answer