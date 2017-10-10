def foo():
    # BOJ - 2577
    from collections import Counter
    num = int(input())*int(input())*int(input())
    count = Counter(str(num))
    for i in range(10):
        if str(i) in count:
            print(count.get(str(i)))
        else:
            print('0')

    # BOJ - 14501
    from array import array
    dp = array('L', [0 for _ in range(16)])
    n = int(input())
    for i in range(1, n+1):
        tp = tuple(map(int, input().split()))
        dp[i] = max(dp[i], dp[i-1])
        if i + tp[0]-1 <= n:
            dp[i+tp[0]-1] = max(dp[i+tp[0]-1], dp[i-1] + tp[1])
    print(dp[n])