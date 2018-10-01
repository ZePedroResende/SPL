#!/usr/local/bin/python3.7
import re
import sys
from PeriodicTable import table

tableKeys = list(map(lambda x: x.lower(), table.keys()))
def regexBuilder():
    sortedTableKeys =  sorted(tableKeys, key=len, reverse=True)
    return re.compile('('+'|'.join(sortedTableKeys)+')')


def wordToElements(word):
    split = re.split(match,word)
    return '-'.join(filter(None, [ s for s in split if s in tableKeys ] ))



match = regexBuilder()
for file in sys.argv[1:]:
    with open(file,"r") as f:
        write = file+".elem"
        with open(write, "w") as w:
            lines = f.readlines()
            for line in lines:
                w.write(wordToElements(line)+"\n")
