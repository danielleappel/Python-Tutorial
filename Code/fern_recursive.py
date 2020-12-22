import matplotlib as mpl
import matplotlib.pyplot as plt 
import numpy as np
import random

def fern_generator(n):
    """Generates a fern fractal recursively.

    Keyword arguments:
    n -- the number of recursive calls
    """
    v = ([0,0])           
    plt.plot(v[0],v[1],'go', alpha = 0.5) # Plot first point at origin
    plt.title("Fern fractal recursive, n = %d" %n)

    fern(v, n)
    plt.show()
    
def fern(v, n):
    """Tries to raise x to the fourth power.

    Keyword arguments:
    x -- the number to raise to the fourth
    """
    if n > 0:
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
        elif switch == 4:
            v =  np.dot(([0,  0],
                        [0,  0.16]), v)

        plt.plot(v[0],v[1],'go', alpha = 0.5)
        fern(v, n-1)

def main():
    n = 900
    fern_generator(n)

if __name__ == "__main__":
    main()
