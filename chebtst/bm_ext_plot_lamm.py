from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.ticker as mtick

result01  = sio.loadmat('bm_ext_base_lamm_rhoe_1p38e1.mat'); 
vplist01  = result01['Vplist'];
pplist01  = result01['Pplist'];
result02  = sio.loadmat('bm_ext_base_lamm_rhoe_1p38e2.mat'); 
vplist02  = result02['Vplist'];
pplist02  = result02['Pplist'];
result03  = sio.loadmat('bm_ext_base_lamm_rhoe_1p38e3.mat'); 
vplist03  = result03['Vplist'];
pplist03  = result03['Pplist'];
result04  = sio.loadmat('bm_ext_base_lamm_rhoe_1p38e4.mat'); 
vplist04  = result04['Vplist'];
pplist04  = result04['Pplist'];
result05  = sio.loadmat('bm_ext_base_lamm_rhoe_1p38e5.mat'); 
vplist05  = result05['Vplist'];
pplist05  = result05['Pplist'];

fr        = result01['fr'];
wr        = 2*np.pi*fr;
Rl        = result01['Rl'];
xib       = result01['xib'];

am_vplist01, ph_vplist01 = np.abs(vplist01), np.angle(vplist01)
am_vplist02, ph_vplist02 = np.abs(vplist02), np.angle(vplist02)
am_vplist03, ph_vplist03 = np.abs(vplist03), np.angle(vplist03)
am_vplist04, ph_vplist04 = np.abs(vplist04), np.angle(vplist04)
am_vplist05, ph_vplist05 = np.abs(vplist05), np.angle(vplist05)

am_pplist01, ph_pplist01 = np.abs(pplist01), np.angle(pplist01) 
am_pplist02, ph_pplist02 = np.abs(pplist02), np.angle(pplist02) 
am_pplist03, ph_pplist03 = np.abs(pplist03), np.angle(pplist03) 
am_pplist04, ph_pplist04 = np.abs(pplist04), np.angle(pplist04) 
am_pplist05, ph_pplist05 = np.abs(pplist05), np.angle(pplist05) 

lamm_list = sio.loadmat('bm_ext_base_lamm_rhoe_list.mat')['lamm_list']
lamm_list = np.transpose(lamm_list)
rhoe_list = sio.loadmat('bm_ext_base_lamm_rhoe_list.mat')['rhoe_list']
rhoe_list = np.transpose(rhoe_list)

