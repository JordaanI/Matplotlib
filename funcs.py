import numpy as np

def contour_gen(n,p):
    Z = np.zeros((n,n))
    for _ in range(p):
        increment = np.random.randint(4)
        x = np.random.randint(n)
        y = np.random.randint(n)
        height = np.random.randint(1,n-y)
        width= n-x
        x_start = [np.random.randint(-0.2*n,0.2*n) for i in range(height)]
        for ind, y_coords in enumerate(range(y,y+height)):
            start = np.random.randint(x_start[ind]-width, x_start[ind]+width)
            end = np.random.randint(start,n)
            for x_coords in range(start, end):
                Z[y_coords][x_coords] += increment
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