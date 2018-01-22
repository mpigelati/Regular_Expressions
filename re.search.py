import re

if re.search("inform","we need to inform him with latest informatin"):
    print("there is inform:")

randstr = "he is \\drogba"
#print(randstr)

print(re.search(r'\\drogba',randstr))