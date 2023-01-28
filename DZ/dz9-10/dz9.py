import re
abc = 'Холодько'
p = re.compile('о')
print(len(p.findall(abc)))