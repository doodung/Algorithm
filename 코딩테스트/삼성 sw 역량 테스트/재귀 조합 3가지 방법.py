import time


def comb_type1(arr, cnt):
    if cnt == 1:
        for i in range(len(arr)):
            yield [arr[i]]
    else:
        for i in range(len(arr)):
            for nxt in comb_type1(arr[i + 1:], cnt - 1):
                yield [arr[i]] + nxt


def comb_type2(arr, ret, cache, cnt, idx):
    if cnt == 1:
        for i in arr[idx:]:
            ret.append(cache + [i])
    else:
        comb_type2(arr, ret, cache + [arr[idx]], cnt - 1, idx + 1)
        if len(arr) - idx > cnt:
            comb_type2(arr, ret, cache, cnt, idx + 1)


def comb_type3(arr, r):
    used = [0 for _ in range(len(arr))]
    c = []

    def generate(chosen):
        if len(chosen) == r:
            c.append(chosen.copy())
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0

    generate([])
    return c


def solution():
    st = time.time()
    for _ in comb_type1(list(range(100)), 3):
        pass
    print(time.time() - st)

    st = time.time()
    res = []
    comb_type2(list(range(100)), res, [], 3, 0)
    print(time.time() - st)

    st = time.time()
    comb_type3(list(range(100)), 3)
    print(time.time() - st)


if __name__ == "__main__":
    solution()