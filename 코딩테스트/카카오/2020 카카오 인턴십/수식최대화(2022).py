def solution(expression):
    op = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+']]
    result = []
    array = []
    tmp = ''

    for i in expression:
        if i.isdigit():
            tmp += i
        else:
            array.append(tmp)
            array.append(i)
            tmp = ''
    array.append(tmp)

    tmp = ''
    result = []
    for i in op:
        _array = array[:]
        for j in i:
            while j in _array:
                tmp = _array.index(j)
                _array[tmp - 1] = str(eval(_array[tmp - 1] + _array[tmp] + _array[tmp + 1]))
                _array = _array[:tmp] + _array[tmp + 2:]
        result.append(_array[-1])
    return max(abs(int(x)) for x in result)