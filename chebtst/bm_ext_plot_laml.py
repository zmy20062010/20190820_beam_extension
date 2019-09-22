from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from cycler import cycler
import matplotlib.ticker as mtick
# mpl.rcParams['text.usetex'] = True
# mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

result00 = sio.loadmat('bm_ext_base_laml_l_00e-3.mat'); 
vplist00  = result00['Vplist'];
pplist00  = result00['Pplist'];
result01 = sio.loadmat('bm_ext_base_laml_l_10e-3.mat'); 
vplist01  = result01['Vplist'];
pplist01  = result01['Pplist'];
result02 = sio.loadmat('bm_ext_base_laml_l_20e-3.mat'); 
vplist02  = result02['Vplist'];
pplist02  = result02['Pplist'];
result03 = sio.loadmat('bm_ext_base_laml_l_30e-3.mat'); 
vplist03  = result03['Vplist'];
pplist03  = result03['Pplist'];
result04 = sio.loadmat('bm_ext_base_laml_l_40e-3.mat'); 
vplist04  = result04['Vplist'];
pplist04  = result04['Pplist'];
result05 = sio.loadmat('bm_ext_base_laml_l_50e-3.mat'); 
vplist05  = result05['Vplist'];
pplist05  = result05['Pplist'];
result06 = sio.loadmat('bm_ext_base_laml_l_60e-3.mat'); 
vplist06  = result06['Vplist'];
pplist06  = result06['Pplist'];
result07 = sio.loadmat('bm_ext_base_laml_l_70e-3.mat');
vplist07  = result07['Vplist'];
pplist07  = result07['Pplist'];
result08 = sio.loadmat('bm_ext_base_laml_l_80e-3.mat'); 
vplist08  = result08['Vplist'];
pplist08  = result08['Pplist'];
result09 = sio.loadmat('bm_ext_base_laml_l_90e-3.mat'); 
vplist09  = result09['Vplist'];
pplist09  = result09['Pplist'];
result10 = sio.loadmat('bm_ext_base_laml_l_100e-3.mat'); 
vplist10  = result10['Vplist'];
pplist10  = result10['Pplist'];

fr        = result01['fr']
wr        = 2*np.pi*fr
Rl        = result01['Rl']
xib       = result01['xib']

am_vplist00 = np.abs(vplist00)
am_vplist01 = np.abs(vplist01)
am_vplist02 = np.abs(vplist02)
am_vplist03 = np.abs(vplist03)
am_vplist04 = np.abs(vplist04)
am_vplist05 = np.abs(vplist05)
am_vplist06 = np.abs(vplist06)
am_vplist07 = np.abs(vplist07)
am_vplist08 = np.abs(vplist08)
am_vplist09 = np.abs(vplist09)
am_vplist10 = np.abs(vplist10)

ph_vplist00 = np.angle(vplist00)
ph_vplist01 = np.angle(vplist01)
ph_vplist02 = np.angle(vplist02)
ph_vplist03 = np.angle(vplist03)
ph_vplist04 = np.angle(vplist04)
ph_vplist05 = np.angle(vplist05)
ph_vplist06 = np.angle(vplist06)
ph_vplist07 = np.angle(vplist07)
ph_vplist08 = np.angle(vplist08)
ph_vplist09 = np.angle(vplist09)
ph_vplist10 = np.angle(vplist10)


am_pplist00 = np.abs(pplist00)
am_pplist01 = np.abs(pplist01)
am_pplist02 = np.abs(pplist02)
am_pplist03 = np.abs(pplist03)
am_pplist04 = np.abs(pplist04)
am_pplist05 = np.abs(pplist05)
am_pplist06 = np.abs(pplist06)
am_pplist07 = np.abs(pplist07)
am_pplist08 = np.abs(pplist08)
am_pplist09 = np.abs(pplist09)
am_pplist10 = np.abs(pplist10)

ph_pplist00 = np.angle(pplist00)
ph_pplist01 = np.angle(pplist01)
ph_pplist02 = np.angle(pplist02)
ph_pplist03 = np.angle(pplist03)
ph_pplist04 = np.angle(pplist04)
ph_pplist05 = np.angle(pplist05)
ph_pplist06 = np.angle(pplist06)
ph_pplist07 = np.angle(pplist07)
ph_pplist08 = np.angle(pplist08)
ph_pplist09 = np.angle(pplist09)
ph_pplist10 = np.angle(pplist10)




