#!/usr/local/bin/python3.7
import re
import sys
from PeriodicTable import table


def regexBuilder(tableKeys):
    sortedTableKeys =  sorted(tableKeys, key=len, reverse=True)
    return re.compile('('+'|'.join(sortedTableKeys)+')')


def wordToElements(word, tableKeys):
    split = re.split(regexBuilder(tableKeys), word)
    split = list(filter(None, split))
    for s in split:
        if s not in tableKeys :
            return None
    return '-'.join(split)

def readFiles(files):
    for file in files:
        with open(file,"r") as fRead:
            write = file+".elem"
            with open(write, "w") as fWrite:
                processLines(fRead, fWrite)

def processLines(fRead, fWrite):
    lines = fRead.read().splitlines()
    for line in lines:
        word = wordToElements(line, tableKeys)
        if word is not None :
            fWrite.write(word +"\n")


if __name__ == '__main__':
    tableKeys = list(map(lambda x: x.lower(), table.keys()))
    if len(sys.argv) > 1:
        readFiles(sys.argv[1:])
    else:
        word = input("Give a word to be transformed\n")
        print(wordToElements(word))
