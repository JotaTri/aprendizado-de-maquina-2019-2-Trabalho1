from math import log, pi
import csv
# import numpy as np

PCm1 = 0.3
PCp1 = 0.7

x1 = -0.19172
x2 = 0.42997
success = 0
total = 0
with open('dados1.csv') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for row in content:
        pXCp1 = -log(8*pi) - ((float(row[0])+1)**2 + (float(row[1])+3)**2)/8
        pXCm1 = -log(2*pi) - ((float(row[0])-1.2)**2 + (float(row[1])-1.2)**2)/2
        result = pXCm1 - pXCp1 + log(PCm1) - log(PCp1)
        print('{} - {} + {} - {} = {}......{}'.format(pXCm1, pXCp1, log(PCm1), log(PCp1), result, row[2]))
        # print(result)
        if result > 0 and row[2] == '-1':
            success += 1
            print(success)
        elif result < 0 and row[2] == '1':
            success += 1
        total += 1

print(float(success))
print(float(total))
print(float(success/total))
