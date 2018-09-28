import re
from PeriodicTable import table

tableKeys = list(map(lambda x: x.lower(), table.keys()))
sortedTableKeys =  sorted(tablekeys, key=len, reverse=True)
print(sortedTablekeys)
string = input("dada uma string\n").lower()
match = re.compile('('+'|'.join(sortedTablekeys)+')')
split = re.split(match,string)
print(split)
res = '-'.join(filter(None,split))
print(res)
