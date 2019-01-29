#!usr/bin/python3.6
import regex as re
import sys
import pickle
from collections import defaultdict, Counter

N=7

def buildAux(filename, outname):
    input_t = open(filename, 'rb')
    output_t = open(outname, 'wb')
    ocorrencias = defaultdict(Counter)

    for line in input_t.readlines():
        line = re.sub(r'\p{punct}', r' ', line)
        line = re.sub(r'\s+', r' ', line)
        seq = [tuple(line[i:i+N]) for i in range(0, len(line)-N+1)]
        for t in seq:
            ocorrencias[''.join(t[0:-1])[-1]] += 1

    pickle.dump(ocorrencias, output_t, protocol = -1)
    input_t.close()
    output_t.close()


def build():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        outname = re.sub(r'(.+\/)*(.+)', r'\1n-grama_\2', filename)
        buildAux(filename, outname)
    else:
        print('número de argumentos inválido')


def add_spaces(filename, dictname, outname):
    f = open(dictname, 'rb')
    ocorrencias = pickle.load(f)
    f.close()
    input_t = open(filename, 'rb')
    output_t = open(outname, 'wb')
    sentence = []

    for line in input_t.readlines():
        line = re.sub(r'([\.,;!?\)\]])', r'\1 ', line)
        line = re.sub(r'([\(\[])', r' \1', line)
        for i in range(0, len(line)-N+1):
            if re.match(r'\p{punct}', line[i+N-1]):
                sentence.append(line[i:i+N])
            else:
                state = line[i:i+N]
                new_state = try_fix(state, ocorrencias)
                sentence.append(new_state)
        sentence = ''.join(sentence)
        output_t.write(sentence)
        sentence = []


def try_fix(state, ocorrencias):
    
