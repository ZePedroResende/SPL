#!usr/bin/python3
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

