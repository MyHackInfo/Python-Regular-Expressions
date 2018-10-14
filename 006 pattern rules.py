import re
print(" pattern rules")

print(re.findall(r'xy*' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'xy+' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'.' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'^t' , 'this is string'))
print(re.findall(r'g$' , 'this is string'))
print(re.findall(r'xy?' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'yy+?' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'x{2,}' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'xy{1,3}' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'[a-x]' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'[^x]' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'[x^]' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'y|x' , 'xyyxxxxxyyyyxxxxxyy'))
print(re.findall(r'(yxx)' , 'xyyxxxxxyyyyxxxxxyy'))

