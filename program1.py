import math
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,3,100)
y=np.power(x,(3/2))
plt.title('cartesian curve for the equation x²=y³')
plt.plot(x,y)
plt.plot(x,-y)
plt.grid()
plt.show()
