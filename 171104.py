# BOJ - 2602
from sys import stdin
read = lambda: stdin.readline().rstrip()
magic = read()
bridge1 = read()
bridge2 = read()
ans = 0
def main(w1, w2, t):
    global ans
    if w1 != '' and t != '':
        if w1[0] == t[0]:
            main(w2[1:], w1[1:], t[1:])
        main(w1[1:], w2[1:], t)
    elif t == '': ans += 1
main(bridge1, bridge2, magic)
main(bridge2, bridge1, magic)
print(ans)


'''
RRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
'''