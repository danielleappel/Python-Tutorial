import matplotlib as mpl
import matplotlib.pyplot as plt 
import numpy as np
import random

def fern_call(n):
    """Generates a fern fractal iteritavely.

    Keyword arguments:
    n -- the number of iterations
    """
    v = ([0,0]) # Start at the origin.
    plt.plot(v[0],v[1],'go', alpha = 0.3)
    plt.title("Fern fractal iterative, n = %d" %n)
    
    i = 0
    while (i < n):
        switch = random.randint(1,4)
        if switch == 1:
            v =  np.dot(([0.85,  0.04],
                        [-0.04, 0.85]), v) + ([0,1.6])
        elif switch == 2:
            v =  np.dot(([0.20,  0.26],
                        [0.23,  0.22]), v) + ([0,1.6])
        elif switch == 3:
            v =  np.dot(([-0.15,  0.28],
                        [0.26, 0.24]), v) + ([0,0.44])
        else :
            v =  np.dot(([0,  0],
                        [0,  0.16]), v)

        plt.plot(v[0],v[1],'go', alpha = 0.3)
        i += 1
        
    plt.show()

def main():
    n = 10000
    fern_call(n)

if __name__ == "__main__":
    main()
