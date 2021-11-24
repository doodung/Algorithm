from collections import deque


def solution(board, moves):
    temp = deque()
    j, k, answer = 0, 0, 0
    length = len(moves)

    for i in range(0, length):
        for j in range(0, len(board)):
            if (board[j][moves[i] - 1] == 0):
                continue
            else:
                temp.append(board[j][moves[i] - 1])
                k += 1
                if (len(temp) >= 2):
                    if (temp[k - 2] == temp[k - 1]):
                        temp.pop()
                        temp.pop()
                        k -= 2
                        answer += 2
                board[j][moves[i] - 1] = 0
                break

    return answer