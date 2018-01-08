import numpy as np

from scipy.spatial.distance import cdist as euclidean_distances

def no_z_dist(p1,p2):
    p1[2] = p2[2] = 0

    return np.sum((p1 - p2)**2)

def no_z_squared(p1):
    p1[:,2] = 0
    return np.sum(p1**2,axis=1)

def no_z_xy(p1,p2):
    p1[:,2] = 0 
    p2[:,2] = 0
    return np.dot(p1, p2.T)

def edm_two_loop(matrix1, matrix2=None): #Euclidean distance matrix
    Nconf = matrix1.shape[0]
    Nlipids = matrix1.shape[1]

    if not np.any(matrix2):
        matrix2 = matrix1

    Nchol = matrix2.shape[1]

    dists = np.zeros([Nconf,Nlipids,Nchol])

    for t in range(Nconf):
        for i in range(Nlipids):
            for j in range(Nchol):
                squared_dist = no_z_dist(matrix1[t][i],matrix2[t][j])
                dists[t,i,j] = np.sqrt(squared_dist)
    
    return dists

def edm(matrix1, matrix2=None): #Euclidean distance matrix
    Nconf = matrix1.shape[0]
    Nlipids = matrix1.shape[1]

    if not np.any(matrix2):
        matrix2 = matrix1

    Nchol = matrix2.shape[1]

    dists = np.zeros([Nconf,Nlipids,Nchol])

    matrix1[:,:,2] = 0
    matrix2[:,:,2] = 0

    for t in range(Nconf):

        dists[t] = euclidean_distances(matrix1[t],matrix2[t],'euclidean')

        """
        x_squared = no_z_squared(matrix1[t])
        y_squared = no_z_squared(matrix2[t])
        xy = no_z_xy(matrix1[t],matrix2[t])
        dists[t] = np.sqrt(-2*xy + y_squared + x_squared)
        """
    
    return dists
    