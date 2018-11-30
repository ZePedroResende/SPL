#!usr/bin/python3
<<<<<<< HEAD
import shelve
import re

s = shelve.open('calao.db')
dic = open('calao_exemplo.txt', 'r')

in_syn = False
syn_found = False
sem_found = False
sem = []
syn = []
value = []

for line in dic:
    if re.match(r'TERM=.+',line):
        key = re.sub(r'TERM=\'\'(.+)\'\'\n', r'\1', line)
    if re.match(r'\s+\'sem\' \=\>', line):
        sem_found = True
        aux = re.sub(r'\s+\'sem\' \=\> \'(.+)\'(,)?\n', r'\1', line)
        sem.append(aux)
    if in_syn and re.match(r'\s+\]', line):
        in_syn = False
        syn_found = True
    if in_syn:
        aux = re.sub(r'\s+\'(.+)\'(,)?\n', r'\1', line)
        syn.append(aux)
    if re.match(r'\s+\'syn\' \=\> \[', line):
        in_syn = True
    if syn_found and re.match(r'\}',line):
        value.append(syn)
        if sem_found:
            value.append(sem)
        s[key] = value
        syn_found = False
        sem_found = False
        syn = []
        value = []
    if re.match(r'\}', line):
        sem = []


for key in s.keys():
    print('---------------------------------')
    print(key)
    for item in s[key]:
        print(item)

dic.close()

=======
import sys
import shelve
import re
from Word import Word


def prettyprint(lista):
    pretty = ''
    i=0
    while (i < len(lista)-1):
        pretty = pretty + lista[i] + '; '
        i += 1
    pretty = pretty + lista[i]
    return pretty


def printdb(dbname):
    s = shelve.open(dbname, flag='r')
    for key in s.keys():
        print('---------------------------------')
        print('TERM: '+key)
        value = s[key]
        print('SYN:'+prettyprint(value.sinonimos))
        if value.semantica is not []:
            print('SEM: '+prettyprint(value.semantica))


def generator(filename, dbname):
    dic = open(filename, 'r')
    s = shelve.open(dbname)
    in_syn = False
    in_sem = False
    syn_found = False
    sem_found = False
    sem = []
    syn = []

    for line in dic:
        if re.match(r'TERM=.+',line):
            key = re.sub(r'TERM=\'*([^\']+)\'*\n', r'\1', line)
        if in_sem and re.match(r'\s+\]', line):
            in_sem = False
            sem_found = True
        if in_sem:
            aux = re.sub(r'\s+\'*([^\']+)\'*(,)?\n', r'\1', line)
            sem.append(aux)
        if re.match(r'\s+\'sem\' \=\> \[', line):
            in_sem = True 
        if (not in_sem) and re.match(r'\s+\'sem\' \=\>', line):
            sem_found = True
            aux = re.sub(r'\s+\'sem\' \=\> \'*([^\']+)\'*(,)?\n', r'\1', line)
            sem.append(aux)
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
                if sem_found:
                    s[key] = Word(syn,sem)
                else:
                    s[key] = Word(syn)
                syn_found = False
                syn.clear()
            sem_found = False
            sem.clear()


def create():
    for filename in sys.argv:
        if filename != 'createdb.py':
            dbname = re.sub(r'(.+)(\..+)', r'\1.db', filename)
            generator(filename, dbname)
            printdb(dbname)

create()
>>>>>>> 998b0867790082bc13ece55b4a887340f8664779
