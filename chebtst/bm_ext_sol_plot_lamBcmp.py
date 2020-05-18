import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

lp = 100e-3
le = 100e-3


result01 = sio.loadmat('bm_ext_sol_lamB_fr_10_Rl_1e4.mat') 
u1f01  = result01['u1f'][0]
u2f01  = result01['u2f'][0]
x      = result01['x'][0]
x      = x*1000
result03 = sio.loadmat('bm_ext_sol_lamB_fr_30_Rl_1e4.mat') 
u1f03  = result03['u1f'][0]
u2f03  = result03['u2f'][0]
result05 = sio.loadmat('bm_ext_sol_lamB_fr_50_Rl_1e4.mat') 
u1f05  = result05['u1f'][0]
u2f05  = result05['u2f'][0]
result07 = sio.loadmat('bm_ext_sol_lamB_fr_70_Rl_1e4.mat') 
u1f07  = result07['u1f'][0]
u2f07  = result07['u2f'][0]
result09 = sio.loadmat('bm_ext_sol_lamB_fr_90_Rl_1e4.mat') 
u1f09  = result09['u1f'][0]
u2f09  = result09['u2f'][0]


u1f01 = np.abs(u1f01)
u2f01 = np.abs(u2f01)

# u1f03 = np.abs(u1f03)
# u1f03 = np.concatenate(( np.abs(u1f03[0:41]), -np.abs(u1f03[41:101]) ),axis=0)
# u2f03 = np.concatenate(( np.abs(u2f03[0:62]), -np.abs(u2f03[62:101]) ),axis=0)

# u1f05 = np.abs(u1f05)
# u2f05 = np.concatenate(( np.abs(u2f05[0:74]), -np.abs(u2f05[74:101]) ),axis=0)

# u1f07 = np.concatenate(( np.abs(u1f07[0:75]), -np.abs(u1f07[75:101]) ),axis=0)
# u2f07 = np.concatenate(( -np.abs(u2f07[0:78]), np.abs(u2f07[78:101]) ),axis=0)

# u1f09 = np.concatenate(( np.abs(u1f09[0:53]), -np.abs(u1f09[53:101]) ),axis=0)
# u2f09 = np.concatenate(( -np.abs(u2f09[0:23]), np.abs(u2f09[23:81]), -np.abs(u2f09[81:101]) ),axis=0)


fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18,10))

axes[0,0].plot(x*lp, u1f01, 'b-', label= 'Primary Beam', linewidth=6)
axes[0,0].plot(le*x + lp*1000, u2f01, 'b--', label= 'Extension Beam', linewidth=2)
axes[0,0].set_ylabel('Normalized beam displacement', fontsize=18)

axes[0,1].plot(x*lp, u1f03, 'b-', label= 'Primary Beam', linewidth=6)
axes[0,1].plot(le*x + lp*1000, u2f03, 'b--', label= 'Extension Beam', linewidth=2)

axes[0,2].plot(x*lp, u1f05, 'b-', label= 'Primary Beam', linewidth=6)
axes[0,2].plot(le*x + lp*1000, u2f05, 'b--', label= 'Extension Beam', linewidth=2)
axes[0,2].set_xlabel('Streamwise beam position (mm)', fontsize=18)

axes[1,0].plot(x*lp, u1f07, 'b-', label= 'Primary Beam', linewidth=6)
axes[1,0].plot(le*x + lp*1000, u2f07, 'b--', label= 'Extension Beam', linewidth=2)
axes[1,0].set_xlabel('Streamwise beam position (mm)', fontsize=18)
axes[1,0].set_ylabel('Normalized beam displacement', fontsize=18)

axes[1,1].plot(x*lp, u1f09, 'b-', label= 'Primary Beam', linewidth=6)
axes[1,1].plot(le*x + lp*1000, u2f09, 'b--', label= 'Extension Beam', linewidth=2)
axes[1,1].set_xlim(0.0, (lp+le)*1000)
axes[1,1].set_xlabel('Streamwise beam position (mm)', fontsize=18)
# axes[1,1].set_ylabel('Normalized beam displacement', fontsize=18)


axes[1,2].set_frame_on(False)
axes[1,2].get_xaxis().set_visible(False)
axes[1,2].get_yaxis().set_visible(False)
axes[1,2].plot(0, 0, 'b-', label= 'Primary Beam', linewidth=6)
axes[1,2].plot(0, 0, 'b--', label= 'Extension Beam', linewidth=2)
axes[1,2].legend(loc = 'center', ncol =1, fontsize=18)


plt.text(0.02, 0.91, "(a) $f_b = 10\\ Hz$", fontweight="bold", transform=axes[0,0].transAxes, fontsize=18)
plt.text(0.02, 0.91, "(b) $f_b = 30\\ Hz$", fontweight="bold", transform=axes[0,1].transAxes, fontsize=18)
plt.text(0.02, 0.91, "(c) $f_b = 50\\ Hz$", fontweight="bold", transform=axes[0,2].transAxes, fontsize=18)
plt.text(0.02, 0.91, "(d) $f_b = 70\\ Hz$", fontweight="bold", transform=axes[1,0].transAxes, fontsize=18)
plt.text(0.02, 0.91, "(e) $f_b = 90\\ Hz$", fontweight="bold", transform=axes[1,1].transAxes, fontsize=18)
plt.subplots_adjust(left=0.05, right=0.98, top=0.96, bottom=0.07, wspace=0.15, hspace=0.10)

plt.savefig("fig_vibration_profile_vs_fr_Rl_lamB_all.pdf")
plt.savefig("fig_vibration_profile_vs_fr_Rl_lamB_all.eps")
plt.savefig("fig_vibration_profile_vs_fr_Rl_lamB_all.jpg", dpi=300)


plt.show()
