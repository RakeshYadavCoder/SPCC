from string import punctuation
FileData = open("H:\\SPCC\\3\\Program.txt", 'r')
ListData = FileData.read().split('\n')
mnemonic = ['AREG','BREG','CREG','ORIGIN','LTORG','ADD','SUB','MULT','DIV','COMP','MOVEM','MOVER','DS','DC', 'STOP', 'END']
Address , Index = 0, 0
SymbolTable = open('SymbolTable.txt','w')
SymbolTable.write("{:<10}{:<15}{:<10}".format("Index","Symbol","Address")+'\n')
SymbolSet = set()          
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
                SymbolTable.write("{:<10}{:<15}{:<10}".format(Index,j,Address)+'\n')
    Address += 1
 
