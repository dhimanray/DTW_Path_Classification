import numpy as np

l = np.loadtxt('cluster_labels.txt')

classes = np.unique(l)

for j in classes:
    print('cluster %d:'%j)
    for i in range(len(l)):
        if l[i] == j:
            print(i+1,end=', ')
    print(' ')
