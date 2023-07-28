import numpy as np
import matplotlib.pyplot as plt

#Extract transition paths in descriptor space
Ntraj = 100
cut_off_1 = -1.0

for i in range(1,Ntraj+1):
    l = np.loadtxt("run%d/COLVAR"%i)
    ll = np.flip(l,0)
    #print(ll[0])
    a = []
    for j in range(len(ll)):
        if ll[j,1] > cut_off_1:
            a.append(ll[j])
        else:
            break
    a = np.array(a)

    pp = np.flip(a,0)

    np.savetxt("transitions/transition_%d"%i,pp,fmt='%0.4f')

