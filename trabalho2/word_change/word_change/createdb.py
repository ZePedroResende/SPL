#!usr/bin/python3
import sys
import shelve
import re
from Word import Word

def printdb(dbname):
    s = shelve.open(dbname, flag='r')
    for key in s.keys():
        print('---------------------------------')
        print('TERM: '+key)
        value = s[key]
        print('SYN:'+str(value.sinonimos))
        if value.semantica is not None:
            print('SEM: '+value.semantica)


def generator(filename, dbname):
    dic = open(filename, 'r')
    s = shelve.open(dbname)
    in_syn = False
    syn_found = False
    sem_found = False
    sem = None
    syn = []

    for line in dic:
        if re.match(r'TERM=.+',line):
            key = re.sub(r'TERM=\'*([^\']+)\'*\n', r'\1', line)
        if re.match(r'\s+\'sem\' \=\>', line):
            sem_found = True
            sem = re.sub(r'\s+\'sem\' \=\> \'*([^\']+)\'*(,)?\n', r'\1', line)
        if in_syn and re.match(r'\s+\]', line):
            in_syn = False
            syn_found = True
        if in_syn:
            aux = re.sub(r'\s+\'*([^\']+)\'*(,)?\n', r'\1', line)
            syn.append(aux)
        if re.match(r'\s+\'syn\' \=\> \[', line):
            in_syn = True
        if re.match(r'\}',line):
            if syn_found:
                s[key] = Word(syn,sem)
                syn_found = False
                syn.clear()
            sem_found = False
            sem = None


def create():
    for filename in sys.argv:
        if filename != 'createdb.py':
            dbname = re.sub(r'(.+)(\..+)', r'\1.db', filename)
            generator(filename, dbname)
            printdb(dbname)

create()
