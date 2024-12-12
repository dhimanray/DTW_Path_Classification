import numpy as np
from dtaidistance import dtw

pathC1 = [ 5, 8, 17, 20, 32, 35, 39, 42, 51, 56, 62, 80, 104, 107, 109, 120, 125, 136 ] 
pathC3 = [ 1, 3, 6, 21, 31, 49, 64, 71, 77, 83, 90, 99, 118, 124, 127, 128 ] 

cont_dtw = np.zeros(161)
for cont in range(161):
    for i in pathC1:
        for j in pathC3:
            p1 = np.loadtxt('../../unbinding_transitions_conts_6_12/unbinding_transition_%d'%i,usecols=(15+cont))
            p2 = np.loadtxt('../../unbinding_transitions_conts_6_12/unbinding_transition_%d'%j,usecols=(15+cont))
            #print(p1.shape,p2.shape)
            cont_dtw[cont] += dtw.distance_fast(p1[::10],p2[::10])
    print(cont_dtw[cont])

