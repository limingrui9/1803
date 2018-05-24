import re


mm = 'c:\\a\\b\\c'
print("*"*50)
print(mm)

ret = re.match('c:\\\\',mm).group()
#print(ret)
print("*"*50)
print(ret)
#ret = re.match('')
