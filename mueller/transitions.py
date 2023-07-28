import numpy as np
import matplotlib.pyplot as plt

#Generate transition paths for unbinding
Ntraj = 20
cut_off_x = -0.5
cut_off_y = 1.0

counter = 0
for i in range(1,Ntraj+1):
    l = np.loadtxt("cv_x/run%d/COLVAR"%i)
    ll = np.flip(l,0)
    #print(ll[0])
    a = []
    for j in range(len(ll)):
        if ll[j,1] > cut_off_x or ll[j,2] < cut_off_y :
            a.append(ll[j])
        else:
            break
    a = np.array(a)

    pp = np.flip(a,0)

    counter += 1
    np.savetxt("transitions/transition_%d"%counter,pp,fmt='%0.4f')

for i in range(1,Ntraj+1):
    l = np.loadtxt("cv_y/run%d/COLVAR"%i)
    ll = np.flip(l,0)
    #print(ll[0])
    a = []
    for j in range(len(ll)):
        if ll[j,1] > cut_off_x or ll[j,2] < cut_off_y :
            a.append(ll[j])
        else:
            break
    a = np.array(a)

    pp = np.flip(a,0)

    counter += 1
    np.savetxt("transitions/transition_%d"%counter,pp,fmt='%0.4f')

