import numpy as np

def pcm_gen(n):
    Z = [0]
    while len(Z) < n*n:
        num = np.random.rand() - np.random.rand()
        if abs(Z[-1]+num) <  abs(Z[-1]+0.2):
            Z.append(Z[-1]+0.1)
        else:
            Z.append(Z[-1])
    return np.reshape(Z,(n,n))