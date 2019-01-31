#!/usr/bin/python3
import sys

def analiseAux(filename1, filename2):
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')
    text1 = file1.read()
    text2 = file2.read()
    
    true_p = 0
    true_n = 0
    false_p = 0
    false_n = 0
    total = len(text1)
    j=0
    i=0
    
    while i < total and j < len(text2):
        if text1[i] == ' ' and text2[j] == ' ':
            true_p += 1
            i += 1
            j += 1
        elif text1[i] != ' ' and text2[j] != ' ':
            true_n += 1
            i += 1
            j += 1
        elif text1[i] == ' ' and text2[j] != ' ':
            false_n += 1
            i += 1
        elif text1[i] != ' ' and text2[j] == ' ':
            false_p += 1
            j += 1

    accuracy = (true_p + true_n) / total
    precision = true_p / (true_p + false_p)
    recall = true_p / (true_p + false_n)

    file1.close()
    file2.close()

    print('True Positives: '+ str(true_p))
    print('True Negatives: '+ str(true_n))
    print('False Positives: '+ str(false_p))
    print('False Negatives: '+ str(false_n))
    print('------------------')
    print('Accuracy: '+ str(accuracy))
    print('Precision: '+ str(precision))
    print('Recall: '+ str(recall))

def analise():
    if len(sys.argv) == 3:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
        analiseAux(filename1, filename2)
    else:
        print('número de argumentos inválido')
