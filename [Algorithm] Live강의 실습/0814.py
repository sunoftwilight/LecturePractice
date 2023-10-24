'''
6528-*2/+
'''

stack = [0] * 100
top = -1

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

fx = '(6+5*(2-8)/2)'
susik = ''

for x in fx:
    if x not in '(+-*/)':
        susik += x

    elif x == ')':
        while stack[top] != '(':
            susik += stack[top]
            top -= 1
        top -= 1

    else:
        if top == -1 or isp[stack[top]] < icp[x]:   # 토큰의 우선 순위가 더 높으면
            top += 1
            stack[top] = x

        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -=1
            top += 1
            stack[top] = x

print(susik)
# susik = '6528-*2/+'

for x in susik:
    if x not in '+-/*':
        top += 1
        stack[top] = int(x)

    else: # 먼저 꺼낸 애(op1)를 연산자의 오른쪽에 (op1 + op2)
        op2 = stack[top]
        top -= 1
        op1 = stack[top]
        top -= 1

        if x == '+':
            top += 1
            stack[top] = op1 + op2

        elif x == '-':
            top += 1
            stack[top] = op1 - op2

        elif x == '/':
            top += 1
            stack[top] = op1 / op2

        elif x == '*':
            top += 1
            stack[top] = op1 * op2

print(stack[top])
