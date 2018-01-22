import re

#\w[a-zA-Z0-9]
#\W[a-zA-Z0-9]

phn = "412-555-1212"

if re.search("\w{3}-\w{3}-\w{4}",phn):
    print("it is a phone number")
if re.search("\d{3}-\d{3}-\d{4}",phn):
    print("it is a phone number")


#\s[\f\n\r\t\v]
#\S[^\f\n\r\t\v]

if re.search("\w{2,20}\S\w{2,20}", "mohansai pigelati"):
    print("full name is valid")
if re.search("\w{2,20}\s\w{2,20}", "mohansai pigelati"):
    print("full name is valid")