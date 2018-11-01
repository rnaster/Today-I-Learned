# BOJ - 2504
from collections import deque
s = tuple(input())
stack = deque()
for i in s:
    if i == ']' or i == ')':
        num = 0
        while len(stack):
            val = stack.pop()
            if isinstance(val, int): num += val
            else:
                if i == ']' and val == '[':
                    if num: stack.append(num*3)
                    else: stack.append(3)
                    break
                elif i == ')' and val == '(':
                    if num: stack.append(num*2)
                    else: stack.append(2)
                    break
                else: print(0);exit()
    else:
        stack.append(i)
ans = 0
while len(stack):
    a = stack.pop()
    if isinstance(a, int): ans += a
    else: print(0); exit()
print(ans)
"""
(()[[]])([])
"""