def plot_vol_lamm_vs_fr_Rl():
    fig01, ax = plt.subplots(ncols=2, nrows=2, figsize=(24,12), sharex=True)

    ax[0,0].plot(fr[0,:].reshape(-1,1),(am_vplist01[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1),(am_vplist01[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1),(am_vplist01[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1),(am_vplist01[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\\Omega$')
    ax[0,0].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[0][0], 
        lamm_list[0][0]), fontsize=18)
    ax[0,0].set_xlim(1,100)
    ax[0,0].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $f_b$')
    ax[0,0].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    # ax[0,0].legend(loc='lower right', ncol=2, fontsize=18)


    ax[0,1].plot(fr[0,:].reshape(-1,1),(am_vplist02[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1),(am_vplist02[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1),(am_vplist02[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1),(am_vplist02[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\\Omega$')
    ax[0,1].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[1][0], 
        lamm_list[1][0]), fontsize=18)
    ax[0,1].set_xlim(1,100)
    ax[0,1].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $f_b$')
    # ax[0,1].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    # ax[0,1].legend(loc='lower right', ncol=2, fontsize=18)

    ax[1,0].plot(fr[0,:].reshape(-1,1),(am_vplist03[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1),(am_vplist03[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1),(am_vplist03[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1),(am_vplist03[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\\Omega$')
    ax[1,0].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[2][0], 
        lamm_list[2][0]), fontsize=18)
    ax[1,0].set_xlim(1,100)
    ax[1,0].set_yscale('log')
    ax[1,0].set_xlabel('Base excitation frequency $f_b$', fontsize=18)
    ax[1,0].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    # ax[1,0].legend(loc='lower right', ncol=2, fontsize=18)


    ax[1,1].plot(fr[0,:].reshape(-1,1),am_vplist04[0,:],'r', label= '$R_l$ = 1 $\\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1),am_vplist04[2,:],'b.', label= '$R_l$ = 100 $\\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1),am_vplist04[4,:],'m*', label= '$R_l$ = 10 k$\\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1),am_vplist04[6,:],'k--', label= '$R_l$ = 1 M$\\Omega$')
    ax[1,1].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[3][0], 
        lamm_list[3][0]), fontsize=18)
    ax[1,1].set_xlim(1,100)
    ax[1,1].set_yscale('log')
    ax[1,1].set_xlabel('Base excitation frequency $f_b$', fontsize=18)
    # ax[1,1].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    # ax[1,1].legend(loc='lower right', ncol=2, fontsize=18)


    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=ax[0,0].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=ax[0,1].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=ax[1,0].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=ax[1,1].transAxes, fontsize=24)

    ax[0,0].legend(bbox_to_anchor=(0.0, 1.10, 2.08, .102), loc=3, ncol=4, mode="expand", borderaxespad=0, fontsize=24)
    # plt.suptitle('Amplitude of the output voltage $V_p$ versus base excitation frequency $f_b$ at different $R_l$ and $\\lambda_m$', fontsize=24)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.08, hspace=0.17)

    plt.savefig("fig_output_voltage_vs_fr_Rl_lamm_all.pdf")
    plt.savefig("fig_output_voltage_vs_fr_Rl_lamm_all.eps")
    plt.savefig("fig_output_voltage_vs_fr_Rl_lamm_all.jpg",dpi=300)
    # plt.show()

def plot_pow_lamm_vs_fr_Rl():
    fig01, ax = plt.subplots(ncols=2, nrows=2, figsize=(24,12), sharex=True)

    ax[0,0].plot(fr[0,:].reshape(-1,1),(am_pplist01[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1),(am_pplist01[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1),(am_pplist01[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1),(am_pplist01[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\\Omega$')
    ax[0,0].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[0][0], 
        lamm_list[0][0]), fontsize=18)
    ax[0,0].set_xlim(1,100)
    ax[0,0].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $f_b$')
    ax[0,0].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    # ax[0,0].legend(loc='lower right', ncol=2, fontsize=18)


    ax[0,1].plot(fr[0,:].reshape(-1,1),(am_pplist02[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1),(am_pplist02[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1),(am_pplist02[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1),(am_pplist02[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\\Omega$')
    ax[0,1].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[1][0], 
        lamm_list[1][0]), fontsize=18)
    ax[0,1].set_xlim(1,100)
    ax[0,1].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $f_b$')
    # ax[0,1].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    # ax[0,1].legend(loc='lower right', ncol=2, fontsize=18)

    ax[1,0].plot(fr[0,:].reshape(-1,1),(am_pplist03[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1),(am_pplist03[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1),(am_pplist03[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1),(am_pplist03[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\\Omega$')
    ax[1,0].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[2][0], 
        lamm_list[2][0]), fontsize=18)
    ax[1,0].set_xlim(1,100)
    ax[1,0].set_yscale('log')
    ax[1,0].set_xlabel('Base excitation frequency $f_b$', fontsize=18)
    ax[1,0].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    # ax[1,0].legend(loc='lower right', ncol=2, fontsize=18)


    ax[1,1].plot(fr[0,:].reshape(-1,1),am_pplist04[0,:],'r', label= '$R_l$ = 1 $\\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1),am_pplist04[2,:],'b.', label= '$R_l$ = 100 $\\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1),am_pplist04[4,:],'m*', label= '$R_l$ = 10 k$\\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1),am_pplist04[6,:],'k--', label= '$R_l$ = 1 M$\\Omega$')
    ax[1,1].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[3][0], 
        lamm_list[3][0]), fontsize=18)
    ax[1,1].set_xlim(1,100)
    ax[1,1].set_yscale('log')
    ax[1,1].set_xlabel('Base excitation frequency $f_b$', fontsize=18)
    # ax[1,1].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    # ax[1,1].legend(loc='lower right', ncol=2, fontsize=18)


    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=ax[0,0].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=ax[0,1].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=ax[1,0].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=ax[1,1].transAxes, fontsize=24)

    ax[0,0].legend(bbox_to_anchor=(0.0, 1.10, 2.08, .102), loc=3, ncol=4, mode="expand", borderaxespad=0, fontsize=24)
    # plt.suptitle('Amplitude of the output voltage $V_p$ versus base excitation frequency $f_b$ at different $R_l$ and $\\lambda_m$', fontsize=24)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.08, hspace=0.17)

    plt.savefig("fig_output_power_vs_fr_Rl_lamm_all.pdf")
    # plt.savefig("fig_output_power_vs_fr_Rl_lamm_all.eps")
    # plt.savefig("fig_output_power_vs_fr_Rl_lamm_all.jpg", dpi=300)
    # plt.show()

def plot_vol_lamm_list_vs_fr_Rl():
    fig, axes = plt.subplots(ncols = 2, nrows = 2, figsize=(24,12), sharex=True)
    axes[0,0].plot(Rl[:,0],am_vplist02[:,200], 'r-*', label='fr=10 $Hz$')
    axes[0,0].plot(Rl[:,0],am_vplist02[:,300], 'g-.', label='fr=31.62 $Hz$')
    axes[0,0].plot(Rl[:,0],am_vplist02[:,325], 'b--', label='fr=42.17 $Hz$')
    axes[0,0].plot(Rl[:,0],am_vplist02[:,350], 'm-', label='fr=56.23 $Hz$')
    axes[0,0].plot(Rl[:,0],am_vplist02[:,375], 'c-d', label='fr=74.99 $Hz$')
    axes[0,0].plot(Rl[:,0],am_vplist02[:,400], 'k-o', label='fr=100 $Hz$')
    axes[0,0].set_xscale('log')
    axes[0,0].set_yscale('log')
    axes[0,0].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[1][0], lamm_list[1][0]), fontsize=18)
    axes[0,0].legend(loc='lower right', ncol=2)
    # axes[0,0].set_xlabel('Externally connected resistance $R_l$ ($\\Omega$)')
    axes[0,0].set_ylabel('Amplitude of the output voltage $V_p$ (V)', fontsize=18)

    axes[0,1].plot(Rl[:,0],am_vplist03[:,200], 'r-*', label='fr=10 $Hz$')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,300], 'g-.', label='fr=31.62 $Hz$')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,325], 'b--', label='fr=42.17 $Hz$')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,350], 'm-', label='fr=56.23 $Hz$')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,375], 'c-d', label='fr=74.99 $Hz$')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,400], 'k-o', label='fr=100 $Hz$')
    # axes[0,1].set_xscale('log')
    axes[0,1].set_yscale('log')
    axes[0,1].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[2][0], lamm_list[2][0]), fontsize=18)
    axes[0,1].legend(loc='lower right', ncol=2)
    # axes[0,1].set_xlabel('Externally connected resistance $R_l$ ($\\Omega$)')
    # axes[0,1].set_ylabel('Amplitude of the output power $P_p$ (W)')

    axes[1,0].plot(Rl[:,0],am_vplist04[:,200], 'r-*', label='fr=10 $Hz$')
    axes[1,0].plot(Rl[:,0],am_vplist04[:,300], 'g-.', label='fr=31.62 $Hz$')
    axes[1,0].plot(Rl[:,0],am_vplist04[:,325], 'b--', label='fr=42.17 $Hz$')
    axes[1,0].plot(Rl[:,0],am_vplist04[:,350], 'm-', label='fr=56.23 $Hz$')
    axes[1,0].plot(Rl[:,0],am_vplist04[:,375], 'c-d', label='fr=74.99 $Hz$')
    axes[1,0].plot(Rl[:,0],am_vplist04[:,400], 'k-o', label='fr=100 $Hz$')
    # axes[1,0].set_xscale('log')
    axes[1,0].set_yscale('log')
    axes[1,0].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[3][0], lamm_list[3][0]), fontsize=18)
    axes[1,0].legend(loc='lower right', ncol=2)
    axes[1,0].set_xlabel('Externally connected resistance $R_l$ ($\\Omega$)', fontsize=18)
    axes[1,0].set_ylabel('Amplitude of the output voltage $V_p$ (V)', fontsize=18)


    axes[1,1].plot(Rl[:,0],am_vplist05[:,200], 'r-*', label='fr=10 $Hz$')
    axes[1,1].plot(Rl[:,0],am_vplist05[:,300], 'g-.', label='fr=31.62 $Hz$')
    axes[1,1].plot(Rl[:,0],am_vplist05[:,325], 'b--', label='fr=42.17 $Hz$')
    axes[1,1].plot(Rl[:,0],am_vplist05[:,350], 'm-', label='fr=56.23 $Hz$')
    axes[1,1].plot(Rl[:,0],am_vplist05[:,375], 'c-d', label='fr=74.99 $Hz$')
    axes[1,1].plot(Rl[:,0],am_vplist05[:,400], 'k-o', label='fr=100 $Hz$')
    # axes[1,1].set_xscale('log')
    axes[1,1].set_yscale('log')
    axes[1,1].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[4][0], lamm_list[4][0]), fontsize=18)
    axes[1,1].legend(loc='lower right', ncol=2)
    axes[1,1].set_xlabel('Externally connected resistance $R_l$ ($\\Omega$)', fontsize=18)
    # axes[1,1].set_ylabel('Amplitude of the output voltage $V_p$ (W)')


    # print(fr[0,200],fr[0,300],fr[0,325],fr[0,350],fr[0,375],fr[0,400])
    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=axes[0,0].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=axes[0,1].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=axes[1,0].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=axes[1,1].transAxes, fontsize=24)
    plt.suptitle("Amplitude of the output voltage $V_p$ versus externally connected resistance $R_l$ at different $f_b$ and $\\lambda_m$", fontsize=24)

    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.15, hspace=0.17)
    plt.savefig("fig_vol_lamm_list_vs_fr_Rl.pdf")
    plt.savefig("fig_vol_lamm_list_vs_fr_Rl.eps")
    plt.savefig("fig_vol_lamm_list_vs_fr_Rl.jpg", dpi=300)
    plt.show()

