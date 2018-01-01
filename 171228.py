# BOJ - 1697
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n, k = map(int, read().split())
cache = array('B', [0 for _ in range(max(k+2, n+2))])
queue = array('Q', [n])
count = 0
cache[n] = 1
while not k in queue:
    temp = array('Q', [])
    for i in queue:
        if i >= 1:
            if cache[i-1] == 0:
                temp.append(i-1); cache[i-1] = 1
        if i+1 <= k+1:
            if cache[i+1] == 0:
                temp.append(i+1); cache[i+1] = 1
        if i*2 <= k+1:
            if cache[i*2] == 0:
                temp.append(i*2); cache[i*2] = 1
    queue = temp[:]
    del temp
    count += 1
print(count)

'''
71 0
142 0
142 71
'''

# for i in range(0, 100001, 71):
#     for j in range(0, 100001, 71):
#         try:
#             main(i, j)
#         except: print(i, j)