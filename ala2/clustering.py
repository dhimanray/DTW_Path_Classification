import numpy as np
import matplotlib.pyplot as plt
import kmedoids

distmatrix = np.loadtxt('dtw_ndim_distance_matrix.dat')

scores = []
f1 = open('silhouette.dat','w')
for i in range(2,50):
    c = kmedoids.fasterpam(distmatrix, medoids=i)
    scores.append(kmedoids.silhouette(distmatrix,c.labels)[0])
    print('Number of Clusters: ',i,'  Silhouette Score: ',kmedoids.silhouette(distmatrix,c.labels)[0])
    print(i,kmedoids.silhouette(distmatrix,c.labels)[0]/float(i),file=f1)
f1.close()


