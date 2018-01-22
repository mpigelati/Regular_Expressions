import re

randstr ='''
keep the blue flag
 flying high 
 chelsea'''
regex =re.compile("\n")
#print(randstr)
randstr=regex.sub("",randstr)
#print(randstr)
#print("match")


randstr="12345"

#print("Match",len(re.findall("\d",randstr)))
#print("Match",len(re.findall("\D",randstr)))
#print("Match",len(re.findall("\d{5}",randstr)))


num= "123 123 1234 12345 123456"
print(num)
print("Match",len(re.findall("\d{5,7}",num)))