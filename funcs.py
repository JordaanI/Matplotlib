import numpy as np

def contour_gen(n,p):
    Z = np.zeros((n,n))
    for _ in range(p):
        x = np.random.randint(n)
        y = np.random.randint(n)
        height = np.random.randint(1,n-y)
        width_start = n-x
        x_start = [np.random.randint(0,width_start) for i in range(-height,height)]
        for y_coord in range(y,height):
            for x_start_coord in x_start: 
                for x_coord in range(x_start_coord, np.random.randint(x_start_coord,n-x_start_coord)):
                        Z[x_coord][y_coord] += 1
    return Z

def pcm_gen(n):
    Z = [0]
    while len(Z) < n*n:
        num = np.random.rand() - np.random.rand()
        if abs(Z[-1]+num) <  abs(Z[-1]+0.2):
            Z.append(Z[-1]+0.1)
        else:
            Z.append(Z[-1])
    return np.reshape(Z,(n,n))