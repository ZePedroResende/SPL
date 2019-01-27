#!/usr/bin/python3

def analise(filename1, filename2):
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
    
    for i in range(0, total):
        if text1[i] == ' ' and text2[j] == ' ':
            true_p += 1
            j += 1
        elif text1[i] != ' ' and text2[j] != ' ':
            true_n += 1
            j += 1
        elif text1[i] == ' ' and text2[j] != ' ':
            false_n += 1
        elif text1[i] != ' ' and text2[j] == ' ':
            false_p += 1
            j += 2

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

analise('teste0.txt', 'teste1.txt')