def plot_vol_laml_vs_fr_Rl():
    fig01, ax = plt.subplots(ncols = 3, nrows = 2, figsize=(24,12), sharex=True)

    # s1 = am_vplist00[0,:]/xib/wr[0,:]/wr[0,:]
    # s2 = fr[0,:].reshape(1,-1)
    # print(s1.shape, s2.shape)
    # print(s1)
    # print(s2)

    ax[0,0].plot(fr[0,:].reshape(-1,1), (am_vplist00[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1), (am_vplist00[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1), (am_vplist00[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1), (am_vplist00[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,0].set_title('$\lambda_l$=0.0', fontsize=24)
    ax[0,0].set_xlim(1,100)
    ax[0,0].set_yscale('log')
    # ax[0,0].set_xlabel('Base excitation frequency $f_b$', fontsize=18)
    ax[0,0].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    ax[0,0].legend(loc='lower right', ncol=2, fontsize=18)


    ax[0,1].plot(fr[0,:].reshape(-1,1), (am_vplist02[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1), (am_vplist02[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1), (am_vplist02[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1), (am_vplist02[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,1].set_title('$\lambda_l$=0.2', fontsize=24)
    ax[0,1].set_xlim(1,100)
    ax[0,1].set_yscale('log')
    # ax[0,1].set_xlabel('Base excitation frequency $f_b$', fontsize=18)
    # ax[0,1].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    ax[0,1].legend(loc='lower right',ncol=2, fontsize=18)


    ax[0,2].plot(fr[0,:].reshape(-1,1), (am_vplist04[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,2].plot(fr[0,:].reshape(-1,1), (am_vplist04[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,2].plot(fr[0,:].reshape(-1,1), (am_vplist04[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,2].plot(fr[0,:].reshape(-1,1), (am_vplist04[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,2].set_title('$\lambda_l$=0.4', fontsize=24)
    ax[0,2].set_xlim(1,100)
    ax[0,2].set_yscale('log')
    # ax[0,2].set_xlabel('Base excitation frequency $f_b$', fontsize=18)
    # ax[0,2].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    ax[0,2].legend(loc='lower right',ncol=2, fontsize=18)


    ax[1,0].plot(fr[0,:].reshape(-1,1), (am_vplist06[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1), (am_vplist06[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1), (am_vplist06[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1), (am_vplist06[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,0].set_title('$\lambda_l$=0.6', fontsize=24)
    ax[1,0].set_xlim(1,100)
    ax[1,0].set_yscale('log')
    ax[1,0].set_xlabel('Base excitation frequency $f_b$ ($Hz$)', fontsize=18)
    ax[1,0].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    ax[1,0].legend(loc='lower right',ncol=2, fontsize=24)


    ax[1,1].plot(fr[0,:].reshape(-1,1), (am_vplist08[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1), (am_vplist08[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1), (am_vplist08[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1), (am_vplist08[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,1].set_title('$\lambda_l$=0.8', fontsize=24)
    ax[1,1].set_xlim(1,100)
    ax[1,1].set_yscale('log')
    ax[1,1].set_xlabel('Base excitation frequency $f_b$ ($Hz$)', fontsize=18)
    # ax[1,1].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    ax[1,1].legend(loc='lower right',ncol=2, fontsize=18)


    ax[1,2].plot(fr[0,:].reshape(-1,1), (am_vplist10[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,2].plot(fr[0,:].reshape(-1,1), (am_vplist10[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,2].plot(fr[0,:].reshape(-1,1), (am_vplist10[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,2].plot(fr[0,:].reshape(-1,1), (am_vplist10[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,2].set_title('$\lambda_l$=1.0', fontsize=24)
    ax[1,2].set_xlim(1,100)
    ax[1,2].set_yscale('log')
    ax[1,2].set_xlabel('Base excitation frequency $f_b$ ($Hz$)', fontsize=18)
    # ax[1,2].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    ax[1,2].legend(loc='lower right',ncol=2, fontsize=18)


    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=ax[0,0].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=ax[0,1].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=ax[0,2].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=ax[1,0].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=ax[1,1].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(f)", fontweight="bold", transform=ax[1,2].transAxes, fontsize=18)
    # plt.suptitle('Amplitude of the output voltage $\\tilde{V}_p$ versus base excitation frequency $f_b$ at different $R_l$ and $\lambda_l$', fontsize=24)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.96, bottom=0.07, wspace=0.15, hspace=0.10)

    plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.pdf")
    plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.eps")
    plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.jpg", dpi=300)

    # plt.show()

def plot_pow_laml_vs_fr_Rl():
    fig01, ax = plt.subplots(ncols = 3, nrows = 2, figsize=(24,12), sharex=True)

    ax[0,0].plot(fr[0,:].reshape(-1,1), (am_pplist00[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1), (am_pplist00[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1), (am_pplist00[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,0].plot(fr[0,:].reshape(-1,1), (am_pplist00[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,0].set_title('$\lambda_l$=0.0', fontsize=24)
    ax[0,0].set_xlim(1,100)
    ax[0,0].set_yscale('log')
    # ax[0,0].set_xlabel('Base excitation frequency $f_b$ ($Hz$)', fontsize=18)
    ax[0,0].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    ax[0,0].legend(loc='lower right', ncol=2, fontsize=18)


    ax[0,1].plot(fr[0,:].reshape(-1,1), (am_pplist02[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1), (am_pplist02[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1), (am_pplist02[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,1].plot(fr[0,:].reshape(-1,1), (am_pplist02[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,1].set_title('$\lambda_l$=0.2', fontsize=24)
    ax[0,1].set_xlim(1,100)
    ax[0,1].set_yscale('log')
    # ax[0,1].set_xlabel('Base excitation frequency $f_b$ ($Hz$)', fontsize=18)
    # ax[0,1].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    ax[0,1].legend(loc='lower right',ncol=2, fontsize=18)


    ax[0,2].plot(fr[0,:].reshape(-1,1), (am_pplist04[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,2].plot(fr[0,:].reshape(-1,1), (am_pplist04[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,2].plot(fr[0,:].reshape(-1,1), (am_pplist04[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,2].plot(fr[0,:].reshape(-1,1), (am_pplist04[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,2].set_title('$\lambda_l$=0.4', fontsize=24)
    ax[0,2].set_xlim(1,100)
    ax[0,2].set_yscale('log')
    # ax[0,2].set_xlabel('Base excitation frequency $f_b$ ($Hz$)', fontsize=18)
    # ax[0,2].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    ax[0,2].legend(loc='lower right',ncol=2, fontsize=18)


    ax[1,0].plot(fr[0,:].reshape(-1,1), (am_pplist06[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1), (am_pplist06[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1), (am_pplist06[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,0].plot(fr[0,:].reshape(-1,1), (am_pplist06[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,0].set_title('$\lambda_l$=0.6', fontsize=24)
    ax[1,0].set_xlim(1,100)
    ax[1,0].set_yscale('log')
    ax[1,0].set_xlabel('Base excitation frequency $f_b$ ($Hz$)', fontsize=18)
    ax[1,0].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    ax[1,0].legend(loc='lower right',ncol=2, fontsize=18)


    ax[1,1].plot(fr[0,:].reshape(-1,1), (am_pplist08[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1), (am_pplist08[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1), (am_pplist08[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,1].plot(fr[0,:].reshape(-1,1), (am_pplist08[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,1].set_title('$\lambda_l$=0.8', fontsize=24)
    ax[1,1].set_xlim(1,100)
    ax[1,1].set_yscale('log')
    ax[1,1].set_xlabel('Base excitation frequency $f_b$ ($Hz$)', fontsize=18)
    # ax[1,1].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    ax[1,1].legend(loc='lower right',ncol=2, fontsize=18)


    ax[1,2].plot(fr[0,:].reshape(-1,1), (am_pplist10[0,:]/xib/wr[0,:]/wr[0,:]).T,'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,2].plot(fr[0,:].reshape(-1,1), (am_pplist10[2,:]/xib/wr[0,:]/wr[0,:]).T,'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,2].plot(fr[0,:].reshape(-1,1), (am_pplist10[4,:]/xib/wr[0,:]/wr[0,:]).T,'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,2].plot(fr[0,:].reshape(-1,1), (am_pplist10[6,:]/xib/wr[0,:]/wr[0,:]).T,'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,2].set_title('$\lambda_l$=1.0', fontsize=24)
    ax[1,2].set_xlim(1,100)
    ax[1,2].set_yscale('log')
    ax[1,2].set_xlabel('Base excitation frequency $f_b$ ($Hz$)', fontsize=18)
    # ax[1,2].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    ax[1,2].legend(loc='lower right',ncol=2, fontsize=18)


    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=ax[0,0].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=ax[0,1].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=ax[0,2].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=ax[1,0].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=ax[1,1].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(f)", fontweight="bold", transform=ax[1,2].transAxes, fontsize=18)
    # plt.suptitle('Amplitude of the output power $P_p$ versus base excitation frequency $f_b$ at different $R_l$ and $\lambda_l$', fontsize=24)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.96, bottom=0.07, wspace=0.15, hspace=0.10)

    plt.savefig("fig_output_power_vs_fr_Rl_laml_all.pdf")
    plt.savefig("fig_output_power_vs_fr_Rl_laml_all.eps")
    plt.savefig("fig_output_power_vs_fr_Rl_laml_all.jpg", dpi=300)

    # plt.show()

def plot_vol_laml_list_vs_fr_Rl():
    fig, ax = plt.subplots(nrows = 2, ncols = 3, figsize=(24,12), sharex=True)
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_vplist00[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_vplist00[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_vplist00[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_vplist00[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_vplist00[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_vplist00[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[0,0].set_xscale('log')
    ax[0,0].set_yscale('log')
    ax[0,0].set_title('$\lambda_l$ = 0.0', fontsize=18)
    ax[0,0].legend(loc='lower right', ncol=2)
    # ax[0,0].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    ax[0,0].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)


    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_vplist02[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_vplist02[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_vplist02[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_vplist02[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_vplist02[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_vplist02[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[0,1].set_xscale('log')
    ax[0,1].set_yscale('log')
    ax[0,1].set_title('$\lambda_l$ = 0.2', fontsize=18)
    ax[0,1].legend(loc='lower right', ncol=2)
    # ax[0,1].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    # ax[0,1].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)


    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_vplist04[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_vplist04[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_vplist04[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_vplist04[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_vplist04[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_vplist04[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[0,2].set_xscale('log')
    ax[0,2].set_yscale('log')
    ax[0,2].set_title('$\lambda_l$ = 0.4', fontsize=18)
    ax[0,2].legend(loc='lower right', ncol=2)
    # ax[0,2].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    # ax[0,2].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)

    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_vplist06[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_vplist06[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_vplist06[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_vplist06[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_vplist06[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_vplist06[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[1,0].set_xscale('log')
    ax[1,0].set_yscale('log')
    ax[1,0].set_title('$\lambda_l$ = 0.6', fontsize=18)
    ax[1,0].legend(loc='lower right', ncol=2)
    ax[1,0].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    ax[1,0].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)


    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_vplist08[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_vplist08[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_vplist08[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_vplist08[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_vplist08[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_vplist08[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[1,1].set_xscale('log')
    ax[1,1].set_yscale('log')
    ax[1,1].set_title('$\lambda_l$ = 0.8', fontsize=18)
    ax[1,1].legend(loc='lower right', ncol=2)
    ax[1,1].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    # ax[1,1].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)

    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_vplist10[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_vplist10[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_vplist10[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_vplist10[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_vplist10[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_vplist10[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[1,2].set_xscale('log')
    ax[1,2].set_yscale('log')
    ax[1,2].set_title('$\lambda_l$ = 1.0', fontsize=18)
    ax[1,2].legend(loc='lower right', ncol=2)
    ax[1,2].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    # ax[1,2].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)

    # print(fr[0,200],fr[0,300],fr[0,325],fr[0,350],fr[0,375],fr[0,400])
    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=ax[0,0].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=ax[0,1].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=ax[0,2].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=ax[1,0].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=ax[1,1].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(f)", fontweight="bold", transform=ax[1,2].transAxes, fontsize=18)
    # plt.suptitle("Amplitude of the output voltage $\\tilde{V}_p$ versus load resistance $R_l$ at different $f_b$ and $\lambda_l$", fontsize=24)

    plt.subplots_adjust(left=0.05, right=0.98, top=0.96, bottom=0.07, wspace=0.15, hspace=0.10)
    plt.savefig("fig_vol_laml_list_vs_fr_Rl.pdf")
    plt.savefig("fig_vol_laml_list_vs_fr_Rl.eps")
    plt.savefig("fig_vol_laml_list_vs_fr_Rl.jpg",dpi=300)
    plt.show()

def plot_pow_laml_list_vs_fr_Rl():
    fig, ax = plt.subplots(nrows = 2, ncols = 3, figsize=(24,12), sharex=True)
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_pplist00[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_pplist00[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_pplist00[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_pplist00[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_pplist00[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[0,0].plot(Rl[:,0].reshape(-1,1),(am_pplist00[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[0,0].set_xscale('log')
    ax[0,0].set_yscale('log')
    ax[0,0].set_title('$\lambda_l$ = 0.0', fontsize=18)
    ax[0,0].legend(loc='lower right', ncol=2)
    # ax[0,0].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    ax[0,0].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)


    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_pplist02[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_pplist02[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_pplist02[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_pplist02[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_pplist02[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[0,1].plot(Rl[:,0].reshape(-1,1),(am_pplist02[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[0,1].set_xscale('log')
    ax[0,1].set_yscale('log')
    ax[0,1].set_title('$\lambda_l$ = 0.2', fontsize=18)
    ax[0,1].legend(loc='lower right', ncol=2)
    # ax[0,1].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    # ax[0,1].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)


    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_pplist04[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_pplist04[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_pplist04[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_pplist04[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_pplist04[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[0,2].plot(Rl[:,0].reshape(-1,1),(am_pplist04[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[0,2].set_xscale('log')
    ax[0,2].set_yscale('log')
    ax[0,2].set_title('$\lambda_l$ = 0.4', fontsize=18)
    ax[0,2].legend(loc='lower right', ncol=2)
    # ax[0,2].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    # ax[0,2].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)

    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_pplist06[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_pplist06[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_pplist06[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_pplist06[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_pplist06[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[1,0].plot(Rl[:,0].reshape(-1,1),(am_pplist06[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[1,0].set_xscale('log')
    ax[1,0].set_yscale('log')
    ax[1,0].set_title('$\lambda_l$ = 0.6', fontsize=18)
    ax[1,0].legend(loc='lower right', ncol=2)
    ax[1,0].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    ax[1,0].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)


    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_pplist08[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_pplist08[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_pplist08[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_pplist08[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_pplist08[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[1,1].plot(Rl[:,0].reshape(-1,1),(am_pplist08[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[1,1].set_xscale('log')
    ax[1,1].set_yscale('log')
    ax[1,1].set_title('$\lambda_l$ = 0.8', fontsize=18)
    ax[1,1].legend(loc='lower right', ncol=2)
    ax[1,1].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    # ax[1,1].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)

    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_pplist10[:,200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$f_b$=10 $Hz$')
    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_pplist10[:,300]/xib/wr[0,300]/wr[0,300]).T, 'g-.', label='$f_b$=31.62 $Hz$')
    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_pplist10[:,325]/xib/wr[0,325]/wr[0,325]).T, 'b--', label='$f_b$=42.17 $Hz$')
    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_pplist10[:,350]/xib/wr[0,350]/wr[0,350]).T, 'm-', label='$f_b$=56.23 $Hz$')
    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_pplist10[:,375]/xib/wr[0,375]/wr[0,375]).T, 'c-d', label='$f_b$=74.99 $Hz$')
    ax[1,2].plot(Rl[:,0].reshape(-1,1),(am_pplist10[:,400]/xib/wr[0,400]/wr[0,400]).T, 'k-o', label='$f_b$=100 $Hz$')
    ax[1,2].set_xscale('log')
    ax[1,2].set_yscale('log')
    ax[1,2].set_title('$\lambda_l$ = 1.0', fontsize=18)
    ax[1,2].legend(loc='lower right', ncol=2)
    ax[1,2].set_xlabel('Load resistance $R_l$ ($\Omega$)', fontsize=18)
    # ax[1,2].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)

    # print(fr[0,200],fr[0,300],fr[0,325],fr[0,350],fr[0,375],fr[0,400])
    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=ax[0,0].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=ax[0,1].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=ax[0,2].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=ax[1,0].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=ax[1,1].transAxes, fontsize=18)
    plt.text(0.02, 0.93, "(f)", fontweight="bold", transform=ax[1,2].transAxes, fontsize=18)
    # plt.suptitle("Amplitude of the output power $\\tilde{P}_p$ versus load resistance $R_l$ at different $f_b$ and $\lambda_l$", fontsize=24)

    plt.subplots_adjust(left=0.05, right=0.98, top=0.96, bottom=0.07, wspace=0.15, hspace=0.10)
    plt.savefig("fig_pow_laml_list_vs_fr_Rl.pdf")
    plt.savefig("fig_pow_laml_list_vs_fr_Rl.eps")
    plt.savefig("fig_pow_laml_list_vs_fr_Rl.jpg",dpi=300)
    plt.show()

def plot_vol_fr_sl_Rl_sl_vs_laml():
    fig, ax = plt.subplots(nrows = 2, ncols = 3, figsize=(24,12), sharex=True)

    am_vplist = np.array([am_vplist00, am_vplist01, am_vplist02, am_vplist03,
                 am_vplist04, am_vplist05, am_vplist06, am_vplist07,
                 am_vplist08, am_vplist09, am_vplist10])
    am_pplist = np.array([am_pplist00, am_pplist01, am_pplist02, am_pplist03,
                 am_pplist04, am_pplist05, am_pplist06, am_pplist07,
                 am_pplist08, am_pplist09, am_pplist10])
    laml_list = np.linspace(0.0, 1.0, 11)

    class ScalarFormatterForceFormat(mtick.ScalarFormatter):
        def _set_format(self,vmin,vmax):  # Override function that finds format to use.
            self.format = "%1.2f"  # Give format here
    
    yfmt = ScalarFormatterForceFormat()
    yfmt.set_powerlimits((0,0))

    # print(laml_list.shape)

    ax[0,0].plot(laml_list.reshape(-1,1),(am_vplist[:, 0, 0]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[0,0].plot(laml_list.reshape(-1,1),(am_vplist[:, 2, 0]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 100 $\Omega$')
    ax[0,0].plot(laml_list.reshape(-1,1),(am_vplist[:, 4, 0]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[0,0].plot(laml_list.reshape(-1,1),(am_vplist[:, 6, 0]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[0,0].yaxis.set_major_formatter(yfmt)
    ax[0,0].set_yscale('log')
    ax[0,0].set_ylim(1e-8,1e0)
    ax[0,0].set_title('$f_b$ = 1 $Hz$', fontsize=18)
    ax[0,0].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    # ax[0,0].legend(loc='upper left', ncol=2, fontsize=18)

    ax[0,1].plot(laml_list.reshape(-1,1),(am_vplist[:, 0, 100]/xib/wr[0,100]/wr[0,100]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[0,1].plot(laml_list.reshape(-1,1),(am_vplist[:, 2, 100]/xib/wr[0,100]/wr[0,100]).T, 'k-.s', label='$R_l$ = 100 $\Omega$')
    ax[0,1].plot(laml_list.reshape(-1,1),(am_vplist[:, 4, 100]/xib/wr[0,100]/wr[0,100]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[0,1].plot(laml_list.reshape(-1,1),(am_vplist[:, 6, 100]/xib/wr[0,100]/wr[0,100]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[0,1].yaxis.set_major_formatter(yfmt)
    ax[0,1].set_title('$f_b$ = 3.162 $Hz$', fontsize=18)
    ax[0,1].set_yscale('log')
    ax[0,1].set_ylim(1e-7,1e0)
    # ax[0,1].legend(loc='upper left', ncol=2, fontsize=18)

    ax[0,2].plot(laml_list.reshape(-1,1),(am_vplist[:, 0, 200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[0,2].plot(laml_list.reshape(-1,1),(am_vplist[:, 2, 200]/xib/wr[0,200]/wr[0,200]).T, 'k-.s', label='$R_l$ = 100 $\Omega$')
    ax[0,2].plot(laml_list.reshape(-1,1),(am_vplist[:, 4, 200]/xib/wr[0,200]/wr[0,200]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[0,2].plot(laml_list.reshape(-1,1),(am_vplist[:, 6, 200]/xib/wr[0,200]/wr[0,200]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[0,2].yaxis.set_major_formatter(yfmt)
    ax[0,2].set_title('$f_b$ = 10 $Hz$', fontsize=18)
    ax[0,2].set_yscale('log')
    ax[0,2].set_ylim(1e-7,1e1)
    # ax[0,2].legend(loc='upper left', ncol=2, fontsize=18)

    ax[1,0].plot(laml_list.reshape(-1,1),(am_vplist[:, 0, 300]/xib/wr[0,300]/wr[0,300]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[1,0].plot(laml_list.reshape(-1,1),(am_vplist[:, 2, 300]/xib/wr[0,300]/wr[0,300]).T, 'k-.s', label='$R_l$ = 100 $\Omega$')
    ax[1,0].plot(laml_list.reshape(-1,1),(am_vplist[:, 4, 300]/xib/wr[0,300]/wr[0,300]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[1,0].plot(laml_list.reshape(-1,1),(am_vplist[:, 6, 300]/xib/wr[0,300]/wr[0,300]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[1,0].yaxis.set_major_formatter(yfmt)
    ax[1,0].set_title('$f_b$ = 31.62 $Hz$', fontsize=18)
    ax[1,0].set_yscale('log')
    ax[1,0].set_xlabel('Length ratio $\\lambda_l$', fontsize=18)
    ax[1,0].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    ax[1,0].set_ylim(1e-6,1e1)
    # ax[1,0].legend(loc='upper left', ncol=2, fontsize=18)


    ax[1,1].plot(laml_list.reshape(-1,1),(am_vplist[:, 0, 325]/xib/wr[0,325]/wr[0,325]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[1,1].plot(laml_list.reshape(-1,1),(am_vplist[:, 2, 325]/xib/wr[0,325]/wr[0,325]).T, 'k-.s', label='$R_l$ = 10 $\Omega$')
    ax[1,1].plot(laml_list.reshape(-1,1),(am_vplist[:, 4, 325]/xib/wr[0,325]/wr[0,325]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[1,1].plot(laml_list.reshape(-1,1),(am_vplist[:, 6, 325]/xib/wr[0,325]/wr[0,325]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[1,1].yaxis.set_major_formatter(yfmt)
    ax[1,1].set_title('$f_b$ = 42.17 $Hz$', fontsize=18)
    ax[1,1].set_yscale('log')
    ax[1,1].set_xlabel('Length ratio $\\lambda_l$', fontsize=18)
    # ax[1,1].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    ax[1,1].set_ylim(1e-6,1e2)
    # ax[1,1].legend(loc='upper left', ncol=2, fontsize=18)
    

    ax[1,2].plot(laml_list.reshape(-1,1),(am_vplist[:, 0, 400]/xib/wr[0,400]/wr[0,400]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[1,2].plot(laml_list.reshape(-1,1),(am_vplist[:, 2, 400]/xib/wr[0,400]/wr[0,400]).T, 'k-.s', label='$R_l$ = 100 $\Omega$')
    ax[1,2].plot(laml_list.reshape(-1,1),(am_vplist[:, 4, 400]/xib/wr[0,400]/wr[0,400]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[1,2].plot(laml_list.reshape(-1,1),(am_vplist[:, 6, 400]/xib/wr[0,400]/wr[0,400]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[1,2].yaxis.set_major_formatter(yfmt)
    ax[1,2].set_title('$f_b$ = 100 $Hz$', fontsize=18)
    ax[1,2].set_xlabel('Length ratio $\\lambda_l$', fontsize=18)
    # ax[1,2].set_ylabel('Output voltage $|\\tilde{V}_p/(\\sigma^2 \\xi_b)|$ ($V \\cdot s^2 / m$)', fontsize=18)
    ax[1,2].set_yscale('log')
    ax[1,2].set_ylim(1e-6,1e0)
    # ax[1,2].legend(loc='upper left', ncol=2, fontsize=18)

    ax[0,0].legend(bbox_to_anchor=(0., 1.10, 3.3, .102), loc=3, ncol=4, mode="expand", borderaxespad=0, fontsize=24)
    # plt.suptitle('Amplitude of the output voltage $\\tilde{V}_p$ versus Length ratio $\\lambda_l$ at different $f_b$ and $R_l$', fontsize=24)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.08, wspace=0.15, hspace=0.17)
    plt.savefig("fig_vol_fr_sl_Rl_sl_vs_laml.pdf")
    plt.savefig("fig_vol_fr_sl_Rl_sl_vs_laml.eps")
    plt.savefig("fig_vol_fr_sl_Rl_sl_vs_laml.jpg",dpi=300)
    plt.show()

def plot_pow_fr_sl_Rl_sl_vs_laml():
    fig, ax = plt.subplots(nrows = 2, ncols = 3, figsize=(24,12), sharex=True)

    am_vplist = np.array([am_vplist00, am_vplist01, am_vplist02, am_vplist03,
                 am_vplist04, am_vplist05, am_vplist06, am_vplist07,
                 am_vplist08, am_vplist09, am_vplist10])
    am_pplist = np.array([am_pplist00, am_pplist01, am_pplist02, am_pplist03,
                 am_pplist04, am_pplist05, am_pplist06, am_pplist07,
                 am_pplist08, am_pplist09, am_pplist10])
    laml_list = np.linspace(0.0, 1.0, 11)

    class ScalarFormatterForceFormat(mtick.ScalarFormatter):
        def _set_format(self,vmin,vmax):  # Override function that finds format to use.
            self.format = "%1.2f"  # Give format here
    
    yfmt = ScalarFormatterForceFormat()
    yfmt.set_powerlimits((0,0))

    # print(laml_list.shape)

    ax[0,0].plot(laml_list.reshape(-1,1),(am_pplist[:, 0, 0]/xib/wr[0,0]/wr[0,0]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[0,0].plot(laml_list.reshape(-1,1),(am_pplist[:, 2, 0]/xib/wr[0,0]/wr[0,0]).T, 'k-.s', label='$R_l$ = 100 $\Omega$')
    ax[0,0].plot(laml_list.reshape(-1,1),(am_pplist[:, 4, 0]/xib/wr[0,0]/wr[0,0]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[0,0].plot(laml_list.reshape(-1,1),(am_pplist[:, 6, 0]/xib/wr[0,0]/wr[0,0]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[0,0].yaxis.set_major_formatter(yfmt)
    ax[0,0].set_yscale('log')
    # ax[0,0].set_ylim(1e-8,1e0)
    ax[0,0].set_title('$f_b$ = 1 $Hz$', fontsize=18)
    ax[0,0].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    # ax[0,0].legend(loc='upper left', ncol=2, fontsize=18)

    ax[0,1].plot(laml_list.reshape(-1,1),(am_pplist[:, 0, 100]/xib/wr[0,100]/wr[0,100]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[0,1].plot(laml_list.reshape(-1,1),(am_pplist[:, 2, 100]/xib/wr[0,100]/wr[0,100]).T, 'k-.s', label='$R_l$ = 100 $\Omega$')
    ax[0,1].plot(laml_list.reshape(-1,1),(am_pplist[:, 4, 100]/xib/wr[0,100]/wr[0,100]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[0,1].plot(laml_list.reshape(-1,1),(am_pplist[:, 6, 100]/xib/wr[0,100]/wr[0,100]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[0,1].yaxis.set_major_formatter(yfmt)
    ax[0,1].set_title('$f_b$ = 3.162 $Hz$', fontsize=18)
    ax[0,1].set_yscale('log')
    # ax[0,1].set_ylim(1e-7,1e0)
    # ax[0,1].legend(loc='upper left', ncol=2, fontsize=18)

    ax[0,2].plot(laml_list.reshape(-1,1),(am_pplist[:, 0, 200]/xib/wr[0,200]/wr[0,200]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[0,2].plot(laml_list.reshape(-1,1),(am_pplist[:, 2, 200]/xib/wr[0,200]/wr[0,200]).T, 'k-.s', label='$R_l$ = 100 $\Omega$')
    ax[0,2].plot(laml_list.reshape(-1,1),(am_pplist[:, 4, 200]/xib/wr[0,200]/wr[0,200]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[0,2].plot(laml_list.reshape(-1,1),(am_pplist[:, 6, 200]/xib/wr[0,200]/wr[0,200]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[0,2].yaxis.set_major_formatter(yfmt)
    ax[0,2].set_title('$f_b$ = 10 $Hz$', fontsize=18)
    ax[0,2].set_yscale('log')
    # ax[0,2].set_ylim(1e-7,1e1)
    # ax[0,2].legend(loc='upper left', ncol=2, fontsize=18)

    ax[1,0].plot(laml_list.reshape(-1,1),(am_pplist[:, 0, 300]/xib/wr[0,300]/wr[0,300]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[1,0].plot(laml_list.reshape(-1,1),(am_pplist[:, 2, 300]/xib/wr[0,300]/wr[0,300]).T, 'k-.s', label='$R_l$ = 100 $\Omega$')
    ax[1,0].plot(laml_list.reshape(-1,1),(am_pplist[:, 4, 300]/xib/wr[0,300]/wr[0,300]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[1,0].plot(laml_list.reshape(-1,1),(am_pplist[:, 6, 300]/xib/wr[0,300]/wr[0,300]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[1,0].yaxis.set_major_formatter(yfmt)
    ax[1,0].set_title('$f_b$ = 31.62 $Hz$', fontsize=18)
    ax[1,0].set_yscale('log')
    ax[1,0].set_xlabel('Length ratio $\\lambda_l$', fontsize=18)
    ax[1,0].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    # ax[1,0].set_ylim(1e-6,1e1)
    # ax[1,0].legend(loc='upper left', ncol=2, fontsize=18)


    ax[1,1].plot(laml_list.reshape(-1,1),(am_pplist[:, 0, 325]/xib/wr[0,325]/wr[0,325]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[1,1].plot(laml_list.reshape(-1,1),(am_pplist[:, 2, 325]/xib/wr[0,325]/wr[0,325]).T, 'k-.s', label='$R_l$ = 10 $\Omega$')
    ax[1,1].plot(laml_list.reshape(-1,1),(am_pplist[:, 4, 325]/xib/wr[0,325]/wr[0,325]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[1,1].plot(laml_list.reshape(-1,1),(am_pplist[:, 6, 325]/xib/wr[0,325]/wr[0,325]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[1,1].yaxis.set_major_formatter(yfmt)
    ax[1,1].set_title('$f_b$ = 42.17 $Hz$', fontsize=18)
    ax[1,1].set_yscale('log')
    ax[1,1].set_xlabel('Length ratio $\\lambda_l$', fontsize=18)
    # ax[1,1].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    # ax[1,1].set_ylim(1e-6,1e2)
    # ax[1,1].legend(loc='upper left', ncol=2, fontsize=18)
    

    ax[1,2].plot(laml_list.reshape(-1,1),(am_pplist[:, 0, 400]/xib/wr[0,400]/wr[0,400]).T, 'r-*', label='$R_l$ = 1 $\Omega$')
    ax[1,2].plot(laml_list.reshape(-1,1),(am_pplist[:, 2, 400]/xib/wr[0,400]/wr[0,400]).T, 'k-.s', label='$R_l$ = 100 $\Omega$')
    ax[1,2].plot(laml_list.reshape(-1,1),(am_pplist[:, 4, 400]/xib/wr[0,400]/wr[0,400]).T, 'm--d', label='$R_l$ = 10 k$\Omega$')
    ax[1,2].plot(laml_list.reshape(-1,1),(am_pplist[:, 6, 400]/xib/wr[0,400]/wr[0,400]).T, 'b-o', label='$R_l$ = 1 M$\Omega$')
    ax[1,2].yaxis.set_major_formatter(yfmt)
    ax[1,2].set_title('$f_b$ = 100 $Hz$', fontsize=18)
    ax[1,2].set_xlabel('Length ratio $\\lambda_l$', fontsize=18)
    # ax[1,2].set_ylabel('Output power $|\\tilde{P}_p/(\\sigma^2 \\xi_b)^2|$ ($W \\cdot s^4 / m^2$)', fontsize=18)
    ax[1,2].set_yscale('log')
    # ax[1,2].set_ylim(1e-6,1e0)
    # ax[1,2].legend(loc='upper left', ncol=2, fontsize=18)

    ax[0,0].legend(bbox_to_anchor=(0., 1.10, 3.3, .102), loc=3, ncol=4, mode="expand", borderaxespad=0, fontsize=24)
    # plt.suptitle('Amplitude of the output voltage $\\tilde{V}_p$ versus Length ratio $\\lambda_l$ at different $f_b$ and $R_l$', fontsize=24)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.08, wspace=0.15, hspace=0.17)
    plt.savefig("fig_pow_fr_sl_Rl_sl_vs_laml.pdf")
    plt.savefig("fig_pow_fr_sl_Rl_sl_vs_laml.eps")
    plt.savefig("fig_pow_fr_sl_Rl_sl_vs_laml.jpg",dpi=300)
    # plt.show()

if __name__ == '__main__':
    # plot_vol_laml_vs_fr_Rl()
    # plot_pow_laml_vs_fr_Rl()
    # plot_vol_laml_list_vs_fr_Rl()
    # plot_pow_laml_list_vs_fr_Rl()
    plot_vol_fr_sl_Rl_sl_vs_laml()
    plot_pow_fr_sl_Rl_sl_vs_laml()