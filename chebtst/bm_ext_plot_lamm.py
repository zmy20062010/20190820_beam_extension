from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.ticker as mtick

result01  = sio.loadmat('bm_ext_base_lamm_rhoe_1p38e1.mat'); 
vplist01  = result01['Vplist'];
result02  = sio.loadmat('bm_ext_base_lamm_rhoe_1p38e2.mat'); 
vplist02  = result02['Vplist'];
result03  = sio.loadmat('bm_ext_base_lamm_rhoe_1p38e3.mat'); 
vplist03  = result03['Vplist'];
result04  = sio.loadmat('bm_ext_base_lamm_rhoe_1p38e4.mat'); 
vplist04  = result04['Vplist'];
result05  = sio.loadmat('bm_ext_base_lamm_rhoe_1p38e5.mat'); 
vplist05  = result05['Vplist'];

fr        = result01['fr'];
Rl        = result01['Rl'];
xib       = result01['xib'];


# Create plot

# fig = plt.figure(1)
# ax  = fig.gca(projection='3d')
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
# ax.set_zlim(-10.0, 10.0)
# # ax.xaxis.set_scale('log')
# # ax.yaxis.set_scale('log')
# #ax.zaxis.set_scale('log')
# # ax.set_zscale('log')
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# # Add a color bar which maps values to colors.
# # fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()


fig2 = plt.figure(2, figsize=(12,8))
plt.plot(fr[0,:],np.abs(vplist01[3,:]),'r', label = r'$\rho_e$=1.38e1')
plt.plot(fr[0,:],np.abs(vplist02[3,:]),'m--', label = r'$\rho_e$=1.38e2')
plt.plot(fr[0,:],np.abs(vplist03[3,:]),'b-*', label = r'$\rho_e$=1.38e3')
plt.plot(fr[0,:],np.abs(vplist04[3,:]),'k-.', label = r'$\rho_e$=1.38e4')
plt.plot(fr[0,:],np.abs(vplist05[3,:]),'c', label = r'$\rho_e$=1.38e5')
plt.xlabel('Base excitation frequency $fr$')
plt.ylabel('Amplitude of the output voltage $V_p$')
plt.title('Amplitude of the output voltage $V_p$ versus base excitation frequency $fr$ when $R_l = 1000\ \Omega$')
plt.legend(loc='lower right')
# plt.xscale('log')
plt.yscale('log')
plt.xlim(1,100)

plt.savefig('fig_output_voltage_vs_frequency_lamm.jpg',dpi=300)
plt.savefig('fig_output_voltage_vs_frequency_lamm.eps')
plt.savefig('fig_output_voltage_vs_frequency_lamm.pdf')

plt.show()






