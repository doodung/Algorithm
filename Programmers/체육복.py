def solution(n, lost, reserve):
    result = 0

    _reserve = list(set(reserve) - set(lost))
    _lost = list(set(lost) - set(reserve))

    for i in range(0, len(_reserve)):
        if _reserve[i] - 1 in _lost:
            _lost.remove(_reserve[i] - 1)
        elif _reserve[i] + 1 in _lost:
            _lost.remove(_reserve[i] + 1)

    if len(_lost) == 0:
        result = n
    else:
        result = n - len(_lost)

    return result