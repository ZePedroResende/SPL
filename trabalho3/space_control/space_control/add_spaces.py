#!usr/bin/python3.6
import regex as re
import sys
import pickle
from collections import defaultdict, Counter

N=9

def buildAux(filename, outname):
    input_t = open(filename, 'r')
    ocorrencias = defaultdict(Counter)

    for line in input_t.readlines():
        line = re.sub(r'\p{punct}', r' ', line)
        line = re.sub(r'\s+', r' ', line)
        seq = [tuple(line[i:i+N]) for i in range(0,len(line) -N + 1)]
        for t in seq:
            ocorrencias[''.join(t[0:-1])][t[-1]] += 1
    
    input_t.close()
    output_t = open(outname, 'wb')
    pickle.dump(ocorrencias, output_t, protocol = -1)
    output_t.close()


def build():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        outname = 'dict.pkl'
        buildAux(filename, outname)
    else:
        print('número de argumentos inválido')


def try_fix(state, char):
    if state in ocorrencias:
        if char in ocorrencias[state]:
            return char
        else:
            l = list(state)
            l.pop(0)
            l.append(' ')
            state = "".join(l)
            if char in ocorrencias[state]:
                return ' ' + char
            else:
                return char
    else:
        return char


def add_spacesAux(filename, dictname, outname):
    f = open(dictname, 'rb')
    global ocorrencias
    ocorrencias = pickle.load(f)
    f.close()
    input_t = open(filename, 'r')
    output_t = open(outname, 'w')

    for line in input_t.readlines():
        line = re.sub(r'([\.,;!?\)\]\}])', r'\1 ', line)
        line = re.sub(r'([\(\[\{])', r' \1', line)
        
        for i in range(0, len(line)-N+1):
            char = line[i+N-1]
            if not re.match(r'\p{punct}', char) and not re.match(r'\p{punct}', line[i+N-2]):
                state = line[i:i+N-1]
                l = list(line)
                l[i+N-1] = try_fix(state, char)
                line = "".join(l)

        output_t.write(line)
    
    output_t.close()
    input_t.close()


def add_spaces():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        dictname = sys.argv[2]
        outname = re.sub(r'(.+\/)*(.+)', r'\1out_\2', filename)
        add_spacesAux(filename, dictname, outname)
    else:
        print('número de argumentos inválido')
