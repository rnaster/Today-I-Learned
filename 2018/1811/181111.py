# BOJ - 2616
n = int(input())
tp = tuple(map(int, input().split()))
m = int(input())
ans = 0
dp = tuple(sum(tp[i:i+m]) for i in range(n - m + 1))
# print(dp, '*******')
dpdp = [0] * m
dp_ = dp[m:]
for i in range(len(dp_)-m):
    dpdp.append(dp_[i] + max(dp_[i+m:]))
for i in range(n - 3 * m + 1):
    if len(dpdp) >= i + m:
        ans = max(ans, dp[i] + max(dpdp[i+m:]))
print(ans)
# for i in range(n - 3 * m + 1):
#     # a = dp[i]
#     dp_ = dp[-len(dp)+i+m:]
#     for j in range(len(dp_)-m):
#         # b = dp_[j],
#         # dp__ = dp_[j+m:]
#         ans = max(ans, dp[i]+dp_[j]+max(dp_[j+m:]))
#         # for k in range(len(dp__)):
#         #     # c = dp__[k]
#         #     # print(a, b, c);exit()
#         #     # print('###########\n')
#         #     ans = max(ans, dp[i]+dp_[j]+dp__[k])
# print(ans)
# def main(n_, m_):
#     ans = 0
#     tp_ = tp[-n_:]
#     if m_ == 1:
#         for i in range(n_):
#             ans = max(ans, sum(tp_[i:i+k]))
#     else:
#         for i in range(n_ - m_*k + 1):
#             ans = max(ans, sum(tp_[i:i+k]) + main(n_-i-k, m_-1))
#     return ans
# print(main(n, 3))
"""
7
35 40 50 10 30 45 60
2
"""