from math import log, pi, exp
import csv

import matplotlib.pyplot as plt

PCm1 = 0.3
PCp1 = 0.7

success = 0
total = 0
x1max = -100
x1min = 100
x2max = -100
x2min = 100
##############################################################################
plt.figure('figura 1')
with open('dados1.csv') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for row in content:
        x1 = float(row[0])
        x2 = float(row[1])
        if x1 < x1min:
            x1min = x1
        if x1 > x1max:
            x1max = x1

        if x2 < x2min:
            x2min = x2
        if x2 > x2max:
            x2max = x2

        pXCp1 = -log(8*pi) - ((x1+1)**2 + (x2+3)**2)/8
        pXCm1 = -log(2*pi) - ((x1-1.2)**2 + (x2-1.2)**2)/2
        result = pXCm1 - pXCp1 + log(PCm1) - log(PCp1)
        if result > 0 and row[2] == '-1':
            success += 1
        elif result < 0 and row[2] == '1':
            success += 1
        total += 1
        if row[2] == '-1':
            plt.plot(x1, x2, 'bo')
        else:
            plt.plot(x1, x2, 'r+')


print('x1min = {}; x1max = {}'.format(x1min, x1max))
print('x2min = {}; x2max = {}'.format(x2min, x2max))
plt.show()

##############################################################################
xmin = min([x1min, x2min])
xmax = max([x1max, x2max])
# xmin = -11.234
# xmax = 7.4222
plt.figure('figura 2')
step = abs(xmax - xmin)/1000
x1plot = plt.subplot(211)
x2plot = plt.subplot(212)
while xmin < xmax:
    x1 = xmin
    x2 = xmin
    px1Cp1 = 1/(8*pi)*exp(-((x1+1)**2)/8)*(PCp1)
    px2Cp1 = 1/(8*pi)*exp(-((x2+3)**2)/8)*(PCp1)
    px1Cm1 = 1/(2*pi)*exp(-((x1-1.2)**2)/2)*(PCm1)
    px2Cm1 = 1/(2*pi)*exp(-((x2-1.2)**2)/2)*(PCm1)

    x1plot.plot(xmin, px1Cp1, 'ro')
    x1plot.plot(xmin, px1Cm1, 'bo')

    x2plot.plot(xmin, px2Cp1, 'ro')
    x2plot.plot(xmin, px2Cm1, 'bo')
    xmin += step
plt.show()

# print(float(success))
# print(float(total))
# print(float(success/total))
