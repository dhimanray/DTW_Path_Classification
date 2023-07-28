from dtaidistance import dtw_ndim
import kmedoids
import numpy as np
import matplotlib.pyplot as plt

def draw_score(figure, position, title, score):
    ax = figure.add_subplot(position)
    ax.bar(range(0, len(score)), score, width=0.7)
    ax.set_title(title)
    ax.set_xlim(0, len(score))
    ax.set_xticklabels([])
    ax.grid()

def mean_without_nan(x):
    sum_all = 0.0
    counter = 0.0
    for i in range(len(x)):
        if np.isfinite(x[i]) == True:
            sum_all += x[i]
            counter += 1.0
    try :
        return sum_all/counter
    except :
        pass

paths = []

files = []
for i in range(40):
    files.append('transitions/transition_%d'%(i+1))

cc = 0
for trajfile in files:
    l = np.loadtxt(trajfile)
    cc += 1
    print(cc,l.shape,trajfile)
    try :
        paths.append(l[:,1:3])
    except :
        pass

distmatrix = dtw_ndim.distance_matrix_fast(s=paths,ndim=2)

np.savetxt('dtw_ndim_distance_matrix.dat',distmatrix,fmt='%0.4f')

'''
f1 = open("silloutte_score.dat","w")
f2 = open("clusters.dat","w")

print("#K #mean_score",file=f1)
print("#K #clusters",file=f2)
for i in range(2,18):
    #model = clustering.KMedoids(
    distmatrix = dtw_ndim.distance_matrix_fast(s=paths,ndim=161)
    c = kmedoids.fasterpam(distmatrix, i)
    print("Loss is:", c.loss)
    #, {}, k=i)
    #print(xxx.shape)
    #cluster_idx, st_score = model.fit(paths)
    #print(i, mean_without_nan(st_score),file=f1)
    #print(i,cluster_idx,file=f2)

    #figure = plt.figure()
    #draw_score(figure, 111, 'K = %d'%i, st_score)
    #plt.show()

f1.close()
f2.close()

'''




