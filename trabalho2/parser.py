#!/usr/bin/python3
import sys
import shelve
import re
import unidecode
from Word import Word
from random import randint

def decodeWord(word):
    return unidecode.unidecode(word)


def prettyprint(lista):
    pretty = ''
    i=0
    while (i < len(lista)-1):
        pretty = pretty + lista[i] + '; '
        i += 1
    pretty = pretty + lista[i]
    return pretty


def find(line, s):
    keys = []
    for key in s.keys():
        auxdb = decodeWord(key)
        auxl = decodeWord(line)
        if re.search(auxdb, auxl):
            keys.append(key)
    return keys


def spotlight(filename, dbname, outname):
    text = open(filename, 'r')
    s = shelve.open(dbname, flag='r')
    outfile = open(outname, 'w')

    for line in text:
        keys = find(line, s)
        if keys is []:
            outfile.write(line)
        else:
            newline = decodeWord(line)
            for key in keys:
                auxdb = decodeWord(key)
                newline = re.sub(auxdb, '['+auxdb+']', newline)
            outfile.write(newline)
            
    text.close()
    outfile.close()


def replace(filename, dbname, outname):
    text = open(filename, 'r')
    s = shelve.open(dbname, flag='r')
    outfile = open(outname, 'w')
    for line in text:
        keys = find(line, s)
        if keys is []:
            outfile.write(line)
        else:
            newline = decodeWord(line)
            for key in keys:
                auxdb = decodeWord(key)
                rand = randint(0, len(s[key].sinonimos)-1)
                syn = s[key].sinonimos[rand]
                newline = re.sub(auxdb, syn, newline)
            outfile.write(newline)

    text.close()
    outfile.close()


def spotlight_latex(filename, dbname, outname):
    text = open(filename, 'r')
    s = shelve.open(dbname, flag='r')
    outfile = open(outname, 'w')

    for line in text:
        keys = find(line, s)
        if keys is []:
            outfile.write(line)
        else:
            newline = decodeWord(line)
            for key in keys:
                auxdb = decodeWord(key)
                if s[key].semantica is None:
                    newline = re.sub(auxdb, '['+auxdb+']', newline)
                else:
                    newline = re.sub(auxdb, '['+auxdb+r'] \\footnote{'+prettyprint(s[key].semantica)+'}', newline)
            outfile.write(newline)

    text.close()
    outfile.close()


def replace_latex(filename, dbname, outname):
    text = open(filename, 'r')
    s = shelve.open(dbname, flag='r')
    outfile = open(outname, 'w')

    for line in text:
        keys = find(line, s)
        if keys is []:
            outfile.write(line)
        else:
            newline = decodeWord(line)
            for key in keys:
                auxdb = decodeWord(key)
                rand = randint(0, len(s[key].sinonimos)-1)
                syn = s[key].sinonimos[rand]
                if s[key].semantica is None:
            	    newline = re.sub(auxdb, syn, newline)
                else:
                    newline = re.sub(auxdb, syn+r' \\footnote{'+prettyprint(s[key].semantica)+'}', newline)
            outfile.write(newline)

    text.close()
    outfile.close()


def creator():
    dbname = sys.argv[1]
    i = 2
    while (i < len(sys.argv)):
        filename = sys.argv[i]
        outname = re.sub(r'(.+)', r'out_\1', filename)
        if re.search(r'\.tex$', filename):
            replace_latex(filename, dbname, outname)
        else:
            replace(filename, dbname, outname)
        i += 1


creator()
