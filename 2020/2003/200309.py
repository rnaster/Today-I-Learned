# BOJ - 1756
from bisect import bisect_right as bi
from itertools import accumulate
d, n = map(int, input().split())
arr = [*map(lambda x: -int(x), input().split())]
arr = [*accumulate(arr, max)]
l = [*map(int, input().split())]
ans = d+1
i = 0
while ans > 0 and i < n:
    ans = bi(arr, -l[i], 0, ans-1)
    i += 1
print(ans)
"""
7 4
5 4 4 3 6 2 3
3 99 5 4

7 3
1 2 3 4 5 6 7
1 2 3
"""
exit()

# BOJ - 6581
import sys
read = sys.stdin.readline
write = sys.stdout.write
arr = []
for line in sys.stdin:
    arr.extend(line.strip().split())
l = []
i = 80
for a in arr:
    if a == '<br>':
        write(' '.join(l + ['\n']))
        l = []
        i = 80
    elif a == '<hr>':
        if l:
            write(' '.join(l + ['\n']))
        write('-' * 80 + '\n')
        l = []
        i = 80
    elif i - len(a) -1 < 0:
        write(' '.join(l + ['\n']))
        l = [a]
        i = 80 - len(a)
    else:
        l.append(a)
        i -= len(a) + 1
write(' '.join(l))
"""
Hallo, dies ist eine 
ziemlich lange Zeile, die in Html
aber nicht umgebrochen wird.
<br>
Zwei <br> <br> produzieren zwei Newlines. 
Es gibt auch noch das tag <hr> was einen Trenner darstellt.
Zwei <hr> <hr> produzieren zwei Horizontal Rulers.
Achtung       mehrere Leerzeichen irritieren

Html genauso wenig wie


mehrere Leerzeilen.
"""