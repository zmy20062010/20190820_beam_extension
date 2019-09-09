from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter



result00 = sio.loadmat('bm_ext_base_lamB_Ye_0p01e9.mat'); 
vplist00  = result00['Vplist'];
result01 = sio.loadmat('bm_ext_base_lamB_Ye_0p02e9.mat'); 
vplist01  = result01['Vplist'];
result02 = sio.loadmat('bm_ext_base_lamB_Ye_0p03e9.mat'); 
vplist02  = result02['Vplist'];
result03 = sio.loadmat('bm_ext_base_lamB_Ye_0p04e9.mat'); 
vplist03  = result03['Vplist'];
result04 = sio.loadmat('bm_ext_base_lamB_Ye_0p05e9.mat'); 
vplist04  = result04['Vplist'];
result05 = sio.loadmat('bm_ext_base_lamB_Ye_0p06e9.mat'); 
vplist05  = result05['Vplist'];
result06 = sio.loadmat('bm_ext_base_lamB_Ye_0p07e9.mat'); 
vplist06  = result06['Vplist'];
result07 = sio.loadmat('bm_ext_base_lamB_Ye_0p08e9.mat');
vplist07  = result07['Vplist'];
result08 = sio.loadmat('bm_ext_base_lamB_Ye_0p09e9.mat'); 
vplist08  = result08['Vplist'];
result09 = sio.loadmat('bm_ext_base_lamB_Ye_0p1e9.mat'); 
vplist09  = result09['Vplist'];
result10 = sio.loadmat('bm_ext_base_lamB_Ye_0p2e9.mat'); 
vplist10  = result10['Vplist'];
result11 = sio.loadmat('bm_ext_base_lamB_Ye_0p3e9.mat'); 
vplist11  = result11['Vplist'];
result12 = sio.loadmat('bm_ext_base_lamB_Ye_1p3e9.mat'); 
vplist12  = result12['Vplist'];
result13 = sio.loadmat('bm_ext_base_lamB_Ye_2p3e9.mat'); 
vplist13  = result13['Vplist'];
result14 = sio.loadmat('bm_ext_base_lamB_Ye_3p3e9.mat'); 
vplist14  = result14['Vplist'];
result15 = sio.loadmat('bm_ext_base_lamB_Ye_4p3e9.mat'); 
vplist15  = result15['Vplist'];
result16 = sio.loadmat('bm_ext_base_lamB_Ye_5p3e9.mat'); 
vplist16  = result16['Vplist'];
result17 = sio.loadmat('bm_ext_base_lamB_Ye_6p3e9.mat'); 
vplist17  = result17['Vplist'];
result18 = sio.loadmat('bm_ext_base_lamB_Ye_7p3e9.mat'); 
vplist18  = result18['Vplist'];
result19 = sio.loadmat('bm_ext_base_lamB_Ye_8p3e9.mat'); 
vplist19  = result19['Vplist'];
result20 = sio.loadmat('bm_ext_base_lamB_Ye_9p3e9.mat'); 
vplist20  = result20['Vplist'];
result21 = sio.loadmat('bm_ext_base_lamB_Ye_10p3e9.mat'); 
vplist21  = result21['Vplist'];
result22 = sio.loadmat('bm_ext_base_lamB_Ye_20p3e9.mat'); 
vplist22  = result22['Vplist'];
result23 = sio.loadmat('bm_ext_base_lamB_Ye_30p3e9.mat'); 
vplist23  = result23['Vplist'];
result24 = sio.loadmat('bm_ext_base_lamB_Ye_40p3e9.mat'); 
vplist24  = result24['Vplist'];
result25 = sio.loadmat('bm_ext_base_lamB_Ye_50p3e9.mat'); 
vplist25  = result25['Vplist'];
result26 = sio.loadmat('bm_ext_base_lamB_Ye_60p3e9.mat'); 
vplist26  = result26['Vplist'];
result27 = sio.loadmat('bm_ext_base_lamB_Ye_70p3e9.mat'); 
vplist27  = result27['Vplist'];
result28 = sio.loadmat('bm_ext_base_lamB_Ye_80p3e9.mat'); 
vplist28  = result28['Vplist'];
result29 = sio.loadmat('bm_ext_base_lamB_Ye_90p3e9.mat'); 
vplist29  = result29['Vplist'];
result30 = sio.loadmat('bm_ext_base_lamB_Ye_100p3e9.mat'); 
vplist30  = result30['Vplist'];
result31 = sio.loadmat('bm_ext_base_lamB_Ye_200p3e9.mat'); 
vplist31  = result31['Vplist'];
result32 = sio.loadmat('bm_ext_base_lamB_Ye_300p3e9.mat'); 
vplist32  = result32['Vplist'];
result33 = sio.loadmat('bm_ext_base_lamB_Ye_400p3e9.mat'); 
vplist33  = result33['Vplist'];



fr        = result00['fr'];
Rl        = result00['Rl'];
xib       = result00['xib'];


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

plt.plot(fr[0,:],np.abs(vplist00[1,:]),'r', label = 'Y_e=0.01e9')
plt.plot(fr[0,:],np.abs(vplist01[1,:]),'g', label = 'Y_e=0.02e9')
plt.plot(fr[0,:],np.abs(vplist02[1,:]),'b', label = 'Y_e=0.03e9')
plt.plot(fr[0,:],np.abs(vplist03[1,:]),'k', label = 'Y_e=0.04e9')
plt.plot(fr[0,:],np.abs(vplist04[1,:]),'c', label = 'Y_e=0.05e9')
plt.plot(fr[0,:],np.abs(vplist05[1,:]),'r.-', label = 'Y_e=0.06e9')
plt.plot(fr[0,:],np.abs(vplist06[1,:]),'g.-', label = 'Y_e=0.07e9')
plt.plot(fr[0,:],np.abs(vplist07[1,:]),'b.-', label = 'Y_e=0.08e9')
plt.plot(fr[0,:],np.abs(vplist08[1,:]),'k.-', label = 'Y_e=0.09e9')
plt.plot(fr[0,:],np.abs(vplist09[1,:]),'c.-', label = 'Y_e=0.1e9')
plt.plot(fr[0,:],np.abs(vplist10[1,:]),'y', label = 'Y_e=0.2e9')
plt.plot(fr[0,:],np.abs(vplist11[1,:]),'y', label = 'Y_e=0.3e9')
plt.plot(fr[0,:],np.abs(vplist12[1,:]),'y', label = 'Y_e=1.3e9')
plt.plot(fr[0,:],np.abs(vplist13[1,:]),'y', label = 'Y_e=2.3e9')
plt.plot(fr[0,:],np.abs(vplist14[1,:]),'y', label = 'Y_e=3.3e9')

plt.xlabel('Base excitation frequency $fr$')
plt.ylabel('Amplitude of the output voltage $V_p$')
plt.title('Amplitude of the output voltage $V_p$ versus base excitation frequency $fr$ when $R_l = 10\ \Omega$')
plt.legend(loc='lower right', ncol=2)
# plt.xscale('log')
plt.yscale('log')
plt.xlim(1,100)

plt.savefig('fig_output_voltage_vs_frequency_lamB.jpg',dpi=300)
plt.savefig('fig_output_voltage_vs_frequency_lamB.eps')
plt.savefig('fig_output_voltage_vs_frequency_lamB.pdf')

plt.show()






