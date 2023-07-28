import numpy as np
import os

l = np.loadtxt('cluster_labels.txt')

for i in np.unique(l):
    os.system('mkdir cluster_%d'%i)
    os.system('touch cluster_%d/transitions.dat'%i)

for j in range(len(l)):
    for i in np.unique(l):
        if l[j] == i :
            os.system('tail -n 1 ../../run_%d/time >> cluster_%d/transitions.dat'%(j+1,i))

