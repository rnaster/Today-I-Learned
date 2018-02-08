# BOJ - 2504
from sys import stdin
read = lambda: stdin.readline().rstrip()
s = (read())
stack = []
for i in s:
    if i == ']' or i == ')':
        num = 0
        while True:
            val = stack.pop()
            if type(val) == int: num += val
            else:
                if i == ']' and val == '[':
                    if num: stack.append(num*3)
                    else: stack.append(3)
                elif i == ')' and val == '(':
                    if num: stack.append(num*2)
                    else: stack.append(2)
                else: print(0);quit()
                break
    else:
        stack.append(i)

ans = 0
for n in stack:
    if type(n) == int:
        ans += n
    else:
        print(0); quit()
print(ans)

'''
(()[[]])([])
'''