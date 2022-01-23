def solution(clothes):
    clo = {}
    answer = 1

    for name, kind in clothes:
        if kind in clo:
            clo[kind] += 1
        else:
            clo[kind] = 1

    for key, value in clo.items():
        answer *= (value + 1)

    answer -= 1
    return answer