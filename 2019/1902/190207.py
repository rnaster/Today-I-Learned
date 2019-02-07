# BOJ - 10798
grid = []
l = []
for i in range(5):
    s = input()
    l.append(len(s))
    grid.append(s)
for i in range(max(l)):
    for j in range(5):
        if i+1 <= l[j]:
            print(grid[j][i], end='')
"""
ABCDE
abcde
01234
FGHIJ
fghij

Aa0FfBb1GgCc2HhDd3IiEe4Jj
Aa0FfBb1GgCc2HhDd3IiEe4Jj

AABCDD
afzz
09121
a8EWg6
P5h3kx

Aa0aPAf985Bz1EhCz2W3D1gkD6x
Aa0aPAf985Bz1EhCz2W3D1gkD6x

a
bc
efg
1234
wxyzk

wxyzk
1234
efg
bc
a
"""
exit()

# BOJ - 1159
n = int(input())
d = {}
ans = []
for _ in range(n):
    a = input()
    if a[0] in d.keys():
        d[a[0]] += 1
    else: d[a[0]] = 1
for dd in d:
    if d[dd] > 4: ans.append(dd)
if ans:
    for ans_ in sorted(ans):
        print(ans_, end='')
else: print('PREDAJA')
"""
18
babic
keksic
boric
bukic
sarmic
balic
kruzic
hrenovkic
beslic
boksic
krafnic
pecivic
klavirkovic
kukumaric
sunkic
kolacic
kovacic
prijestolonasljednikovi
"""