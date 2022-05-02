FileDataForMDTIndex = open('H:\\SPCC\\4\\macro.asm','r')
ListForMDTIndex = FileDataForMDTIndex.read().split('\n')
print('{:<8} {:<15} '. format('Index', 'MDT Instruction'))
index = 0
for i in  range(len(ListForMDTIndex)):
    if ListForMDTIndex[i] == 'MACRO':
        while True:
            index += 1
            if ListForMDTIndex[i] == 'MEND':
                print('{:<8} {:<15} '. format(index, ListForMDTIndex[i]))
                break
            elif ListForMDTIndex[i] == 'MACRO':
                index -= 1
            else:
                print('{:<8} {:<15} '. format(index, ListForMDTIndex[i]))
            i += 1
             



