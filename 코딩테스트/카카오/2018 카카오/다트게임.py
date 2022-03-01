def solution(dartResult):
    num = []
    temp = ''
    print(dartResult)
    for i in dartResult:
        if i.isdigit():
            temp += i
        elif i == 'S':
            num.append(int(temp) ** 1)
            temp = ''
        elif i == 'D':
            num.append(int(temp) ** 2)
            temp = ''
        elif i == 'T':
            num.append(int(temp) ** 3)
            temp = ''
        elif i == '*':
            if len(num) >= 2:
                num[-1] = num[-1] * 2
                num[-2] = num[-2] * 2
            else:
                num[0] = num[0] * 2
        elif i == '#':
            num[-1] = -num[-1]

    return sum(num)