import numpy as np
import matplotlib.pyplot as plt

#Generate transition paths for unbinding
Ntraj = 20
cut_off_x = -0.5
cut_off_y = 1.0

counter = 0
for i in range(1,Ntraj+1):
    l = np.loadtxt("cv_x/run%d/COLVAR"%i)

    counter += 1
    np.savetxt("transitions_colvar/transition_%d"%counter,l,fmt='%0.4f')

for i in range(1,Ntraj+1):
    l = np.loadtxt("cv_y/run%d/COLVAR"%i)

    counter += 1
    np.savetxt("transitions_colvar/transition_%d"%counter,l,fmt='%0.4f')

