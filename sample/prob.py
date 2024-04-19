
from random import randrange

top = 50
arr = [0]*top

for i in range(1000000):
    arr[randrange(0, top)] +=1

print(arr)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([i for i in range(0, top)])
ypoints = np.array(arr)

plt.plot(xpoints, ypoints)
plt.set_ylim(ymin=0)
plt.show()