import re

email = "mohansai@gmail.com sakethram@gmail.com @sox.com"

email= "sk@aol.com md@.com @eoe.com dc@.com"
print("email matches ",len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-za-z]{2,3}",email)))