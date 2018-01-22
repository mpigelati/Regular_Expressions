import re

str= "we need to inform him with latest information"
for i in re.finditer("inform",str):
    print(i)
