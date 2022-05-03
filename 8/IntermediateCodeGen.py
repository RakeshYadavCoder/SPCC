Expression = str(input("Enter Expression: "))
post = []
ExpGenList = []
Precedence = {'+': 1, '-': 1, "*": 2, '/': 2}
OperatorList = []
for i in Expression:
    if i.isalpha():
        post.append(i)
    elif not OperatorList or Precedence[i] > Precedence[OperatorList[-1]]:
        OperatorList.append(i)
    else:
        y = OperatorList.pop()
        post.append(y)
        OperatorList.append(i)
ReverseOpList = OperatorList[::-1]
post.extend(ReverseOpList)

i = 1
for z in post:
    if z.isalpha():
        ExpGenList.append(z)
    else:
        right = ExpGenList.pop()
        left = ExpGenList.pop()
        print('t'+str(i), '=', left, z, right)
        ExpGenList.append('t' + str(i))
        i += 1

#i/o
# Enter Expression: A+B+C*D/S
# t1 = A + B
# t2 = C * D
# t3 = t2 / S
# t4 = t1 + t3