# BOJ - 1107
n = input()
nn = len(n)
m = int(input())
if n == '100': print(0);exit()
if m == 0: print(min(abs(int(n)-100), nn));exit()
l = [i for i in range(10)]
for i in map(int, input().split()):
    l.remove(i)
a, b = min(l), max(l)
if m == 10: print(abs(int(n)-100));exit()
p, q = '', ''
if n[0] == '1':

"""
5457
3
6 7 8

100
5
0 1 2 3 4

500000
8
0 2 3 4 6 7 8 9
"""