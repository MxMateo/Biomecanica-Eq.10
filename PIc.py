from multiprocessing import Pool
from random import randint
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy as np


width = 10000
heigth = width
radio = width

npuntos = 0
ndentro = 0
radio2 = radio*radio
replicas = 100
n = 0
nrep = []
promediopi = []

plt.ylim(2,4)
plt.xlabel("No. Repeticiones \n [1e6 = 10 replicas]", size = 8)
plt.ylabel("π", size = 8)

if __name__ == '__main__':
        with Pool(4) as p:
            for j in range(replicas):
                for i in range(1,100000):
                    x = randint(0,width)
                    y = randint(0,width)
                    npuntos += 1
                    if x*x + y*y <= radio2:
                        ndentro += 1
                    pi = ndentro * 4 /npuntos
                    promediopi.append(pi)
                    n+=1
                    nrep.append(n)
                    # Vista por repetición
                    """
                    plt.figure(1)
                    plt.axhline(y=np.pi, c='darkseagreen',linewidth=2,alpha=0.5)
                    plt.plot(nrep,promediopi,c='mediumorchid')
                    plt.title('Aproximación π', size = 16)
                    plt.annotate('π',[0,np.pi],fontsize=25)
                    plt.draw()
                    plt.pause(0.1)
                plt.show() """
                # Vista por replica
                plt.figure(1)
                plt.axhline(y=np.pi, c='darkseagreen',linewidth=2,alpha=0.5)
                plt.plot(nrep,promediopi,c='mediumorchid')
                plt.title('Aproximación π', size = 16)
                plt.annotate('π',[0,np.pi],fontsize=25)
                plt.draw()
                plt.pause(0.1)
            plt.show()
