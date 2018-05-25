# BOJ - 2591
import sys
n = int(input())
q = 0
while True:
    if n // (10 ** q) < 10: break
    else: q += 1
def main(n, q):
    print(n, q)
    if n // (10 ** (q - 2)) < 10: print(0); sys.exit()
    if n == 0: return 0
    if 1 <= n <= 10: return 1
    if n <= 34: return 2
    else:
        ans = 0
        if n // (10 ** q) < 10: ans += main(n % (10 ** q), q - 1)
        if n // (10 ** (q-1)) <= 34: ans += main(n % (10 ** (q - 1)), q - 2)
        return ans
print(main(n, q))
'''
27123
'''