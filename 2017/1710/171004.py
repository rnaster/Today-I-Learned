# BOJ - 11055
def foo():
    from sys import stdin, stdout
    from array import array
    read = lambda: stdin.readline().rstrip()
    n = int(read())
    tp = tuple(map(int, read().split()))
    m = tp[0]
    arr = array('L', [0 for _ in range(n)])
    for i in range(n):
        arr[i] = tp[i]
        for j in range(i):
            if tp[j] < tp[i] and arr[i] < arr[j] + tp[i]:
                arr[i] = arr[j] + tp[i]
        m = max(m, arr[i])
    stdout.write(str(m)+'\n')

# num = int(input())
# seq = list(map(int, input().split()))
# dic = {seq[0]: seq[0]}
#
# for idx in range(1, num):
#     key = seq[idx]
#     check = [x for x in list(dic.keys()) if x < key]
#
#     if check:
#         dic[key] = max([dic[x] for x in check]) + key
#     else:
#         dic[key] = key
#
# print(max(dic.values()))

# BOJ - 3017
from sys import stdin, stdout
from array import array
read = lambda: stdin.readline().rstrip()
tp1 = tuple(read())
tp2 = tuple(read())
