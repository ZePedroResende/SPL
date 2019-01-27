#!/usr/bin/python3
import re

def remove_espacos(filename):
    text = open(filename, 'r')
    outname = re.sub(r'(.+\/)*(.+)', r'\1spaceless_\2', filename)
    outfile = open(outname, 'w')

    for line in text:
        newline = re.sub(r' +', r'', line)
        outfile.write(newline)
            
    text.close()
    outfile.close()