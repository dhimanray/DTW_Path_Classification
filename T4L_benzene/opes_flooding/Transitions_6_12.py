import numpy as np
import matplotlib.pyplot as plt

#Generate transition paths for unbinding
Ntraj = 137
cut_off_rho = 0.3
cut_off_cont = 3.0
max_rho = 3.0 #take care of the jump accross box

include = False #when include = True, trajectory data is used for analysis

for i in range(1,Ntraj+1):
    l = np.loadtxt("run_%d/CA_bnz_contacts_6_12.dat"%i)
    
    #First remove the portion in the bound state
    ll = np.flip(l,0)
    #print(ll[0])
    a = []
    for j in range(len(ll)):
        if ll[j,11] > cut_off_rho:
            if ll[j,11] < max_rho:
                a.append(ll[j])
        else:
            break
    a = np.array(a)

    pp = np.flip(a,0)
    print(np.max(pp[:,11]))

    #Now remove the portion in the unbound state
    path = []
    for j in range(len(pp)):
        if pp[j,14] > cut_off_cont:
            path.append(pp[j])
        else:
            break
    path = np.array(path)
    np.savetxt("unbinding_transitions_conts_6_12/unbinding_transition_%d"%i,path,fmt='%0.4f')

'''
    a = []
    for j in range(len(l)):
        #start include when rho > cutoff
        if l[j,11] > cut_off_rho:
            include = True
        if l[j,14] < cut_off_cont:
            include = False
            break

        if include:
            a.append(l[j])
'''
    #ll = np.flip(l,0)
    #print(ll[0])
    #a = []
    #for j in range(len(ll)):
    #    if ll[j,11] > cut_off_1:
    #        if ll[j,11] < max_rho:
    #            a.append(ll[j])
    #    else:
    #        break
    #a = np.array(a)

    #pp = np.flip(a,0)

    #np.savetxt("unbinding_transitions_conts_6_12/unbinding_transition_%d"%i,path,fmt='%0.4f')

