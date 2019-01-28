#!/usr/bin/python3
import re
import sys

def remove_espacosAux(filename, outname):
    text = open(filename, 'r')
    outfile = open(outname, 'w')

    for line in text:
        newline = re.sub(r' +', r'', line)
        outfile.write(newline)
            
    text.close()
    outfile.close()

def remove_espacos():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        outname = re.sub(r'(.+\/)*(.+)', r'\1spaceless_\2', filename)
        remove_espacosAux(filename, outname)
    else:
        print('número de argumentos inválido')