def plot_pow_lamm_list_vs_fr_Rl():
    fig, axes = plt.subplots(ncols = 2, nrows = 2, figsize=(24,12), sharex=True)
    axes[0,0].plot(Rl[:,0],am_pplist02[:,200], 'r-*', label='fr=10 $Hz$')
    axes[0,0].plot(Rl[:,0],am_pplist02[:,300], 'g-.', label='fr=31.62 $Hz$')
    axes[0,0].plot(Rl[:,0],am_pplist02[:,325], 'b--', label='fr=42.17 $Hz$')
    axes[0,0].plot(Rl[:,0],am_pplist02[:,350], 'm-', label='fr=56.23 $Hz$')
    axes[0,0].plot(Rl[:,0],am_pplist02[:,375], 'c-d', label='fr=74.99 $Hz$')
    axes[0,0].plot(Rl[:,0],am_pplist02[:,400], 'k-o', label='fr=100 $Hz$')
    axes[0,0].set_xscale('log')
    axes[0,0].set_yscale('log')
    axes[0,0].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[1][0], lamm_list[1][0]), fontsize=18)
    axes[0,0].legend(loc='lower right', ncol=2)
    # axes[0,0].set_xlabel('Externally connected resistance $R_l$ ($\\Omega$)')
    axes[0,0].set_ylabel('Amplitude of the output power $P_p$ (W)', fontsize=18)

    axes[0,1].plot(Rl[:,0],am_pplist03[:,200], 'r-*', label='fr=10 $Hz$')
    axes[0,1].plot(Rl[:,0],am_pplist03[:,300], 'g-.', label='fr=31.62 $Hz$')
    axes[0,1].plot(Rl[:,0],am_pplist03[:,325], 'b--', label='fr=42.17 $Hz$')
    axes[0,1].plot(Rl[:,0],am_pplist03[:,350], 'm-', label='fr=56.23 $Hz$')
    axes[0,1].plot(Rl[:,0],am_pplist03[:,375], 'c-d', label='fr=74.99 $Hz$')
    axes[0,1].plot(Rl[:,0],am_pplist03[:,400], 'k-o', label='fr=100 $Hz$')
    # axes[0,1].set_xscale('log')
    axes[0,1].set_yscale('log')
    axes[0,1].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[2][0], lamm_list[2][0]), fontsize=18)
    axes[0,1].legend(loc='lower right', ncol=2)
    # axes[0,1].set_xlabel('Externally connected resistance $R_l$ ($\\Omega$)')
    # axes[0,1].set_ylabel('Amplitude of the output power $P_p$ (W)')

    axes[1,0].plot(Rl[:,0],am_pplist04[:,200], 'r-*', label='fr=10 $Hz$')
    axes[1,0].plot(Rl[:,0],am_pplist04[:,300], 'g-.', label='fr=31.62 $Hz$')
    axes[1,0].plot(Rl[:,0],am_pplist04[:,325], 'b--', label='fr=42.17 $Hz$')
    axes[1,0].plot(Rl[:,0],am_pplist04[:,350], 'm-', label='fr=56.23 $Hz$')
    axes[1,0].plot(Rl[:,0],am_pplist04[:,375], 'c-d', label='fr=74.99 $Hz$')
    axes[1,0].plot(Rl[:,0],am_pplist04[:,400], 'k-o', label='fr=100 $Hz$')
    # axes[1,0].set_xscale('log')
    axes[1,0].set_yscale('log')
    axes[1,0].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[3][0], lamm_list[3][0]), fontsize=18)
    axes[1,0].legend(loc='lower right', ncol=2)
    axes[1,0].set_xlabel('Externally connected resistance $R_l$ ($\\Omega$)', fontsize=18)
    axes[1,0].set_ylabel('Amplitude of the output power $P_p$ (W)', fontsize=18)


    axes[1,1].plot(Rl[:,0],am_pplist05[:,200], 'r-*', label='fr=10 $Hz$')
    axes[1,1].plot(Rl[:,0],am_pplist05[:,300], 'g-.', label='fr=31.62 $Hz$')
    axes[1,1].plot(Rl[:,0],am_pplist05[:,325], 'b--', label='fr=42.17 $Hz$')
    axes[1,1].plot(Rl[:,0],am_pplist05[:,350], 'm-', label='fr=56.23 $Hz$')
    axes[1,1].plot(Rl[:,0],am_pplist05[:,375], 'c-d', label='fr=74.99 $Hz$')
    axes[1,1].plot(Rl[:,0],am_pplist05[:,400], 'k-o', label='fr=100 $Hz$')
    # axes[1,1].set_xscale('log')
    axes[1,1].set_yscale('log')
    axes[1,1].set_title('$\\rho_e$={0:1.2e}, $\\lambda_m$={1:1.2e}'.format(rhoe_list[4][0], lamm_list[4][0]), fontsize=18)
    axes[1,1].legend(loc='lower right', ncol=2)
    axes[1,1].set_xlabel('Externally connected resistance $R_l$ ($\\Omega$)', fontsize=18)
    # axes[1,1].set_ylabel('Amplitude of the output power $P_p$ (W)')


    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=axes[0,0].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=axes[0,1].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=axes[1,0].transAxes, fontsize=24)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=axes[1,1].transAxes, fontsize=24)
    plt.suptitle("Amplitude of the output power $P_p$ versus externally connected resistance $R_l$ at different $f_b$ and $\\lambda_m$", fontsize=24)

    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.15, hspace=0.17)
    plt.savefig("fig_pow_lamm_list_vs_fr_Rl.pdf")
    plt.savefig("fig_pow_lamm_list_vs_fr_Rl.eps")
    plt.savefig("fig_pow_lamm_list_vs_fr_Rl.jpg", dpi=300)
    plt.show()

