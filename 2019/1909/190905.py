# programmers - 2018 kakao blind 무지의 먹방
food_times = [3, 1, 2]
k = 5
def solution(food_times, k):
    if sum(food_times) <= k: return -1
    idx = {}
    for i, f in enumerate(food_times):
        if f in idx:
            idx[f].append(i)
        else:
            idx[f] = [i]
    food = sorted(idx.keys())
    a = 0
    sz = len(food_times)
    for f in food:
        _f = f - a
        a += _f
        if sz * _f > k:
            _, b = divmod(k, sz)
            l = []
            for v in idx.values():
                l += v
            return sorted(l)[b] + 1
        else:
            k -= sz * _f
            sz -= len(idx[f])
            del idx[f]