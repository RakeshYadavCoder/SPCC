FileDataForMDTIndex = open('H:\\SPCC\\4\\macro.asm','r')
FileDataForMacroName = open('H:\\SPCC\\4\\macro.asm','r')
ListForMDTIndex = FileDataForMDTIndex.read().split('\n')
ListForMacroName = FileDataForMacroName.read().split()
outputlist = []
index = 0
print ("{:<8} {:<15} {:<10}".format('Index','Macro Name','MDT Index',))
for i in range(len(ListForMacroName)):
  if ListForMacroName[i] == 'MACRO':
    index += 1
    MacroName = ListForMacroName[i+1]
    for j in range(len(ListForMDTIndex)):
      if len(MacroName) <= len(ListForMDTIndex[j]):
        if MacroName == ListForMDTIndex[j][0:len(MacroName)]:
          if j > 1:
            print ("{:<8} {:<15} {:<10}".format(index,MacroName,j-1))
          else:
            print ("{:<8} {:<15} {:<10}".format(index,MacroName,j))
          

