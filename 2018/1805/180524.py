# BOJ - 2309
import sys
l = []
for _ in range(9):
    l.append(int(input()))
for i in range(9):
    for j in range(i+1, 9):
        if sum(l) - l[i] - l[j] == 100:
            a, b = l[i], l[j]
            l.remove(a)
            l.remove(b)
            l.sort()
            for n in l:
                print(n)
            sys.exit()

'''
20
7
23
19
10
15
25
8
13
'''