# BOJ - 1085
def BOJ1085():
    x, y, w, h = map(int, input().split())
    print(min(x, y, w-x, h-y))

# BOJ - 2851
def BOJ2851():
    ans = 0
    for _ in range(10):
        n = int(input())
        if abs(ans - 100) >= abs(ans + n - 100):
            ans += n
        else:
            break
    print(ans)

