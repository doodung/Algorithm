class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None


def solution(n, k, cmd):
    nodeArr = [Node() for _ in range(n)]
    for i in range(1, n):
        nodeArr[i - 1].next = nodeArr[i]
        nodeArr[i].prev = nodeArr[i - 1]

    curr = nodeArr[k]
    mystack = []

    for str in cmd:
        if str[0] == 'U':
            x = int(str[2:])
            for _ in range(x):
                curr = curr.prev
        elif str[0] == 'D':
            x = int(str[2:])
            for _ in range(x):
                curr = curr.next
        elif str[0] == 'C':
            mystack.append(curr)
            curr.removed = True
            up = curr.prev
            down = curr.next
            if up:
                up.next = down
            if down:
                down.prev = up
                curr = down
            else:  # 삭제된행이마지막행
                curr = up
        else:  # Z
            node = mystack.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up:
                up.next = node
            if down:
                down.prev = node

    answer = ''
    for i in range(n):
        if nodeArr[i].removed:
            answer += 'X'
        else:
            answer += 'O'
    return answer