import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

lp = 100e-3
le = 100e-3


result00 = sio.loadmat('bm_ext_sol_laml_fr_1_Rl_1e4.mat') 
u1f00  = result00['u1f'][0]
u2f00  = result00['u2f'][0]
x      = result00['x'][0]
x      = x*1000
result01 = sio.loadmat('bm_ext_sol_laml_fr_10_Rl_1e4.mat') 
u1f01  = result01['u1f'][0]
u2f01  = result01['u2f'][0]
result02 = sio.loadmat('bm_ext_sol_laml_fr_20_Rl_1e4.mat') 
u1f02  = result02['u1f'][0]
u2f02  = result02['u2f'][0]
result03 = sio.loadmat('bm_ext_sol_laml_fr_30_Rl_1e4.mat') 
u1f03  = result03['u1f'][0]
u2f03  = result03['u2f'][0]
result04 = sio.loadmat('bm_ext_sol_laml_fr_40_Rl_1e4.mat') 
u1f04  = result04['u1f'][0]
u2f04  = result04['u2f'][0]
result05 = sio.loadmat('bm_ext_sol_laml_fr_50_Rl_1e4.mat') 
u1f05  = result05['u1f'][0]
u2f05  = result05['u2f'][0]
result06 = sio.loadmat('bm_ext_sol_laml_fr_60_Rl_1e4.mat') 
u1f06  = result06['u1f'][0]
u2f06  = result06['u2f'][0]
result07 = sio.loadmat('bm_ext_sol_laml_fr_70_Rl_1e4.mat') 
u1f07  = result07['u1f'][0]
u2f07  = result07['u2f'][0]
result08 = sio.loadmat('bm_ext_sol_laml_fr_80_Rl_1e4.mat') 
u1f08  = result08['u1f'][0]
u2f08  = result08['u2f'][0]
result09 = sio.loadmat('bm_ext_sol_laml_fr_90_Rl_1e4.mat') 
u1f09  = result09['u1f'][0]
u2f09  = result09['u2f'][0]
result10 = sio.loadmat('bm_ext_sol_laml_fr_100_Rl_1e4.mat') 
u1f10  = result10['u1f'][0]
u2f10  = result10['u2f'][0]



u1f00 = np.abs(u1f00)
u2f00 = np.abs(u2f00)

u1f02 = np.abs(u1f02)
u2f02 = np.concatenate(( np.abs(u2f02[0:62]), -np.abs(u2f02[62:101]) ),axis=0)

u1f04 = np.abs(u1f04)
u2f04 = np.concatenate(( np.abs(u2f04[0:74]), -np.abs(u2f04[74:101]) ),axis=0)

u1f06 = np.concatenate(( np.abs(u1f06[0:75]), -np.abs(u1f06[75:101]) ),axis=0)
u2f06 = np.concatenate(( -np.abs(u2f06[0:78]), np.abs(u2f06[78:101]) ),axis=0)

u1f08 = np.concatenate(( np.abs(u1f08[0:53]), -np.abs(u1f08[53:101]) ),axis=0)
u2f08 = np.concatenate(( -np.abs(u2f08[0:23]), np.abs(u2f08[23:81]), -np.abs(u2f08[81:101]) ),axis=0)

u1f10 = np.concatenate(( np.abs(u1f10[0:65]), -np.abs(u1f10[65:101]) ),axis=0)
u2f10 = np.concatenate(( -np.abs(u2f10[0:33]), np.abs(u2f10[33:83]), -np.abs(u2f10[83:101]) ),axis=0)

# plt.figure(1)
# plt.subplot(2,3,1)
# plt.plot(x*lp, u1f00, 'b-', label= 'Primary Beam', linewidth=6)
# plt.plot(le*x + lp*1000, u2f00, 'b--', label= 'Extension Beam', linewidth=2)

# plt.subplot(2,3,2)
# plt.plot(x*lp, u1f02, 'b-', label= 'Primary Beam', linewidth=6)
# plt.plot(le*x + lp*1000, u2f02, 'b--', label= 'Extension Beam', linewidth=2)

# plt.subplot(2,3,3)
# plt.plot(x*lp, u1f04, 'b-', label= 'Primary Beam', linewidth=6)
# plt.plot(le*x + lp*1000, u2f04, 'b--', label= 'Extension Beam', linewidth=2)

# plt.subplot(2,3,4)
# plt.plot(x*lp, u1f06, 'b-', label= 'Primary Beam', linewidth=6)
# plt.plot(le*x + lp*1000, u2f06, 'b--', label= 'Extension Beam', linewidth=2)

# plt.subplot(2,3,5)
# plt.plot(x*lp, u1f08, 'b-', label= 'Primary Beam', linewidth=6)
# plt.plot(le*x + lp*1000, u2f08, 'b--', label= 'Extension Beam', linewidth=2)

# plt.subplot(2,3,6)
# plt.plot(x*lp, u1f10, 'b-', label= 'Primary Beam', linewidth=6)
# plt.plot(le*x + lp*1000, u2f10, 'b--', label= 'Extension Beam', linewidth=2)

# # plt.legend(loc='upper left', ncol=2)
# plt.xlim(0.0, (lp+le)*1000)
# plt.xlabel('Streamwise beam position (mm)')
# plt.ylabel('Normalized beam displacement')



# print(np.abs(u1f09))
# print(np.abs(u2f09))

u1f01 = np.abs(u1f01)
u2f01 = np.abs(u2f01)

u1f03 = np.abs(u1f03)
u2f03 = np.concatenate(( np.abs(u2f03[0:70]), -np.abs(u2f03[70:101]) ),axis=0)

u1f05 = np.concatenate(( np.abs(u1f05[0:49]), -np.abs(u1f05[49:101]) ),axis=0)
u2f05 = np.concatenate(( -np.abs(u2f05[0:77]), np.abs(u2f05[77:101]) ),axis=0)

u1f07 = np.abs(u1f07)
u2f07 = np.concatenate(( np.abs(u2f07[0:13]), -np.abs(u2f07[13:80]), np.abs(u2f07[80:101]) ),axis=0)

u1f09 = np.concatenate(( np.abs(u1f09[0:62]), -np.abs(u1f09[62:101]) ),axis=0)
u2f09 = np.concatenate(( -np.abs(u2f09[0:29]), np.abs(u2f09[29:82]), -np.abs(u2f09[82:101]) ),axis=0)


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


plt.text(0.02, 0.93, "(a) $f_b = 10\ Hz$", fontweight="bold", transform=axes[0,0].transAxes, fontsize=18)
plt.text(0.02, 0.93, "(b) $f_b = 30\ Hz$", fontweight="bold", transform=axes[0,1].transAxes, fontsize=18)
plt.text(0.02, 0.93, "(c) $f_b = 50\ Hz$", fontweight="bold", transform=axes[0,2].transAxes, fontsize=18)
plt.text(0.02, 0.93, "(d) $f_b = 70\ Hz$", fontweight="bold", transform=axes[1,0].transAxes, fontsize=18)
plt.text(0.02, 0.93, "(e) $f_b = 90\ Hz$", fontweight="bold", transform=axes[1,1].transAxes, fontsize=18)
plt.subplots_adjust(left=0.05, right=0.98, top=0.96, bottom=0.07, wspace=0.15, hspace=0.10)

plt.savefig("fig_vibration_profile_vs_fr_Rl_laml_all.pdf")
plt.savefig("fig_vibration_profile_vs_fr_Rl_laml_all.eps")
plt.savefig("fig_vibration_profile_vs_fr_Rl_laml_all.jpg", dpi=300)


plt.show()