def plot_vol_fr_sl_Rl_sl_vs_lamm():
    fig, axes = plt.subplots(nrows = 2, ncols = 3, figsize=(24,12), sharex=True)

    am_vplist = np.array([am_vplist01, am_vplist02, am_vplist03,
                 am_vplist04, am_vplist05])
    am_pplist = np.array([am_pplist01, am_pplist02, am_pplist03,
                 am_pplist04, am_pplist05])

    class ScalarFormatterForceFormat(mtick.ScalarFormatter):
        def _set_format(self,vmin,vmax):  # Override function that finds format to use.
            self.format = "%1.2f"  # Give format here
    
    yfmt = ScalarFormatterForceFormat()
    yfmt.set_powerlimits((0,0))

    axes[0,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 0]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 1 $\\Omega$')
    axes[0,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 0]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 1 $\\Omega$')
    axes[0,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 0]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 1 $\\Omega$')
    axes[0,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 0]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 1 $\\Omega$')
    axes[0,0].yaxis.set_major_formatter(yfmt)
    axes[0,0].set_xscale('log')
    axes[0,0].set_yscale('log')
    # axes[0,0].set_ylim(1e-10,1e-1)
    axes[0,0].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[0,0].set_title('$f_b$ = 1 $Hz$', fontsize=18)
    axes[0,0].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    # axes[0,0].legend(loc='upper left', ncol=2, fontsize=18)


    axes[0,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 100]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 100 $\\Omega$')
    axes[0,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 100]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 100 $\\Omega$')
    axes[0,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 100]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 100 $\\Omega$')
    axes[0,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 100]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 100 $\\Omega$')
    axes[0,1].yaxis.set_major_formatter(yfmt)
    axes[0,1].set_xscale('log')
    axes[0,1].set_yscale('log')
    # axes[0,1].set_ylim(1e-8,1e0)
    axes[0,1].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[0,1].set_title('$f_b$ = 3.162 $Hz$', fontsize=18)
    # axes[0,1].legend(loc='upper left', ncol=2, fontsize=18)

    axes[0,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 200]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 10 k$\\Omega$')
    axes[0,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 200]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 10 k$\\Omega$')
    axes[0,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 200]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 10 k$\\Omega$')
    axes[0,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 200]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 10 k$\\Omega$')
    axes[0,2].yaxis.set_major_formatter(yfmt)
    axes[0,2].set_xscale('log')
    axes[0,2].set_yscale('log')
    # axes[0,2].set_ylim(1e-7,1e1)
    axes[0,2].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[0,2].set_title('$f_b$ = 10 $Hz$', fontsize=18)
    # axes[0,2].legend(loc='upper left', ncol=2, fontsize=18)


    axes[1,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 300]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 1 $\\Omega$')
    axes[1,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 300]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 1 $\\Omega$')
    axes[1,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 300]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 1 $\\Omega$')
    axes[1,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 300]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 1 $\\Omega$')
    axes[1,0].yaxis.set_major_formatter(yfmt)
    axes[1,0].set_xscale('log')
    axes[1,0].set_yscale('log')
    # axes[1,0].set_ylim(1e-5,1e3)
    axes[1,0].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[1,0].set_title('$f_b$ = 31.62 $Hz$', fontsize=18)
    axes[1,0].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    axes[1,0].set_xlabel('Line density ratio $\\lambda_m$', fontsize=18)
    # axes[1,0].legend(loc='upper left', ncol=2, fontsize=18)


    axes[1,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 325]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 100 $\\Omega$')
    axes[1,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 325]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 100 $\\Omega$')
    axes[1,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 325]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 100 $\\Omega$')
    axes[1,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 325]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 100 $\\Omega$')
    axes[1,1].yaxis.set_major_formatter(yfmt)
    axes[1,1].set_xscale('log')
    axes[1,1].set_yscale('log')
    # axes[1,1].set_ylim(1e-6,1e5)
    axes[1,1].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[1,1].set_title('$f_b$ = 42.17 $Hz$', fontsize=18)
    axes[1,1].set_xlabel('Line density ratio $\\lambda_m$', fontsize=18)
    # axes[1,1].legend(loc='upper left', ncol=2, fontsize=18)


    axes[1,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 400]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 10 k$\\Omega$')
    axes[1,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 400]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 10 k$\\Omega$')
    axes[1,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 400]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 10 k$\\Omega$')
    axes[1,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 400]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 10 k$\\Omega$')
    axes[1,2].yaxis.set_major_formatter(yfmt)
    axes[1,2].set_xscale('log')
    axes[1,2].set_yscale('log')
    # axes[1,2].set_ylim(1e-4,1e3)
    axes[1,2].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[1,2].set_title('$f_b$ = 100 $Hz$', fontsize=18)
    axes[1,2].set_xlabel('Line density ratio $\\lambda_m$', fontsize=18)
    # axes[1,2].legend(loc='upper left', ncol=2, fontsize=18)

    axes[0,0].legend(bbox_to_anchor=(0., 1.10, 3.3, .102), loc=3, ncol=4, mode="expand", borderaxespad=0, fontsize=24)
    # plt.suptitle('Amplitude of the output voltage $V_p$ versus line density ratio $\\lambda_m$ at different $f_b$ and $R_l$', fontsize=24)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.08, wspace=0.15, hspace=0.17)

    plt.savefig("fig_vol_fr_sl_Rl_sl_vs_lamm.pdf")
    plt.savefig("fig_vol_fr_sl_Rl_sl_vs_lamm.eps")
    plt.savefig("fig_vol_fr_sl_Rl_sl_vs_lamm.jpg",dpi=300)
    # plt.show()

