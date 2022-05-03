Operator = ['+','-','/','*']
for i in range(int(input('Enter Number Of Line: '))):
    Expression = list(map(str, input('Enter Expression: ').strip().split()))
    for i in range(len(Expression)-1):
        if Expression[i+1] in Operator:
            print("MOV R1 ", Expression[i])
            print("MOV R2 ", Expression[i+2])
            if Expression[i+1] == '+':
                print("ADD R1, R2 ")
            elif Expression[i+1] == '-':
                print("SUB R1, R2 ")
            elif Expression[i+1] == '*':
                print("MULT R1, R2 ")
            elif Expression[i+1] == '+':
                print("DIV R1, R2 ")
            else:
                print('Please Enter Valid Expression')

# Enter Number Of Line: 1
# Enter Expression: t =  a + b
# MOV R1  a
# MOV R2  b
# ADD R1, R2