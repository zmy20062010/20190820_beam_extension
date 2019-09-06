import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

enablelog = True

snr=15
fig = plt.figure(figsize=(12,12))
ax = fig.gca(projection='3d')

realsnr = 10**(snr/10)
B,T = np.mgrid[100e3:10e6:100e3, 1:60:1]
C = .55 / (np.sqrt(2) * B * np.sqrt(B * T * realsnr) )
if enablelog: C = np.log10(C)
surf = ax.plot_surface(
    B/1e6, T, C, cmap='rainbow',cstride=1,
    rstride=1,linewidth=0,antialiased=False)
ax.set_xlabel("Bandwidth MHz")
ax.set_ylabel("Integration Time")
ax.set_zlabel("Cramer-Rao Lower Bound")
if enablelog:zticks = [1e-13,1e-12,1e-11,1e-10,1e-9]
if enablelog:ax.set_zticks(np.log10(zticks))
if enablelog:ax.set_zticklabels(zticks)
plt.show()


print(np.logspace(-10,10,21))