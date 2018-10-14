import re
print('Special char')
strings='you are 47 -21 is 4.56 ab453457 not good. or'
print(re.findall(r'\Ayou',strings))
print(re.findall(r'\b',strings))
print(re.findall(r'\B',strings))
print(re.findall(r'\d',strings))
print(re.findall(r'\D',strings))
print(re.findall(r'\s',strings))
print(re.findall(r'\S',strings))
print(re.findall(r'\w',strings))
print(re.findall(r'\W',strings))
print(re.findall(r'or\Z',strings))

