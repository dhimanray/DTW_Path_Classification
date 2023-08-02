import numpy as np
import matplotlib.pyplot as plt
import kmedoids

distmatrix = np.loadtxt('dtw_ndim_distance_matrix.dat')

Nmedoids = 7

c = kmedoids.fasterpam(distmatrix, medoids=Nmedoids)
labels = c.labels

med_idx = c.medoids

np.savetxt('cluster_labels.txt',labels,'%d')

cluster_list = [[] for i in range(Nmedoids)]
#copy images
copy_image = True

if copy_image == True:
    import os
    os.system('rm -r %d_cluster_figs'%Nmedoids)
    os.system('rm -r %d_cluster_figs_side_view'%Nmedoids)
    os.system('mkdir %d_cluster_figs'%Nmedoids)
    os.system('mkdir %d_cluster_figs_side_view'%Nmedoids)
    for i in range(int(np.max(labels))+1):
        os.system('mkdir %d_cluster_figs/cluster_%d'%(Nmedoids,i))
        #os.system('mkdir %d_cluster_figs_side_view/cluster_%d'%(Nmedoids,i))

    for i in range(len(labels)):
        index = i+1
        os.system("cp ../run%d/unb.tga %d_cluster_figs/cluster_%d/unb%d.tga"%(index,Nmedoids,labels[i],index))
        #os.system("cp ../run_%d/side_view.tga %d_cluster_figs_side_view/cluster_%d/side_view%d.tga"%(index,Nmedoids,labels[i],index))
        cluster_list[labels[i]].append(index)

for i in range(Nmedoids):
    print(int(med_idx[i]+1),': ',cluster_list[i])
        
