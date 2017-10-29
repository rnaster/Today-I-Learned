# BOJ - 4883
def foo():
    from sys import stdin
    read = lambda: stdin.readline().rstrip()
    def main():
        k = 0
        while True:
            n = int(read())
            if n <= 0: quit()
            else: k += 1
            tp1 = tuple(map(int, read().split()))
            tp2 = tuple(map(int, read().split()))
            L1 = tp1[1] + tp2[0]
            C1 = min(L1, tp1[1], sum(tp1[1:])) + tp2[1]
            R1 = min(C1, tp1[1], sum(tp1[1:])) + tp2[2]
            for _ in range(n-2):
                tp = tuple(map(int, read().split()))
                L2 = min(L1, C1) + tp[0]
                C2 = min(L1, L2, C1, R1) + tp[1]
                R2 = min(C1, C2, R1) + tp[2]
                L1, C1, R1 = L2, C2, R2
            print('%s. %s' %(k, C1))
    main()

