from dtaidistance import dtw_ndim
import kmedoids
import numpy as np
import matplotlib.pyplot as plt


paths = []

files = []
for i in range(100):
    files.append('../unbinding_transitions_conts_6_12/unbinding_transition_%d'%(i+1))

cc = 0
for trajfile in files:
    l = np.loadtxt(trajfile)
    cc += 1
    print(cc,l.shape,trajfile)
    try :
        paths.append(l[::1,15:])
    except :
        pass

distmatrix = dtw_ndim.distance_matrix_fast(s=paths,ndim=161)

np.savetxt('dtw_ndim_distance_matrix.dat',distmatrix,fmt='%0.4f')



