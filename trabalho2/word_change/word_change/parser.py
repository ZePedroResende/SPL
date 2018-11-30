#!/usr/bin/python3
import sys
import shelve
import re
import unidecode
from .Word import Word
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
        if re.search(r'($|\s)'+auxdb, auxl):
            keys.append(key)
    return keys


def spotlightAux(filename, dbname, outname):
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
    s.close()
    outfile.close()


def spotlight():
    if len(sys.argv) == 3:
        dbname = sys.argv[1]
        filename = sys.argv[2]
        outname = re.sub(r'(.+\/)*(.+)', r'\1out_\2', filename)
        spotlightAux(filename, dbname, outname)
    else:
        print('número de argumentos inválido')


def replaceAux(filename, dbname, outname):
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
    s.close()
    outfile.close()


def replace():
    if len(sys.argv) == 3:
        dbname = sys.argv[1]
        filename = sys.argv[2]
        outname = re.sub(r'(.+\/)*(.+)', r'\1out_\2', filename)
        replaceAux(filename, dbname, outname)
    else:
        print('número de argumentos inválido')


def spotlight_latexAux(filename, dbname, outname):
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
    s.close()
    outfile.close()


def spotlight_latex():
    if len(sys.argv) == 3:
        dbname = sys.argv[1]
        filename = sys.argv[2]
        outname = re.sub(r'(.+\/)*(.+)', r'\1out_\2', filename)
        spotlight_latexAux(filename, dbname, outname)
    else:
        print('número de argumentos inválido')


def replace_latexAux(filename, dbname, outname):
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
    s.close()
    outfile.close()


def replace_latex():
    if len(sys.argv) == 3:
        dbname = sys.argv[1]
        filename = sys.argv[2]
        outname = re.sub(r'(.+\/)*(.+)', r'\1out_\2', filename)
        replace_latexAux(filename, dbname, outname)
    else:
        print('número de argumentos inválido')



def creator():
    if len(sys.argv) > 2:
        dbname = sys.argv[1]
        for filename in sys.argv[2:]:
            outname = re.sub(r'(.+\/)*(.+)', r'\1out_\2', filename)
            if re.search(r'\.tex$', filename):
                replace_latexAux(filename, dbname, outname)
            else:
                replaceAux(filename, dbname, outname)
    else:
        print('número de argumentos inválido')

