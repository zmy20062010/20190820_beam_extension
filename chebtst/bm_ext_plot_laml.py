from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from cycler import cycler
import matplotlib.ticker as mtick


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

fr        = result01['fr'];
Rl        = result01['Rl'];
xib       = result01['xib'];

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
    # fig, ax = plt.subplots()
    # fig, (ax0, ax1) = plt.subplots(nrows=2, constrained_layout=True)
    fig01, ((ax11, ax12), (ax13, ax21), (ax22, ax23)) = plt.subplots(ncols = 2, nrows = 3, figsize=(18,24), sharex=True)
    # fig01 = plt.figure(1, figsize=(12,8))
    # ax01 = fig01.add_axes([0.1, 0.1, 0.6, 0.75])


    ax11.plot(fr[0,:],am_vplist00[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax11.plot(fr[0,:],am_vplist00[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax11.plot(fr[0,:],am_vplist00[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax11.plot(fr[0,:],am_vplist00[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax11.plot(fr[0,:],am_vplist00[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax11.plot(fr[0,:],am_vplist00[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax11.plot(fr[0,:],am_vplist00[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax11.plot(fr[0,:],am_vplist00[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    # To the value of Rl being 1 Mohm, there is no obvious difference in terms of the 
    # eigenfrequency and output voltage
    ax11.set_title('$\lambda_l$=0.0')
    ax11.set_xlim(1,100)
    ax11.set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax11.set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax11.legend(loc='lower right', ncol=4)


    ax12.plot(fr[0,:],am_vplist02[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax12.plot(fr[0,:],am_vplist02[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax12.plot(fr[0,:],am_vplist02[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax12.plot(fr[0,:],am_vplist02[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax12.plot(fr[0,:],am_vplist02[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax12.plot(fr[0,:],am_vplist02[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax12.plot(fr[0,:],am_vplist02[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax12.plot(fr[0,:],am_vplist02[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    ax12.set_title('$\lambda_l$=0.2')
    ax12.set_xlim(1,100)
    ax12.set_yscale('log')
    # ax12.set_xlabel('Base excitation frequency $fr$')
    # ax12.set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax12.legend(loc='lower right',ncol=4)


    ax13.plot(fr[0,:],am_vplist04[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax13.plot(fr[0,:],am_vplist04[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax13.plot(fr[0,:],am_vplist04[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax13.plot(fr[0,:],am_vplist04[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax13.plot(fr[0,:],am_vplist04[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax13.plot(fr[0,:],am_vplist04[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax13.plot(fr[0,:],am_vplist04[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax13.plot(fr[0,:],am_vplist04[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    ax13.set_title('$\lambda_l$=0.4')
    ax13.set_xlim(1,100)
    ax13.set_yscale('log')
    # ax13.set_xlabel('Base excitation frequency $fr$')
    ax13.set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax13.legend(loc='lower right',ncol=4)


    ax21.plot(fr[0,:],am_vplist06[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax21.plot(fr[0,:],am_vplist06[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax21.plot(fr[0,:],am_vplist06[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax21.plot(fr[0,:],am_vplist06[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax21.plot(fr[0,:],am_vplist06[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax21.plot(fr[0,:],am_vplist06[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax21.plot(fr[0,:],am_vplist06[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax21.plot(fr[0,:],am_vplist06[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    ax21.set_title('$\lambda_l$=0.6')
    ax21.set_xlim(1,100)
    ax21.set_yscale('log')
    # ax21.set_xlabel('Base excitation frequency $fr$ ($Hz$)')
    # ax21.set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax21.legend(loc='lower right',ncol=4)


    ax22.plot(fr[0,:],am_vplist08[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax22.plot(fr[0,:],am_vplist08[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax22.plot(fr[0,:],am_vplist08[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax22.plot(fr[0,:],am_vplist08[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax22.plot(fr[0,:],am_vplist08[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax22.plot(fr[0,:],am_vplist08[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax22.plot(fr[0,:],am_vplist08[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax22.plot(fr[0,:],am_vplist08[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    ax22.set_title('$\lambda_l$=0.8')
    ax22.set_xlim(1,100)
    ax22.set_yscale('log')
    ax22.set_xlabel('Base excitation frequency $fr$ ($Hz$)')
    ax22.set_ylabel('Amplitude of the output voltage $V_p$')
    ax22.legend(loc='lower right',ncol=4)


    ax23.plot(fr[0,:],am_vplist10[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax23.plot(fr[0,:],am_vplist10[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax23.plot(fr[0,:],am_vplist10[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax23.plot(fr[0,:],am_vplist10[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax23.plot(fr[0,:],am_vplist10[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax23.plot(fr[0,:],am_vplist10[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax23.plot(fr[0,:],am_vplist10[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax23.plot(fr[0,:],am_vplist00[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    ax23.set_title('$\lambda_l$=1.0')
    ax23.set_xlim(1,100)
    ax23.set_yscale('log')
    ax23.set_xlabel('Base excitation frequency $fr$ ($Hz$)')
    # ax23.set_ylabel('Amplitude of the output voltage $V_p$')
    ax23.legend(loc='lower right',ncol=4)


    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=ax11.transAxes)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=ax12.transAxes)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=ax13.transAxes)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=ax21.transAxes)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=ax22.transAxes)
    plt.text(0.02, 0.93, "(f)", fontweight="bold", transform=ax23.transAxes)
    plt.suptitle('Amplitude of the output voltage $V_p$ versus base excitation frequency $fr$ at different $R_l$ and $\lambda_l$',fontsize=18)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.08, hspace=0.17)
    # plt.tight_layout(w_pad=0.1, h_pad=0.01)

    plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.pdf")
    plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.eps")
    plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.jpg",dpi=300)
    plt.show()

def plot_pow_laml_vs_fr_Rl():
    # fig, ax = plt.subplots()
    # fig, (ax0, ax1) = plt.subplots(nrows=2, constrained_layout=True)
    fig01, ((ax11, ax12), (ax13, ax21), (ax22, ax23)) = plt.subplots(ncols = 2, nrows = 3, figsize=(18,24), sharex=True)
    # fig01 = plt.figure(1, figsize=(12,8))
    # ax01 = fig01.add_axes([0.1, 0.1, 0.6, 0.75])


    ax11.plot(fr[0,:],am_pplist00[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax11.plot(fr[0,:],am_pplist00[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax11.plot(fr[0,:],am_pplist00[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax11.plot(fr[0,:],am_pplist00[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax11.plot(fr[0,:],am_pplist00[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax11.plot(fr[0,:],am_pplist00[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax11.plot(fr[0,:],am_pplist00[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax11.plot(fr[0,:],am_pplist00[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    # To the value of Rl being 1 Mohm, there is no obvious difference in terms of the 
    # eigenfrequency and output voltage
    ax11.set_title('$\lambda_l$=0.0')
    ax11.set_xlim(1,100)
    ax11.set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax11.set_ylabel('Amplitude of the output power $P_p$ (W)')
    ax11.legend(loc='lower right',ncol=4)


    ax12.plot(fr[0,:],am_pplist02[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax12.plot(fr[0,:],am_pplist02[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax12.plot(fr[0,:],am_pplist02[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax12.plot(fr[0,:],am_pplist02[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax12.plot(fr[0,:],am_pplist02[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax12.plot(fr[0,:],am_pplist02[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax12.plot(fr[0,:],am_pplist02[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax12.plot(fr[0,:],am_pplist02[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    ax12.set_title('$\lambda_l$=0.2')
    ax12.set_xlim(1,100)
    ax12.set_yscale('log')
    # ax12.set_xlabel('Base excitation frequency $fr$')
    # ax12.set_ylabel('Amplitude of the output power $P_p$ (W)')
    ax12.legend(loc='lower right',ncol=4)


    ax13.plot(fr[0,:],am_pplist04[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax13.plot(fr[0,:],am_pplist04[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax13.plot(fr[0,:],am_pplist04[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax13.plot(fr[0,:],am_pplist04[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax13.plot(fr[0,:],am_pplist04[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax13.plot(fr[0,:],am_pplist04[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax13.plot(fr[0,:],am_pplist04[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax13.plot(fr[0,:],am_pplist04[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    ax13.set_title('$\lambda_l$=0.4')
    ax13.set_xlim(1,100)
    ax13.set_yscale('log')
    # ax13.set_xlabel('Base excitation frequency $fr$')
    ax13.set_ylabel('Amplitude of the output power $P_p$ (W)')
    ax13.legend(loc='lower right',ncol=4)


    ax21.plot(fr[0,:],am_pplist06[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax21.plot(fr[0,:],am_pplist06[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax21.plot(fr[0,:],am_pplist06[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax21.plot(fr[0,:],am_pplist06[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax21.plot(fr[0,:],am_pplist06[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax21.plot(fr[0,:],am_pplist06[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax21.plot(fr[0,:],am_pplist06[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax21.plot(fr[0,:],am_pplist06[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    ax21.set_title('$\lambda_l$=0.6')
    ax21.set_xlim(1,100)
    ax21.set_yscale('log')
    # ax21.set_xlabel('Base excitation frequency $fr$ ($Hz$)')
    # ax21.set_ylabel('Amplitude of the output power $P_p$ (W)')
    ax21.legend(loc='lower right',ncol=4)


    ax22.plot(fr[0,:],am_pplist08[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax22.plot(fr[0,:],am_pplist08[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax22.plot(fr[0,:],am_pplist08[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax22.plot(fr[0,:],am_pplist08[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax22.plot(fr[0,:],am_pplist08[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax22.plot(fr[0,:],am_pplist08[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax22.plot(fr[0,:],am_pplist08[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax22.plot(fr[0,:],am_pplist08[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    ax22.set_title('$\lambda_l$=0.8')
    ax22.set_xlim(1,100)
    ax22.set_yscale('log')
    ax22.set_xlabel('Base excitation frequency $fr$ ($Hz$)')
    ax22.set_ylabel('Amplitude of the output power $P_p$ (W)')
    ax22.legend(loc='lower right',ncol=4)


    ax23.plot(fr[0,:],am_pplist10[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    # ax23.plot(fr[0,:],am_pplist10[1,:],'g', label= '$R_l$ = 10 $\Omega$')
    ax23.plot(fr[0,:],am_pplist10[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    # ax23.plot(fr[0,:],am_pplist10[3,:],'c', label= '$R_l$ = 1 k$\Omega$')
    ax23.plot(fr[0,:],am_pplist10[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    # ax23.plot(fr[0,:],am_pplist10[5,:],'k', label= '$R_l$ = 100 k$\Omega$')
    ax23.plot(fr[0,:],am_pplist10[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    # ax23.plot(fr[0,:],am_pplist00[7,:],'y--', label= '$R_l$ = 10 M$\Omega$')
    ax23.set_title('$\lambda_l$=1.0')
    ax23.set_xlim(1,100)
    ax23.set_yscale('log')
    ax23.set_xlabel('Base excitation frequency $fr$ ($Hz$)')
    # ax23.set_ylabel('Amplitude of the output power $P_p$ (W)')
    ax23.legend(loc='lower right',ncol=4)


    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=ax11.transAxes)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=ax12.transAxes)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=ax13.transAxes)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=ax21.transAxes)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=ax22.transAxes)
    plt.text(0.02, 0.93, "(f)", fontweight="bold", transform=ax23.transAxes)
    plt.suptitle('Amplitude of the output power $P_p$ versus base excitation frequency $fr$ at different $R_l$ and $\lambda_l$',fontsize=18)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.08, hspace=0.17)
    # plt.tight_layout(w_pad=0.1, h_pad=0.01)

    plt.savefig("fig_output_power_vs_fr_Rl_laml_all.pdf")
    plt.savefig("fig_output_power_vs_fr_Rl_laml_all.eps")
    plt.savefig("fig_output_power_vs_fr_Rl_laml_all.jpg",dpi=300)
    plt.show()

def plot_perf_laml_0p3_0p4_vs_fr_Rl():
    fig, axes = plt.subplots(ncols = 3, nrows = 2, figsize=(24,18), sharex=True)
    axes[0,0].plot(Rl[:,0],am_vplist00[:,200], 'r-*', label='fr=10')
    axes[0,0].plot(Rl[:,0],am_vplist00[:,300], 'g-.', label='fr=31.62')
    axes[0,0].plot(Rl[:,0],am_vplist00[:,325], 'b--', label='fr=42.17')
    axes[0,0].plot(Rl[:,0],am_vplist00[:,350], 'm-', label='fr=56.23')
    axes[0,0].plot(Rl[:,0],am_vplist00[:,375], 'c-d', label='fr=74.99')
    axes[0,0].plot(Rl[:,0],am_vplist00[:,400], 'k-o', label='fr=100')
    axes[0,0].set_xscale('log')
    axes[0,0].set_yscale('log')
    axes[0,0].set_title('$\lambda_l$ = 0.0')
    axes[0,0].legend(loc='lower right', ncol=2)
    # axes[0,0].set_xlabel('Externally connected resistance $R_l$ ($\Omega$)')
    axes[0,0].set_ylabel('Amplitude of the output voltage $V_p$ (V)')

    axes[1,0].plot(Rl[:,0],am_pplist00[:,200], 'r-*', label='fr=10')
    axes[1,0].plot(Rl[:,0],am_pplist00[:,300], 'g-.', label='fr=31.62')
    axes[1,0].plot(Rl[:,0],am_pplist00[:,325], 'b--', label='fr=42.17')
    axes[1,0].plot(Rl[:,0],am_pplist00[:,350], 'm-', label='fr=56.23')
    axes[1,0].plot(Rl[:,0],am_pplist00[:,375], 'c-d', label='fr=74.99')
    axes[1,0].plot(Rl[:,0],am_pplist00[:,400], 'k-o', label='fr=100')
    axes[1,0].set_xscale('log')
    axes[1,0].set_yscale('log')
    axes[1,0].set_title('$\lambda_l$ = 0.0')
    axes[1,0].legend(loc='lower right', ncol=2)
    axes[1,0].set_xlabel('Externally connected resistance $R_l$ ($\Omega$)')
    axes[1,0].set_ylabel('Amplitude of the output power $P_p$ (W)')


    axes[0,1].plot(Rl[:,0],am_vplist03[:,200], 'r-*', label='fr=10')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,300], 'g-.', label='fr=31.62')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,325], 'b--', label='fr=42.17')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,350], 'm-', label='fr=56.23')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,375], 'c-d', label='fr=74.99')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,400], 'k-o', label='fr=100')
    axes[0,1].set_xscale('log')
    axes[0,1].set_yscale('log')
    axes[0,1].set_title('$\lambda_l$ = 0.3')
    axes[0,1].legend(loc='lower right', ncol=2)
    # axes[0,1].set_xlabel('Externally connected resistance $R_l$ ($\Omega$)')
    # axes[0,1].set_ylabel('Amplitude of the output voltage $V_p$ (W)')

    axes[1,1].plot(Rl[:,0],am_pplist03[:,200], 'r-*', label='fr=10')
    axes[1,1].plot(Rl[:,0],am_pplist03[:,300], 'g-.', label='fr=31.62')
    axes[1,1].plot(Rl[:,0],am_pplist03[:,325], 'b--', label='fr=42.17')
    axes[1,1].plot(Rl[:,0],am_pplist03[:,350], 'm-', label='fr=56.23')
    axes[1,1].plot(Rl[:,0],am_pplist03[:,375], 'c-d', label='fr=74.99')
    axes[1,1].plot(Rl[:,0],am_pplist03[:,400], 'k-o', label='fr=100')
    axes[1,1].set_xscale('log')
    axes[1,1].set_yscale('log')
    axes[1,1].set_title('$\lambda_l$ = 0.3')
    axes[1,1].legend(loc='lower right', ncol=2)
    axes[1,1].set_xlabel('Externally connected resistance $R_l$ ($\Omega$)')
    # axes[1,1].set_ylabel('Amplitude of the output power $P_p$ (W)')


    axes[0,2].plot(Rl[:,0],am_vplist04[:,200], 'r-*', label='fr=10')
    axes[0,2].plot(Rl[:,0],am_vplist04[:,300], 'g-.', label='fr=31.62')
    axes[0,2].plot(Rl[:,0],am_vplist04[:,325], 'b--', label='fr=42.17')
    axes[0,2].plot(Rl[:,0],am_vplist04[:,350], 'm-', label='fr=56.23')
    axes[0,2].plot(Rl[:,0],am_vplist04[:,375], 'c-d', label='fr=74.99')
    axes[0,2].plot(Rl[:,0],am_vplist04[:,400], 'k-o', label='fr=100')
    axes[0,2].set_xscale('log')
    axes[0,2].set_yscale('log')
    axes[0,2].set_title('$\lambda_l$ = 0.4')
    axes[0,2].legend(loc='lower right', ncol=2)
    # axes[0,2].set_xlabel('Externally connected resistance $R_l$ ($\Omega$)')
    # axes[0,2].set_ylabel('Amplitude of the output voltage $V_p$ (W)')

    axes[1,2].plot(Rl[:,0],am_pplist04[:,200], 'r-*', label='fr=10')
    axes[1,2].plot(Rl[:,0],am_pplist04[:,300], 'g-.', label='fr=31.62')
    axes[1,2].plot(Rl[:,0],am_pplist04[:,325], 'b--', label='fr=42.17')
    axes[1,2].plot(Rl[:,0],am_pplist04[:,350], 'm-', label='fr=56.23')
    axes[1,2].plot(Rl[:,0],am_pplist04[:,375], 'c-d', label='fr=74.99')
    axes[1,2].plot(Rl[:,0],am_pplist04[:,400], 'k-o', label='fr=100')
    axes[1,2].set_xscale('log')
    axes[1,2].set_yscale('log')
    axes[1,2].set_title('$\lambda_l$ = 0.4')
    axes[1,2].legend(loc='lower right', ncol=2)
    axes[1,2].set_xlabel('Externally connected resistance $R_l$ ($\Omega$)')
    # axes[1,2].set_ylabel('Amplitude of the output power $P_p$ (W)')

    # print(fr[0,200],fr[0,300],fr[0,325],fr[0,350],fr[0,375],fr[0,400])
    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=axes[0,0].transAxes)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=axes[0,1].transAxes)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=axes[0,2].transAxes)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=axes[1,0].transAxes)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=axes[1,1].transAxes)
    plt.text(0.02, 0.93, "(f)", fontweight="bold", transform=axes[1,2].transAxes)
    plt.suptitle("Amplitude of the output power $P_p$  and voltage $V_p$ versus externally connected resistance $R_l$ at different $fr$ and $\lambda_l$",fontsize=18)

    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.15, hspace=0.17)
    plt.savefig("fig_perf_laml_0p3_0p4_vs_fr_Rl.pdf")
    plt.savefig("fig_perf_laml_0p3_0p4_vs_fr_Rl.eps")
    plt.savefig("fig_perf_laml_0p3_0p4_vs_fr_Rl.jpg",dpi=300)
    plt.show()


def plot_vol_fr_sl_Rl_sl_vs_laml():
    fig, axes = plt.subplots(ncols = 4, nrows = 4, figsize=(18,24), sharex=True)


    am_vplist = np.array([am_vplist00, am_vplist01, am_vplist02, am_vplist03,
                 am_vplist04, am_vplist05, am_vplist06, am_vplist07,
                 am_vplist08, am_vplist09, am_vplist10])
    am_pplist = np.array([am_pplist00, am_pplist01, am_pplist02, am_pplist03,
                 am_pplist04, am_pplist05, am_pplist06, am_pplist07,
                 am_pplist08, am_pplist09, am_pplist10])
    laml_list = np.linspace(0.0, 1.0, 11)
    # print(am_vplist.shape)
    # print(am_pplist.shape)
    # print(laml_list)
    class ScalarFormatterForceFormat(mtick.ScalarFormatter):
        def _set_format(self,vmin,vmax):  # Override function that finds format to use.
            self.format = "%1.2f"  # Give format here
    
    yfmt = ScalarFormatterForceFormat()
    yfmt.set_powerlimits((0,0))

    # ticklabel_format(self, *, axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)

    # axes[0,0].plot(laml_list,am_vplist[:, 0, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 1 $\Omega$')
    # axes[0,0].yaxis.set_major_formatter(yfmt)
    # # axes[0,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[0,1].plot(laml_list,am_vplist[:, 2, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 100 $\Omega$')
    # axes[0,1].yaxis.set_major_formatter(yfmt)
    # # axes[0,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[0,2].plot(laml_list,am_vplist[:, 4, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 10 k$\Omega$')
    # axes[0,2].yaxis.set_major_formatter(yfmt)
    # # axes[0,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[0,3].plot(laml_list,am_vplist[:, 6, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 1 M$\Omega$')
    # axes[0,3].yaxis.set_major_formatter(yfmt)
    # # axes[0,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))


    # axes[1,0].plot(laml_list,am_vplist[:, 0, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 1 $\Omega$')
    # axes[1,0].yaxis.set_major_formatter(yfmt)
    # # axes[1,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[1,1].plot(laml_list,am_vplist[:, 2, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 100 $\Omega$')
    # axes[1,1].yaxis.set_major_formatter(yfmt)
    # # axes[1,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[1,2].plot(laml_list,am_vplist[:, 4, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 10 $\Omega$')
    # axes[1,2].yaxis.set_major_formatter(yfmt)
    # # axes[1,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[1,3].plot(laml_list,am_vplist[:, 6, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 1 M$\Omega$')
    # axes[1,3].yaxis.set_major_formatter(yfmt)
    # # axes[1,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[0,0].plot(laml_list,am_vplist[:, 0, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 1 $\Omega$')
    axes[0,0].yaxis.set_major_formatter(yfmt)
    # axes[0,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[0,1].plot(laml_list,am_vplist[:, 2, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 100 $\Omega$')
    axes[0,1].yaxis.set_major_formatter(yfmt)
    # axes[0,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[0,2].plot(laml_list,am_vplist[:, 4, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[0,2].yaxis.set_major_formatter(yfmt)
    # axes[0,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[0,3].plot(laml_list,am_vplist[:, 6, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[0,3].yaxis.set_major_formatter(yfmt)
    # axes[0,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[1,0].plot(laml_list,am_vplist[:, 0, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 1 $\Omega$')
    axes[1,0].yaxis.set_major_formatter(yfmt)
    # axes[1,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,1].plot(laml_list,am_vplist[:, 2, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 100 $\Omega$')
    axes[1,1].yaxis.set_major_formatter(yfmt)
    # axes[1,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,2].plot(laml_list,am_vplist[:, 4, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[1,2].yaxis.set_major_formatter(yfmt)
    # axes[1,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,3].plot(laml_list,am_vplist[:, 6, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[1,3].yaxis.set_major_formatter(yfmt)
    # axes[1,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[2,0].plot(laml_list,am_vplist[:, 0, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 1 $\Omega$')
    axes[2,0].yaxis.set_major_formatter(yfmt)
    # axes[2,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,1].plot(laml_list,am_vplist[:, 2, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 10 $\Omega$')
    axes[2,1].yaxis.set_major_formatter(yfmt)
    # axes[2,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,2].plot(laml_list,am_vplist[:, 4, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[2,2].yaxis.set_major_formatter(yfmt)
    # axes[2,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,3].plot(laml_list,am_vplist[:, 6, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[2,3].yaxis.set_major_formatter(yfmt)
    # axes[2,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[3,0].plot(laml_list,am_vplist[:, 0, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 1 $\Omega$')
    axes[3,0].yaxis.set_major_formatter(yfmt)
    # axes[3,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,1].plot(laml_list,am_vplist[:, 2, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 100 $\Omega$')
    axes[3,1].yaxis.set_major_formatter(yfmt)
    # axes[3,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,2].plot(laml_list,am_vplist[:, 4, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[3,2].yaxis.set_major_formatter(yfmt)
    # axes[3,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,3].plot(laml_list,am_vplist[:, 6, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[3,3].yaxis.set_major_formatter(yfmt)
    # axes[3,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    for i in range(4):
        for j in range(4):
            axes[i,j].legend(loc='best')


    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.15, hspace=0.17)
    plt.savefig("fig_vol_fr_sl_Rl_sl_vs_laml.pdf")
    plt.savefig("fig_vol_fr_sl_Rl_sl_vs_laml.eps")
    plt.savefig("fig_vol_fr_sl_Rl_sl_vs_laml.jpg",dpi=300)
    plt.show()

def plot_pow_fr_sl_Rl_sl_vs_laml():
    fig, axes = plt.subplots(ncols = 4, nrows = 4, figsize=(18,24), sharex=True)


    am_pplist = np.array([am_pplist00, am_pplist01, am_pplist02, am_pplist03,
                 am_pplist04, am_pplist05, am_pplist06, am_pplist07,
                 am_pplist08, am_pplist09, am_pplist10])
    am_pplist = np.array([am_pplist00, am_pplist01, am_pplist02, am_pplist03,
                 am_pplist04, am_pplist05, am_pplist06, am_pplist07,
                 am_pplist08, am_pplist09, am_pplist10])
    laml_list = np.linspace(0.0, 1.0, 11)
    # print(am_pplist.shape)
    # print(am_pplist.shape)
    # print(laml_list)
    class ScalarFormatterForceFormat(mtick.ScalarFormatter):
        def _set_format(self,vmin,vmax):  # Override function that finds format to use.
            self.format = "%1.2f"  # Give format here
    
    yfmt = ScalarFormatterForceFormat()
    yfmt.set_powerlimits((0,0))

    # ticklabel_format(self, *, axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)

    # axes[0,0].plot(laml_list,am_pplist[:, 0, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 1 $\Omega$')
    # axes[0,0].yaxis.set_major_formatter(yfmt)
    # # axes[0,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[0,1].plot(laml_list,am_pplist[:, 2, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 100 $\Omega$')
    # axes[0,1].yaxis.set_major_formatter(yfmt)
    # # axes[0,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[0,2].plot(laml_list,am_pplist[:, 4, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 10 k$\Omega$')
    # axes[0,2].yaxis.set_major_formatter(yfmt)
    # # axes[0,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[0,3].plot(laml_list,am_pplist[:, 6, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 1 M$\Omega$')
    # axes[0,3].yaxis.set_major_formatter(yfmt)
    # # axes[0,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))


    # axes[1,0].plot(laml_list,am_pplist[:, 0, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 1 $\Omega$')
    # axes[1,0].yaxis.set_major_formatter(yfmt)
    # # axes[1,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[1,1].plot(laml_list,am_pplist[:, 2, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 100 $\Omega$')
    # axes[1,1].yaxis.set_major_formatter(yfmt)
    # # axes[1,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[1,2].plot(laml_list,am_pplist[:, 4, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 10 $\Omega$')
    # axes[1,2].yaxis.set_major_formatter(yfmt)
    # # axes[1,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    # axes[1,3].plot(laml_list,am_pplist[:, 6, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 1 M$\Omega$')
    # axes[1,3].yaxis.set_major_formatter(yfmt)
    # # axes[1,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[0,0].plot(laml_list,am_pplist[:, 0, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 1 $\Omega$')
    axes[0,0].yaxis.set_major_formatter(yfmt)
    # axes[0,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[0,1].plot(laml_list,am_pplist[:, 2, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 100 $\Omega$')
    axes[0,1].yaxis.set_major_formatter(yfmt)
    # axes[0,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[0,2].plot(laml_list,am_pplist[:, 4, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[0,2].yaxis.set_major_formatter(yfmt)
    # axes[0,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[0,3].plot(laml_list,am_pplist[:, 6, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[0,3].yaxis.set_major_formatter(yfmt)
    # axes[0,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[1,0].plot(laml_list,am_pplist[:, 0, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 1 $\Omega$')
    axes[1,0].yaxis.set_major_formatter(yfmt)
    # axes[1,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,1].plot(laml_list,am_pplist[:, 2, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 100 $\Omega$')
    axes[1,1].yaxis.set_major_formatter(yfmt)
    # axes[1,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,2].plot(laml_list,am_pplist[:, 4, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[1,2].yaxis.set_major_formatter(yfmt)
    # axes[1,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,3].plot(laml_list,am_pplist[:, 6, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[1,3].yaxis.set_major_formatter(yfmt)
    # axes[1,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[2,0].plot(laml_list,am_pplist[:, 0, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 1 $\Omega$')
    axes[2,0].yaxis.set_major_formatter(yfmt)
    # axes[2,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,1].plot(laml_list,am_pplist[:, 2, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 10 $\Omega$')
    axes[2,1].yaxis.set_major_formatter(yfmt)
    # axes[2,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,2].plot(laml_list,am_pplist[:, 4, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[2,2].yaxis.set_major_formatter(yfmt)
    # axes[2,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,3].plot(laml_list,am_pplist[:, 6, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[2,3].yaxis.set_major_formatter(yfmt)
    # axes[2,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[3,0].plot(laml_list,am_pplist[:, 0, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 1 $\Omega$')
    axes[3,0].yaxis.set_major_formatter(yfmt)
    # axes[3,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,1].plot(laml_list,am_pplist[:, 2, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 100 $\Omega$')
    axes[3,1].yaxis.set_major_formatter(yfmt)
    # axes[3,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,2].plot(laml_list,am_pplist[:, 4, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[3,2].yaxis.set_major_formatter(yfmt)
    # axes[3,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,3].plot(laml_list,am_pplist[:, 6, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[3,3].yaxis.set_major_formatter(yfmt)
    # axes[3,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    for i in range(4):
        for j in range(4):
            axes[i,j].legend(loc='best')


    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.15, hspace=0.17)
    plt.savefig("fig_pow_fr_sl_Rl_sl_vs_laml.pdf")
    plt.savefig("fig_pow_fr_sl_Rl_sl_vs_laml.eps")
    plt.savefig("fig_pow_fr_sl_Rl_sl_vs_laml.jpg",dpi=300)
    plt.show()

if __name__ == '__main__':
    # plot_vol_laml_vs_fr_Rl()
    # plot_pow_laml_vs_fr_Rl()
    plot_perf_laml_0p3_0p4_vs_fr_Rl()
    # plot_vol_fr_sl_Rl_sl_vs_laml()
    # plot_pow_fr_sl_Rl_sl_vs_laml()