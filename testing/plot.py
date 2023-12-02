import matplotlib.pyplot as plt
import numpy as np


prices = [7,1,5,3,6,4]

def plot_stocks(arr:list):

    xpoints = np.array([i for i in range(len(arr))])
    ypoints = np.array(arr)

    plt.plot(xpoints, ypoints)
    plt.show()

plot_stocks(prices)