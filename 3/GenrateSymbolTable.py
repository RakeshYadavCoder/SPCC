from string import punctuation
FileData = open("H:\\SPCC\\3\\Program.txt", 'r')
ListData = FileData.read().split('\n')
mnemonic = ['AREG','BREG','CREG','ORIGIN','LTORG','ADD','SUB','MULT','DIV','COMP','MOVEM','MOVER','DS','DC', 'STOP', 'END']
Address , Index = 0, 0
print("{:<10}{:<10}{:<10}".format("Index","Symbol","Address"))
SymbolSet = set()
OutputList = []          
for i in ListData:
    for j in i.split():
        if j == 'START':
            Address = int(i.split()[-1]) - 1
        
        elif j in mnemonic or j.isnumeric() or j in punctuation or j.isdigit():
            pass

        else:
            if j not in SymbolSet:
                SymbolSet.add(j)
                Index += 1
                OutputList.append([Index,j,Address])
            else:
                if 'DS' in i.split() or 'DC' in i.split():
                    for k in OutputList:
                        if j in k:
                            Index = OutputList.index(k)
                            OutputList[Index][-1] = Address        
    Address += 1

for i in OutputList:
    IndexVal, Symbol, CurrAddress = i
    print("{:<10}{:<10}{:<10}".format(IndexVal,Symbol,CurrAddress))
 
