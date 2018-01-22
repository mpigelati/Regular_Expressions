import re
allinform =re.findall("inform","we need to inform hime with the latest information")

#for i in allinform:
#    print(i)


str="Sat, hat, pat,sat,mat"

allstr =re.findall("[shmp]at",str)

#for i in allstr:
 #   print(i)


allstr1=re.findall("[h-m]at",str)
#for i in allstr1:
#    print(i)

allstr1=re.findall("[h-z]at",str)
#for i in allstr1:
#    print(i)

allstr1=re.findall("[^h-m]at",str)
for i in allstr1:
    print(i)


