import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.0, 10.0, 10001)
y0 = 1.0 + np.cosh(x)
y = 1.0 + np.cos(x) * np.cosh(x)



plt.figure()
plt.plot(x,y)
plt.plot(x,y0,'r--')
# plt.yscale('log')
plt.grid()

plt.show()