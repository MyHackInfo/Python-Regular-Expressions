import re
strings='yes i am ready for do this work of code 47'
work=re.findall(r'\d{1,1}',strings)
name=re.findall(r'[a-z]*',strings)
print(name)
print(work)