def plot_pow_fr_sl_Rl_sl_vs_lamm():
    fig, axes = plt.subplots(nrows = 2, ncols = 3, figsize=(24,12), sharex=True)

    am_vplist = np.array([am_vplist01, am_vplist02, am_vplist03,
                 am_vplist04, am_vplist05])
    am_pplist = np.array([am_pplist01, am_pplist02, am_pplist03,
                 am_pplist04, am_pplist05])

    class ScalarFormatterForceFormat(mtick.ScalarFormatter):
        def _set_format(self,vmin,vmax):  # Override function that finds format to use.
            self.format = "%1.2f"  # Give format here
    
    yfmt = ScalarFormatterForceFormat()
    yfmt.set_powerlimits((0,0))


    axes[0,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 0]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 1 $\\Omega$')
    axes[0,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 0]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 1 $\\Omega$')
    axes[0,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 0]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 1 $\\Omega$')
    axes[0,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 0]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 1 $\\Omega$')
    axes[0,0].yaxis.set_major_formatter(yfmt)
    axes[0,0].set_xscale('log')
    axes[0,0].set_yscale('log')
    # axes[0,0].set_ylim(1e-10,1e-1)
    axes[0,0].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[0,0].set_title('$f_b$ = 1 $Hz$', fontsize=18)
    axes[0,0].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    # axes[0,0].legend(loc='upper left', ncol=2, fontsize=18)


    axes[0,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 100]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 100 $\\Omega$')
    axes[0,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 100]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 100 $\\Omega$')
    axes[0,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 100]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 100 $\\Omega$')
    axes[0,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 100]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 100 $\\Omega$')
    axes[0,1].yaxis.set_major_formatter(yfmt)
    axes[0,1].set_xscale('log')
    axes[0,1].set_yscale('log')
    # axes[0,1].set_ylim(1e-8,1e0)
    axes[0,1].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[0,1].set_title('$f_b$ = 3.162 $Hz$', fontsize=18)
    # axes[0,1].legend(loc='upper left', ncol=2, fontsize=18)

    axes[0,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 200]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 10 k$\\Omega$')
    axes[0,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 200]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 10 k$\\Omega$')
    axes[0,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 200]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 10 k$\\Omega$')
    axes[0,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 200]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 10 k$\\Omega$')
    axes[0,2].yaxis.set_major_formatter(yfmt)
    axes[0,2].set_xscale('log')
    axes[0,2].set_yscale('log')
    # axes[0,2].set_ylim(1e-7,1e1)
    axes[0,2].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[0,2].set_title('$f_b$ = 10 $Hz$', fontsize=18)
    # axes[0,2].legend(loc='upper left', ncol=2, fontsize=18)


    axes[1,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 300]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 1 $\\Omega$')
    axes[1,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 300]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 1 $\\Omega$')
    axes[1,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 300]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 1 $\\Omega$')
    axes[1,0].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 300]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 1 $\\Omega$')
    axes[1,0].yaxis.set_major_formatter(yfmt)
    axes[1,0].set_xscale('log')
    axes[1,0].set_yscale('log')
    # axes[1,0].set_ylim(1e-5,1e3)
    axes[1,0].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[1,0].set_title('$f_b$ = 31.62 $Hz$', fontsize=18)
    axes[1,0].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    axes[1,0].set_xlabel('Line density ratio $\\lambda_m$', fontsize=18)
    # axes[1,0].legend(loc='upper left', ncol=2, fontsize=18)


    axes[1,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 325]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 100 $\\Omega$')
    axes[1,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 325]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 100 $\\Omega$')
    axes[1,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 325]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 100 $\\Omega$')
    axes[1,1].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 325]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 100 $\\Omega$')
    axes[1,1].yaxis.set_major_formatter(yfmt)
    axes[1,1].set_xscale('log')
    axes[1,1].set_yscale('log')
    # axes[1,1].set_ylim(1e-6,1e5)
    axes[1,1].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[1,1].set_title('$f_b$ = 42.17 $Hz$', fontsize=18)
    axes[1,1].set_xlabel('Line density ratio $\\lambda_m$', fontsize=18)
    # axes[1,1].legend(loc='upper left', ncol=2, fontsize=18)


    axes[1,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 0, 400]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 10 k$\\Omega$')
    axes[1,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 2, 400]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 10 k$\\Omega$')
    axes[1,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 4, 400]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 10 k$\\Omega$')
    axes[1,2].plot(lamm_list.reshape(-1,1),(am_vplist[:, 6, 400]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 10 k$\\Omega$')
    axes[1,2].yaxis.set_major_formatter(yfmt)
    axes[1,2].set_xscale('log')
    axes[1,2].set_yscale('log')
    # axes[1,2].set_ylim(1e-4,1e3)
    axes[1,2].set_xlim(np.min(lamm_list), np.max(lamm_list))
    axes[1,2].set_title('$f_b$ = 100 $Hz$', fontsize=18)
    axes[1,2].set_xlabel('Line density ratio $\\lambda_m$', fontsize=18)
    # axes[1,2].legend(loc='upper left', ncol=2, fontsize=18)

    axes[0,0].legend(bbox_to_anchor=(0., 1.10, 3.3, .102), loc=3, ncol=4, mode="expand", borderaxespad=0, fontsize=24)
    # plt.suptitle('Amplitude of the output voltage $V_p$ versus line density ratio $\\lambda_m$ at different $f_b$ and $R_l$', fontsize=24)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.08, wspace=0.15, hspace=0.17)
    
    plt.savefig("fig_pow_fr_sl_Rl_sl_vs_lamm.pdf")
    # plt.savefig("fig_pow_fr_sl_Rl_sl_vs_lamm.eps")
    # plt.savefig("fig_pow_fr_sl_Rl_sl_vs_lamm.jpg",dpi=300)
    # plt.show()


if __name__ == '__main__':
    # plot_vol_lamm_vs_fr_Rl()
    # plot_pow_lamm_vs_fr_Rl()
    # plot_vol_lamm_list_vs_fr_Rl()
    # plot_pow_lamm_list_vs_fr_Rl()
    plot_vol_fr_sl_Rl_sl_vs_lamm()
    plot_pow_fr_sl_Rl_sl_vs_lamm()