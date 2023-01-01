import numpy as np
import matplotlib.pyplot as plt
import math

plt.axes(projection = 'polar')

a=4

rads = np.arange(0, (2 * np.pi),0.01)

for rad in rads:
    sq=(math.cos(2*rad))
    if sq<0:
        continue
    else:
        r=a*math.sqrt(sq)
        plt.polar(rad,r,'g.')

plt.show()
