def solution(record):
    # 채팅방 나간 후 새로운 닉네임
    # 채팅방에서 닉네임을 변경
    user = {}
    answer = []
    for i in range(len(record)):
        k = record[i].split(' ')[1]
        if (record[i][0] == 'E') or (record[i][0] == 'C'):
            user[k] = record[i].split(' ')[2]

    for i in range(len(record)):
        k = record[i].split(' ')[1]
        if record[i][0] == 'E':
            answer.append(user[k] + "님이 들어왔습니다.")
        elif record[i][0] == 'L':
            answer.append(user[k] + "님이 나갔습니다.")

    return answer