from numpy import linalg
import csv

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
# ################################Letra a##############################################
total = 0
x1sum = 0
x2sum = 0
x3sum = 0
with open('dados2.csv') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for row in content:
        x1sum += float(row[0])
        x2sum += float(row[1])
        x3sum += float(row[2])
        total += 1

x1mean = x1sum/total
x2mean = x2sum/total
x3mean = x3sum/total
print('''Média Amostral
    x1|  {0:.2f},
    x2|  {1:.2f},
    x3|  {2:.2f}'''.format(x1mean, x2mean, x3mean))

total = 0
# fig1 = plt.figure()
# ax = fig1.add_subplot(111, projection='3d')
with open('dados2-media-nula.csv', 'w') as output:
    with open('dados2.csv') as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        for row in content:
            output.write('{},{},{}\r\n'.format(
                float(row[0]) - x1mean,
                float(row[1]) - x2mean,
                float(row[2]) - x3mean))
            # output.write('{0:.2f},{1:.2f},{2:.2f}\r\n'.format(
            #     float(row[0]) - x1mean,
            #     float(row[1]) - x2mean,
            #     float(row[2]) - x3mean))
            total += 1
            # ax.scatter(float(row[0]), float(row[1]), float(row[2]), c='b')
# fig1.show()
# plt.show()
#######################################################################################
# ################################Letra b##############################################
fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')
matriz_cov = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
with open('dados2-media-nula.csv') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for row in content:
        x = float(row[0])
        y = float(row[1])
        z = float(row[2])
        ax.scatter(x, y, z, c='b')
        matriz_cov[0][0] += x*x
        matriz_cov[0][1] += x*y
        matriz_cov[0][2] += x*z
        matriz_cov[1][0] += y*x
        matriz_cov[1][1] += y*y
        matriz_cov[1][2] += y*z
        matriz_cov[2][0] += z*x
        matriz_cov[2][1] += z*y
        matriz_cov[2][2] += z*z
    matriz_cov[0][0] = matriz_cov[0][0]/(total-1)
    matriz_cov[0][1] = matriz_cov[0][1]/(total-1)
    matriz_cov[0][2] = matriz_cov[0][2]/(total-1)
    matriz_cov[1][0] = matriz_cov[1][0]/(total-1)
    matriz_cov[1][1] = matriz_cov[1][1]/(total-1)
    matriz_cov[1][2] = matriz_cov[1][2]/(total-1)
    matriz_cov[2][0] = matriz_cov[2][0]/(total-1)
    matriz_cov[2][1] = matriz_cov[2][1]/(total-1)
    matriz_cov[2][2] = matriz_cov[2][2]/(total-1)
print(
    """             X \t\t Y \t\t Z
        X |{0:.2f},\t{1:.2f},\t\t{2:.2f}
        
        Y |{3:.2f},\t{4:.2f},\t\t{5:.2f}
        
        Z |{6:.2f},\t{7:.2f},\t\t{8:.2f}
    """.format(
        matriz_cov[0][0],
        matriz_cov[0][1],
        matriz_cov[0][2],
        matriz_cov[1][0],
        matriz_cov[1][1],
        matriz_cov[1][2],
        matriz_cov[2][0],
        matriz_cov[2][1],
        matriz_cov[2][2])
)
autovalores, autovetores = linalg.eig(matriz_cov)
print(autovalores)
print(autovetores)
# xx = np.arange(-5, 5, 0.1)
# yy = np.arange(-15, 15, 0.1)
# X, Y = np.meshgrid(xx, yy)
# max_index = np.argmax(autovalores)
# print(autovetores[max_index][0])
# print(autovetores[max_index][1])
# print(autovetores[max_index][2])
# Z = abs(autovetores[max_index][0])*X/abs(autovetores[max_index][2]) + abs(autovetores[max_index][1])*Y/abs(autovetores[max_index][2])
# ax.plot_surface(X, Y, Z)
# ax.view_init(8, -2)

point = np.array([0,0,0])
min_index = np.argmin(autovalores)
normal = [autovetores[0][min_index],autovetores[1][min_index],autovetores[2][min_index]]
print(min_index)
print(normal)

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d = -point.dot(normal)
print(d)

# create x,y
xx, yy = np.meshgrid(range(10), range(10))
xx = np.arange(-5, 5, 0.1)
yy = np.arange(-15, 15, 0.1)
X, Y = np.meshgrid(xx, yy)

# calculate corresponding z
z = autovalores[1]*(-normal[0] * X - normal[1] * Y - d) * 1. /normal[2]

# plot the surface
ax.plot_surface(X, Y, z)
ax.quiver([0,0,0], [0,0,0], [0,0,0], autovetores[0]*10, autovetores[1]*10, autovetores[2]*10, color='green', arrow_length_ratio=0.1)
ax.view_init(8, -2)

plt.show()
