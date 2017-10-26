from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
def main(n):
    # n = int(read())
    arr = array('L', [])
    f = lambda x: x*(x+1)*(x+2)//6
    for i in range(1, 121):
        if f(i) <= n:
            arr.append(f(i))
        else: break
    ans = n+1
    for i in range(len(arr)-1, -1, -1):
        N = n
        s = 0
        for j in range(i, -1, -1):
            s += N // arr[j]
            N = N % arr[j]
            # print(s, N, arr[j])
            if N == 0: break
        # print()
        ans = min(ans, s)
    print(ans, arr, n)

# 백준 ㅡㅡ
for i in range(1, 101):
    main(i)
'''
'''
