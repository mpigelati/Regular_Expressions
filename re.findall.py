import re

Name='''"Mohansai is 32 and Thanuja is 26 and Lekshana is 3 and Sakethram is 12'''

ages =re.findall(r'\d{1,3}',Name)

names =re.findall(r'[A-Z][a-z]*',Name)

ageDict={}
x=0

for eachname in names:
    ageDict[eachname]=ages[x]
    x=x+1
    #x+=1
print(ageDict)
