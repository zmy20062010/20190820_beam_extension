from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


result00 = sio.loadmat('bm_ext_base_laml_l_00e-3.mat'); 
vplist00  = result00['Vplist'];
result01 = sio.loadmat('bm_ext_base_laml_l_10e-3.mat'); 
vplist01  = result01['Vplist'];
result02 = sio.loadmat('bm_ext_base_laml_l_20e-3.mat'); 
vplist02  = result02['Vplist'];
result03 = sio.loadmat('bm_ext_base_laml_l_30e-3.mat'); 
vplist03  = result03['Vplist'];
result04 = sio.loadmat('bm_ext_base_laml_l_40e-3.mat'); 
vplist04  = result04['Vplist'];
result05 = sio.loadmat('bm_ext_base_laml_l_50e-3.mat'); 
vplist05  = result05['Vplist'];
result06 = sio.loadmat('bm_ext_base_laml_l_60e-3.mat'); 
vplist06  = result06['Vplist'];
result07 = sio.loadmat('bm_ext_base_laml_l_70e-3.mat');
vplist07  = result07['Vplist'];
result08 = sio.loadmat('bm_ext_base_laml_l_80e-3.mat'); 
vplist08  = result08['Vplist'];
result09 = sio.loadmat('bm_ext_base_laml_l_90e-3.mat'); 
vplist09  = result09['Vplist'];
result10 = sio.loadmat('bm_ext_base_laml_l_100e-3.mat'); 
vplist10  = result10['Vplist'];


fr        = result01['fr'];
Rl        = result01['Rl'];
xib       = result01['xib'];

fig2 = plt.figure(2, figsize=(12,8))
plt.plot(fr[0,:],np.abs(vplist00[5,:]),'r', label= '$\lambda_l$=0.0')
plt.plot(fr[0,:],np.abs(vplist01[5,:]),'g', label= '$\lambda_l$=0.1')
plt.plot(fr[0,:],np.abs(vplist02[5,:]),'b', label= '$\lambda_l$=0.2')
plt.plot(fr[0,:],np.abs(vplist03[5,:]),'k', label= '$\lambda_l$=0.3')
plt.plot(fr[0,:],np.abs(vplist04[5,:]),'c', label= '$\lambda_l$=0.4')
plt.plot(fr[0,:],np.abs(vplist05[5,:]),'r.--', label= '$\lambda_l$=0.5')
plt.plot(fr[0,:],np.abs(vplist06[5,:]),'g.--', label= '$\lambda_l$=0.6')
plt.plot(fr[0,:],np.abs(vplist07[5,:]),'b.--', label= '$\lambda_l$=0.7')
plt.plot(fr[0,:],np.abs(vplist08[5,:]),'k.--', label= '$\lambda_l$=0.8')
plt.plot(fr[0,:],np.abs(vplist09[5,:]),'c.--', label= '$\lambda_l$=0.9')
plt.plot(fr[0,:],np.abs(vplist10[5,:]),'y', label= '$\lambda_l$=1.0')
plt.xlabel('Base excitation frequency $fr$')
plt.ylabel('Amplitude of the output voltage $V_p$')
plt.title('Amplitude of the output voltage $V_p$ versus base excitation frequency $fr$ when $R_l = 1000\ \Omega$')
plt.legend(loc='lower right')
# plt.xscale('log')
plt.yscale('log')
plt.xlim(1,100)

# plt.savefig('fig_output_voltage_vs_frequency_laml.jpg',dpi=300)
# plt.savefig('fig_output_voltage_vs_frequency_laml.eps')
# plt.savefig('fig_output_voltage_vs_frequency_laml.pdf')



## plot 2



fig = plt.figure(1)
ax  = fig.gca(projection='3d')
# surf01 = ax.plot_surface(np.log10(fr), np.log10(Rl), np.log10(np.abs(vplist01)), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf02 = ax.plot_surface(np.log10(fr), np.log10(Rl), np.log10(np.abs(vplist02)), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf03 = ax.plot_surface(np.log10(fr), np.log10(Rl), np.log10(np.abs(vplist03)), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf04 = ax.plot_surface(np.log10(fr), np.log10(Rl), np.log10(np.abs(vplist04)), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf05 = ax.plot_surface(np.log10(fr), np.log10(Rl), np.log10(np.abs(vplist05)), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# fr = np.log10(fr)
# Rl = np.log10(Rl)


surf01 = ax.plot_surface(fr, Rl, np.abs(vplist01), cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# surf02 = ax.plot_surface(fr, Rl, np.abs(vplist02), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf03 = ax.plot_surface(fr, Rl, np.abs(vplist03), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf04 = ax.plot_surface(fr, Rl, np.abs(vplist04), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# surf05 = ax.plot_surface(fr, Rl, np.abs(vplist05), cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# ax.set_zlim(-10.0, 10.0)
# ax.xaxis.set_scale('log')
# ax.yaxis.set_scale('log')
# ax.zaxis.set_scale('log')
# ax.set_zscale('log')
# ax.set_xscale('log')
# print(dir(ax.xaxis))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# fig.colorbar(surf, shrink=0.5, aspect=5)


# xticks = [1e0,1e1,1e2,1e3]
# yticks = [1e0,1e1,1e2,1e3,1e4,1e5,1e6,1e7]
# zticks = np.logspace(-5,5,11)
# ax.set_xticks(np.log10(xticks))
# ax.set_xticklabels(xticks)
# ax.set_yticks(np.log10(yticks))
# ax.set_yticklabels(yticks)
# ax.set_zticks(np.log10(zticks))
# ax.set_zticklabels(zticks)


plt.show()



