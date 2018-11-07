# BOJ - 1254
s = input()
ss = len(s)
if ss == 1: print(1);exit()
def func(s_, ss_):
    for i in range(ss_//2):
        if s_[i] != s_[-(i+1)]: return False
    return True
ans = 0
for j in range(ss-1):
    if func(s[j:], ss-j): print(ans+ss);exit()
    else: ans += 1
print(ans+ss)