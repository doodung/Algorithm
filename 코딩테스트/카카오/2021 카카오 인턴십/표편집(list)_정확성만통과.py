def solution(n, k, cmd):
    q = []
    for i in range(n):
        q.append(i)
    first = q
    temp = []
    this = k
    for i in range(len(cmd)):
        if len(cmd[i]) > 1:
            ud, num = map(str, cmd[i].split())  # 명령어, 숫자
            num = int(num)
            if ud == 'U':
                this -= num
                continue
            if ud == 'D':
                this += num
                continue
        else:
            ud = cmd[i]
            if ud == 'C':
                t = q[this]
                del q[this]
                temp.append([this, t])
                if this == len(q):
                    this -= 1
                continue
            if ud == 'Z':
                tx, tn = temp.pop()
                if tx <= this:
                    this += 1
                q.insert(tx, tn)
                continue

    answer = ''
    for i in range(n):
        if i in q:
            answer += 'O'
        else:
            answer += 'X'
    return answer