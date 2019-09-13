from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.ticker as mtick

result00 = sio.loadmat('bm_ext_base_lamB_Ye_0p01e9.mat'); 
vplist00  = result00['Vplist'];
pplist00  = result00['Pplist'];
result01 = sio.loadmat('bm_ext_base_lamB_Ye_0p02e9.mat'); 
vplist01  = result01['Vplist'];
pplist01  = result01['Pplist'];
result02 = sio.loadmat('bm_ext_base_lamB_Ye_0p03e9.mat'); 
vplist02  = result02['Vplist'];
pplist02  = result02['Pplist'];
result03 = sio.loadmat('bm_ext_base_lamB_Ye_0p04e9.mat'); 
vplist03  = result03['Vplist'];
pplist03  = result03['Pplist'];
result04 = sio.loadmat('bm_ext_base_lamB_Ye_0p05e9.mat'); 
vplist04  = result04['Vplist'];
pplist04  = result04['Pplist'];
result05 = sio.loadmat('bm_ext_base_lamB_Ye_0p06e9.mat'); 
vplist05  = result05['Vplist'];
pplist05  = result05['Pplist'];
result06 = sio.loadmat('bm_ext_base_lamB_Ye_0p07e9.mat'); 
vplist06  = result06['Vplist'];
pplist06  = result06['Pplist'];
result07 = sio.loadmat('bm_ext_base_lamB_Ye_0p08e9.mat');
vplist07  = result07['Vplist'];
pplist07  = result07['Pplist'];
result08 = sio.loadmat('bm_ext_base_lamB_Ye_0p09e9.mat'); 
vplist08  = result08['Vplist'];
pplist08  = result08['Pplist'];
result09 = sio.loadmat('bm_ext_base_lamB_Ye_0p1e9.mat'); 
vplist09  = result09['Vplist'];
pplist09  = result09['Pplist'];
result10 = sio.loadmat('bm_ext_base_lamB_Ye_0p2e9.mat'); 
vplist10  = result10['Vplist'];
pplist10  = result10['Pplist'];
result11 = sio.loadmat('bm_ext_base_lamB_Ye_0p3e9.mat'); 
vplist11  = result11['Vplist'];
pplist11  = result11['Pplist'];
result12 = sio.loadmat('bm_ext_base_lamB_Ye_1p3e9.mat'); 
vplist12  = result12['Vplist'];
pplist12  = result12['Pplist'];
result13 = sio.loadmat('bm_ext_base_lamB_Ye_2p3e9.mat'); 
vplist13  = result13['Vplist'];
pplist13  = result13['Pplist'];
result14 = sio.loadmat('bm_ext_base_lamB_Ye_3p3e9.mat'); 
vplist14  = result14['Vplist'];
pplist14  = result14['Pplist'];
result15 = sio.loadmat('bm_ext_base_lamB_Ye_4p3e9.mat'); 
vplist15  = result15['Vplist'];
pplist15  = result15['Pplist'];
result16 = sio.loadmat('bm_ext_base_lamB_Ye_5p3e9.mat'); 
vplist16  = result16['Vplist'];
pplist16  = result16['Pplist'];
result17 = sio.loadmat('bm_ext_base_lamB_Ye_6p3e9.mat'); 
vplist17  = result17['Vplist'];
pplist17  = result17['Pplist'];
result18 = sio.loadmat('bm_ext_base_lamB_Ye_7p3e9.mat'); 
vplist18  = result18['Vplist'];
pplist18  = result18['Pplist'];
result19 = sio.loadmat('bm_ext_base_lamB_Ye_8p3e9.mat'); 
vplist19  = result19['Vplist'];
pplist19  = result19['Pplist'];
result20 = sio.loadmat('bm_ext_base_lamB_Ye_9p3e9.mat'); 
vplist20  = result20['Vplist'];
pplist20  = result20['Pplist'];
result21 = sio.loadmat('bm_ext_base_lamB_Ye_10p3e9.mat'); 
vplist21  = result21['Vplist'];
pplist21  = result21['Pplist'];
result22 = sio.loadmat('bm_ext_base_lamB_Ye_20p3e9.mat'); 
vplist22  = result22['Vplist'];
pplist22  = result22['Pplist'];
result23 = sio.loadmat('bm_ext_base_lamB_Ye_30p3e9.mat'); 
vplist23  = result23['Vplist'];
pplist23  = result23['Pplist'];
result24 = sio.loadmat('bm_ext_base_lamB_Ye_40p3e9.mat'); 
vplist24  = result24['Vplist'];
pplist24  = result24['Pplist'];
result25 = sio.loadmat('bm_ext_base_lamB_Ye_50p3e9.mat'); 
vplist25  = result25['Vplist'];
pplist25  = result25['Pplist'];
result26 = sio.loadmat('bm_ext_base_lamB_Ye_60p3e9.mat'); 
vplist26  = result26['Vplist'];
pplist26  = result26['Pplist'];
result27 = sio.loadmat('bm_ext_base_lamB_Ye_70p3e9.mat'); 
vplist27  = result27['Vplist'];
pplist27  = result27['Pplist'];
result28 = sio.loadmat('bm_ext_base_lamB_Ye_80p3e9.mat'); 
vplist28  = result28['Vplist'];
pplist28  = result28['Pplist'];
result29 = sio.loadmat('bm_ext_base_lamB_Ye_90p3e9.mat'); 
vplist29  = result29['Vplist'];
pplist29  = result29['Pplist'];
result30 = sio.loadmat('bm_ext_base_lamB_Ye_100p3e9.mat'); 
vplist30  = result30['Vplist'];
pplist30  = result30['Pplist'];
result31 = sio.loadmat('bm_ext_base_lamB_Ye_200p3e9.mat'); 
vplist31  = result31['Vplist'];
pplist31  = result31['Pplist'];
result32 = sio.loadmat('bm_ext_base_lamB_Ye_300p3e9.mat'); 
vplist32  = result32['Vplist'];
pplist32  = result32['Pplist'];
result33 = sio.loadmat('bm_ext_base_lamB_Ye_400p3e9.mat'); 
vplist33  = result33['Vplist'];
pplist33  = result33['Pplist'];


fr        = result00['fr'];
Rl        = result00['Rl'];
xib       = result00['xib'];

am_vplist00, ph_vplist00 = np.abs(vplist00), np.angle(vplist00)
am_vplist01, ph_vplist01 = np.abs(vplist01), np.angle(vplist01)
am_vplist02, ph_vplist02 = np.abs(vplist02), np.angle(vplist02)
am_vplist03, ph_vplist03 = np.abs(vplist03), np.angle(vplist03)
am_vplist04, ph_vplist04 = np.abs(vplist04), np.angle(vplist04)
am_vplist05, ph_vplist05 = np.abs(vplist05), np.angle(vplist05)
am_vplist06, ph_vplist06 = np.abs(vplist06), np.angle(vplist06)
am_vplist07, ph_vplist07 = np.abs(vplist07), np.angle(vplist07)
am_vplist08, ph_vplist08 = np.abs(vplist08), np.angle(vplist08)
am_vplist09, ph_vplist09 = np.abs(vplist09), np.angle(vplist09)
am_vplist10, ph_vplist10 = np.abs(vplist10), np.angle(vplist10)
am_vplist11, ph_vplist11 = np.abs(vplist11), np.angle(vplist11)
am_vplist12, ph_vplist12 = np.abs(vplist12), np.angle(vplist12)
am_vplist13, ph_vplist13 = np.abs(vplist13), np.angle(vplist13)
am_vplist14, ph_vplist14 = np.abs(vplist14), np.angle(vplist14)
am_vplist15, ph_vplist15 = np.abs(vplist15), np.angle(vplist15)
am_vplist16, ph_vplist16 = np.abs(vplist16), np.angle(vplist16)
am_vplist17, ph_vplist17 = np.abs(vplist17), np.angle(vplist17)
am_vplist18, ph_vplist18 = np.abs(vplist18), np.angle(vplist18)
am_vplist19, ph_vplist19 = np.abs(vplist19), np.angle(vplist19)
am_vplist20, ph_vplist20 = np.abs(vplist20), np.angle(vplist20)
am_vplist21, ph_vplist21 = np.abs(vplist21), np.angle(vplist21)
am_vplist22, ph_vplist22 = np.abs(vplist22), np.angle(vplist22)
am_vplist23, ph_vplist23 = np.abs(vplist23), np.angle(vplist23)
am_vplist24, ph_vplist24 = np.abs(vplist24), np.angle(vplist24)
am_vplist25, ph_vplist25 = np.abs(vplist25), np.angle(vplist25)
am_vplist26, ph_vplist26 = np.abs(vplist26), np.angle(vplist26)
am_vplist27, ph_vplist27 = np.abs(vplist27), np.angle(vplist27)
am_vplist28, ph_vplist28 = np.abs(vplist28), np.angle(vplist28)
am_vplist29, ph_vplist29 = np.abs(vplist29), np.angle(vplist29)
am_vplist30, ph_vplist30 = np.abs(vplist30), np.angle(vplist30)
am_vplist31, ph_vplist31 = np.abs(vplist31), np.angle(vplist31)
am_vplist32, ph_vplist32 = np.abs(vplist32), np.angle(vplist32)
am_vplist33, ph_vplist33 = np.abs(vplist33), np.angle(vplist33)



am_pplist00, ph_pplist00 = np.abs(pplist00), np.angle(pplist00)
am_pplist01, ph_pplist01 = np.abs(pplist01), np.angle(pplist01) 
am_pplist02, ph_pplist02 = np.abs(pplist02), np.angle(pplist02) 
am_pplist03, ph_pplist03 = np.abs(pplist03), np.angle(pplist03) 
am_pplist04, ph_pplist04 = np.abs(pplist04), np.angle(pplist04) 
am_pplist05, ph_pplist05 = np.abs(pplist05), np.angle(pplist05) 
am_pplist06, ph_pplist06 = np.abs(pplist06), np.angle(pplist06) 
am_pplist07, ph_pplist07 = np.abs(pplist07), np.angle(pplist07) 
am_pplist08, ph_pplist08 = np.abs(pplist08), np.angle(pplist08) 
am_pplist09, ph_pplist09 = np.abs(pplist09), np.angle(pplist09) 
am_pplist10, ph_pplist10 = np.abs(pplist10), np.angle(pplist10)
am_pplist11, ph_pplist11 = np.abs(pplist11), np.angle(pplist11)
am_pplist12, ph_pplist12 = np.abs(pplist12), np.angle(pplist12)
am_pplist13, ph_pplist13 = np.abs(pplist13), np.angle(pplist13)
am_pplist14, ph_pplist14 = np.abs(pplist14), np.angle(pplist14)
am_pplist15, ph_pplist15 = np.abs(pplist15), np.angle(pplist15)
am_pplist16, ph_pplist16 = np.abs(pplist16), np.angle(pplist16)
am_pplist17, ph_pplist17 = np.abs(pplist17), np.angle(pplist17)
am_pplist18, ph_pplist18 = np.abs(pplist18), np.angle(pplist18)
am_pplist19, ph_pplist19 = np.abs(pplist19), np.angle(pplist19)
am_pplist20, ph_pplist20 = np.abs(pplist20), np.angle(pplist20) 
am_pplist21, ph_pplist21 = np.abs(pplist21), np.angle(pplist21)
am_pplist22, ph_pplist22 = np.abs(pplist22), np.angle(pplist22)
am_pplist23, ph_pplist23 = np.abs(pplist23), np.angle(pplist23)
am_pplist24, ph_pplist24 = np.abs(pplist24), np.angle(pplist24)
am_pplist25, ph_pplist25 = np.abs(pplist25), np.angle(pplist25)
am_pplist26, ph_pplist26 = np.abs(pplist26), np.angle(pplist26)
am_pplist27, ph_pplist27 = np.abs(pplist27), np.angle(pplist27)
am_pplist28, ph_pplist28 = np.abs(pplist28), np.angle(pplist28)
am_pplist29, ph_pplist29 = np.abs(pplist29), np.angle(pplist29)
am_pplist30, ph_pplist30 = np.abs(pplist30), np.angle(pplist30) 
am_pplist31, ph_pplist31 = np.abs(pplist31), np.angle(pplist31)
am_pplist32, ph_pplist32 = np.abs(pplist32), np.angle(pplist32)
am_pplist33, ph_pplist33 = np.abs(pplist33), np.angle(pplist33)


def plot_vol_lamB_vs_fr_Rl():
    fig01, ax = plt.subplots(ncols=3, nrows=2, figsize=(18,24), sharex=True)

    ax[0,0].plot(fr[0,:],am_vplist00[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,0].plot(fr[0,:],am_vplist00[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,0].plot(fr[0,:],am_vplist00[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,0].plot(fr[0,:],am_vplist00[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,0].set_title('$Y_e$=0.01e9')
    ax[0,0].set_xlim(1,100)
    ax[0,0].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[0,0].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[0,0].legend(loc='lower right', ncol=4)


    ax[0,1].plot(fr[0,:],am_vplist05[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,1].plot(fr[0,:],am_vplist05[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,1].plot(fr[0,:],am_vplist05[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,1].plot(fr[0,:],am_vplist05[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,1].set_title('$Y_e$=0.02e9')
    ax[0,1].set_xlim(1,100)
    ax[0,1].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[0,1].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[0,1].legend(loc='lower right', ncol=4)


    ax[0,2].plot(fr[0,:],am_vplist10[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,2].plot(fr[0,:],am_vplist10[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,2].plot(fr[0,:],am_vplist10[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,2].plot(fr[0,:],am_vplist10[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,2].set_title('$Y_e$=0.03e9')
    ax[0,2].set_xlim(1,100)
    ax[0,2].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[0,2].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[0,2].legend(loc='lower right', ncol=4)


    ax[1,0].plot(fr[0,:],am_vplist15[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,0].plot(fr[0,:],am_vplist15[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,0].plot(fr[0,:],am_vplist15[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,0].plot(fr[0,:],am_vplist15[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,0].set_title('$Y_e$=0.04e9')
    ax[1,0].set_xlim(1,100)
    ax[1,0].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[1,0].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[1,0].legend(loc='lower right', ncol=4)


    ax[1,1].plot(fr[0,:],am_vplist20[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,1].plot(fr[0,:],am_vplist20[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,1].plot(fr[0,:],am_vplist20[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,1].plot(fr[0,:],am_vplist20[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,1].set_title('$Y_e$=0.05e9')
    ax[1,1].set_xlim(1,100)
    ax[1,1].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[1,1].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[1,1].legend(loc='lower right', ncol=4)

    ax[1,2].plot(fr[0,:],am_vplist25[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,2].plot(fr[0,:],am_vplist25[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,2].plot(fr[0,:],am_vplist25[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,2].plot(fr[0,:],am_vplist25[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,2].set_title('$Y_e$=0.06e9')
    ax[1,2].set_xlim(1,100)
    ax[1,2].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[1,2].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[1,2].legend(loc='lower right', ncol=4)




    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=ax[0,0].transAxes)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=ax[0,1].transAxes)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=ax[0,2].transAxes)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=ax[1,0].transAxes)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=ax[1,1].transAxes)
    plt.text(0.02, 0.93, "(f)", fontweight="bold", transform=ax[1,2].transAxes)
    plt.suptitle('Amplitude of the output voltage $V_p$ versus base excitation frequency $fr$ at different $R_l$ and $\lambda_l$',fontsize=18)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.08, hspace=0.17)
    # plt.tight_layout(w_pad=0.1, h_pad=0.01)

    # plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.pdf")
    # plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.eps")
    # plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.jpg",dpi=300)
    plt.show()

def plot_pow_lamB_vs_fr_Rl():
    fig01, ax = plt.subplots(ncols=3, nrows=2, figsize=(18,24), sharex=True)

    ax[0,0].plot(fr[0,:],am_pplist00[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,0].plot(fr[0,:],am_pplist00[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,0].plot(fr[0,:],am_pplist00[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,0].plot(fr[0,:],am_pplist00[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,0].set_title('$Y_e$=0.01e9')
    ax[0,0].set_xlim(1,100)
    ax[0,0].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[0,0].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[0,0].legend(loc='lower right', ncol=4)


    ax[0,1].plot(fr[0,:],am_pplist05[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,1].plot(fr[0,:],am_pplist05[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,1].plot(fr[0,:],am_pplist05[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,1].plot(fr[0,:],am_pplist05[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,1].set_title('$Y_e$=0.02e9')
    ax[0,1].set_xlim(1,100)
    ax[0,1].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[0,1].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[0,1].legend(loc='lower right', ncol=4)


    ax[0,2].plot(fr[0,:],am_pplist10[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[0,2].plot(fr[0,:],am_pplist10[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[0,2].plot(fr[0,:],am_pplist10[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[0,2].plot(fr[0,:],am_pplist10[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[0,2].set_title('$Y_e$=0.03e9')
    ax[0,2].set_xlim(1,100)
    ax[0,2].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[0,2].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[0,2].legend(loc='lower right', ncol=4)


    ax[1,0].plot(fr[0,:],am_pplist15[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,0].plot(fr[0,:],am_pplist15[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,0].plot(fr[0,:],am_pplist15[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,0].plot(fr[0,:],am_pplist15[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,0].set_title('$Y_e$=0.04e9')
    ax[1,0].set_xlim(1,100)
    ax[1,0].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[1,0].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[1,0].legend(loc='lower right', ncol=4)


    ax[1,1].plot(fr[0,:],am_pplist20[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,1].plot(fr[0,:],am_pplist20[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,1].plot(fr[0,:],am_pplist20[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,1].plot(fr[0,:],am_pplist20[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,1].set_title('$Y_e$=0.05e9')
    ax[1,1].set_xlim(1,100)
    ax[1,1].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[1,1].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[1,1].legend(loc='lower right', ncol=4)

    ax[1,2].plot(fr[0,:],am_pplist25[0,:],'r', label= '$R_l$ = 1 $\Omega$')
    ax[1,2].plot(fr[0,:],am_pplist25[2,:],'b.', label= '$R_l$ = 100 $\Omega$')
    ax[1,2].plot(fr[0,:],am_pplist25[4,:],'m*', label= '$R_l$ = 10 k$\Omega$')
    ax[1,2].plot(fr[0,:],am_pplist25[6,:],'k--', label= '$R_l$ = 1 M$\Omega$')
    ax[1,2].set_title('$Y_e$=0.06e9')
    ax[1,2].set_xlim(1,100)
    ax[1,2].set_yscale('log')
    # ax11.set_xlabel('Base excitation frequency $fr$')
    ax[1,2].set_ylabel('Amplitude of the output voltage $V_p$ (V)')
    ax[1,2].legend(loc='lower right', ncol=4)


    plt.text(0.02, 0.93, "(a)", fontweight="bold", transform=ax[0,0].transAxes)
    plt.text(0.02, 0.93, "(b)", fontweight="bold", transform=ax[0,1].transAxes)
    plt.text(0.02, 0.93, "(c)", fontweight="bold", transform=ax[0,2].transAxes)
    plt.text(0.02, 0.93, "(d)", fontweight="bold", transform=ax[1,0].transAxes)
    plt.text(0.02, 0.93, "(e)", fontweight="bold", transform=ax[1,1].transAxes)
    plt.text(0.02, 0.93, "(f)", fontweight="bold", transform=ax[1,2].transAxes)
    plt.suptitle('Amplitude of the output voltage $V_p$ versus base excitation frequency $fr$ at different $R_l$ and $\lambda_l$',fontsize=18)
    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.08, hspace=0.17)
    # plt.tight_layout(w_pad=0.1, h_pad=0.01)

    # plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.pdf")
    # plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.eps")
    # plt.savefig("fig_output_voltage_vs_fr_Rl_laml_all.jpg",dpi=300)
    plt.show()

def plot_perf_lamB_0p3_0p4_vs_fr_Rl():
    fig, axes = plt.subplots(ncols = 3, nrows = 2, figsize=(24,18), sharex=True)
    axes[0,0].plot(Rl[:,0],am_vplist00[:,200], 'r-*', label='fr=10')
    axes[0,0].plot(Rl[:,0],am_vplist00[:,300], 'g-.', label='fr=31.62')
    axes[0,0].plot(Rl[:,0],am_vplist00[:,325], 'b--', label='fr=42.17')
    axes[0,0].plot(Rl[:,0],am_vplist00[:,350], 'm-', label='fr=56.23')
    axes[0,0].plot(Rl[:,0],am_vplist00[:,375], 'c-d', label='fr=74.99')
    axes[0,0].plot(Rl[:,0],am_vplist00[:,400], 'k-o', label='fr=100')
    axes[0,0].set_xscale('log')
    axes[0,0].set_yscale('log')
    axes[0,0].set_title('$\lambda_B$ = 0.0')
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
    axes[1,0].set_title('$\lambda_B$ = 0.0')
    axes[1,0].legend(loc='lower right', ncol=2)
    axes[1,0].set_xlabel('Externally connected resistance $R_l$ ($\Omega$)')
    axes[1,0].set_ylabel('Amplitude of the output power $P_p$ (W)')


    axes[0,1].plot(Rl[:,0],am_vplist13[:,200], 'r-*', label='fr=10')
    axes[0,1].plot(Rl[:,0],am_vplist13[:,300], 'g-.', label='fr=31.62')
    axes[0,1].plot(Rl[:,0],am_vplist13[:,325], 'b--', label='fr=42.17')
    axes[0,1].plot(Rl[:,0],am_vplist13[:,350], 'm-', label='fr=56.23')
    axes[0,1].plot(Rl[:,0],am_vplist13[:,375], 'c-d', label='fr=74.99')
    axes[0,1].plot(Rl[:,0],am_vplist03[:,400], 'k-o', label='fr=100')
    axes[0,1].set_xscale('log')
    axes[0,1].set_yscale('log')
    axes[0,1].set_title('$\lambda_B$ = 0.3')
    axes[0,1].legend(loc='lower right', ncol=2)
    # axes[0,1].set_xlabel('Externally connected resistance $R_l$ ($\Omega$)')
    # axes[0,1].set_ylabel('Amplitude of the output voltage $V_p$ (W)')

    axes[1,1].plot(Rl[:,0],am_pplist13[:,200], 'r-*', label='fr=10')
    axes[1,1].plot(Rl[:,0],am_pplist13[:,300], 'g-.', label='fr=31.62')
    axes[1,1].plot(Rl[:,0],am_pplist13[:,325], 'b--', label='fr=42.17')
    axes[1,1].plot(Rl[:,0],am_pplist13[:,350], 'm-', label='fr=56.23')
    axes[1,1].plot(Rl[:,0],am_pplist13[:,375], 'c-d', label='fr=74.99')
    axes[1,1].plot(Rl[:,0],am_pplist13[:,400], 'k-o', label='fr=100')
    axes[1,1].set_xscale('log')
    axes[1,1].set_yscale('log')
    axes[1,1].set_title('$\lambda_B$ = 0.3')
    axes[1,1].legend(loc='lower right', ncol=2)
    axes[1,1].set_xlabel('Externally connected resistance $R_l$ ($\Omega$)')
    # axes[1,1].set_ylabel('Amplitude of the output power $P_p$ (W)')


    axes[0,2].plot(Rl[:,0],am_vplist24[:,200], 'r-*', label='fr=10')
    axes[0,2].plot(Rl[:,0],am_vplist24[:,300], 'g-.', label='fr=31.62')
    axes[0,2].plot(Rl[:,0],am_vplist24[:,325], 'b--', label='fr=42.17')
    axes[0,2].plot(Rl[:,0],am_vplist24[:,350], 'm-', label='fr=56.23')
    axes[0,2].plot(Rl[:,0],am_vplist24[:,375], 'c-d', label='fr=74.99')
    axes[0,2].plot(Rl[:,0],am_vplist24[:,400], 'k-o', label='fr=100')
    axes[0,2].set_xscale('log')
    axes[0,2].set_yscale('log')
    axes[0,2].set_title('$\lambda_B$ = 0.4')
    axes[0,2].legend(loc='lower right', ncol=2)
    # axes[0,2].set_xlabel('Externally connected resistance $R_l$ ($\Omega$)')
    # axes[0,2].set_ylabel('Amplitude of the output voltage $V_p$ (W)')

    axes[1,2].plot(Rl[:,0],am_pplist24[:,200], 'r-*', label='fr=10')
    axes[1,2].plot(Rl[:,0],am_pplist24[:,300], 'g-.', label='fr=31.62')
    axes[1,2].plot(Rl[:,0],am_pplist24[:,325], 'b--', label='fr=42.17')
    axes[1,2].plot(Rl[:,0],am_pplist24[:,350], 'm-', label='fr=56.23')
    axes[1,2].plot(Rl[:,0],am_pplist24[:,375], 'c-d', label='fr=74.99')
    axes[1,2].plot(Rl[:,0],am_pplist24[:,400], 'k-o', label='fr=100')
    axes[1,2].set_xscale('log')
    axes[1,2].set_yscale('log')
    axes[1,2].set_title('$\lambda_B$ = 0.4')
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
    # plt.savefig("fig_perf_lamB_0p3_0p4_vs_fr_Rl.pdf")
    # plt.savefig("fig_perf_lamB_0p3_0p4_vs_fr_Rl.eps")
    # plt.savefig("fig_perf_lamB_0p3_0p4_vs_fr_Rl.jpg",dpi=300)
    plt.show()

def plot_vol_fr_sl_Rl_sl_vs_lamB():
    fig, axes = plt.subplots(ncols = 4, nrows = 4, figsize=(18,24), sharex=True)

    am_vplist = np.array([am_vplist00, am_vplist01, am_vplist02, am_vplist03,
                 am_vplist04, am_vplist05, am_vplist06, am_vplist07,
                 am_vplist08, am_vplist09, am_vplist10, am_vplist11,
                 am_vplist12, am_vplist13, am_vplist14, am_vplist15,
                 am_vplist16, am_vplist17, am_vplist18, am_vplist19,
                 am_vplist20, am_vplist21, am_vplist22, am_vplist23,
                 am_vplist24, am_vplist25, am_vplist26, am_vplist27,
                 am_vplist28, am_vplist29, am_vplist30, am_vplist31,
                 am_vplist32, am_vplist33])
    am_pplist = np.array([am_pplist00, am_pplist01, am_pplist02, am_pplist03,
                 am_pplist04, am_pplist05, am_pplist06, am_pplist07,
                 am_pplist08, am_pplist09, am_pplist10, am_pplist11,
                 am_pplist12, am_pplist13, am_pplist14, am_pplist15,
                 am_pplist16, am_pplist17, am_pplist18, am_pplist19,
                 am_pplist20, am_pplist21, am_pplist22, am_pplist23,
                 am_pplist24, am_pplist25, am_pplist26, am_pplist27,
                 am_pplist28, am_pplist29, am_pplist30, am_pplist31,
                 am_pplist32, am_pplist33])
    lamB_list = np.asarray([0.01e9, 0.02e9, 0.03e9, 0.04e9, 0.05e9,
                            0.06e9, 0.07e9, 0.08e9, 0.09e9, 0.1e9,
                            0.2e9, 0.3e9, 1.3e9, 2.3e9, 3.3e9,
                            4.3e9, 5.3e9, 6.3e9, 7.3e9, 8.3e9,
                            9.3e9, 10.3e9, 20.3e9, 30.3e9, 40.3e9,
                            50.3e9, 60.3e9, 70.3e9, 80.3e9, 90.3e9,
                            100.3e9, 200.3e9, 300.3e9, 400.3e9])
    # print(am_vplist.shape)
    # print(am_pplist.shape)
    # print(laml_list)
    class ScalarFormatterForceFormat(mtick.ScalarFormatter):
        def _set_format(self,vmin,vmax):  # Override function that finds format to use.
            self.format = "%1.2f"  # Give format here
    
    yfmt = ScalarFormatterForceFormat()
    yfmt.set_powerlimits((0,0))

    axes[0,0].plot(lamB_list,am_vplist[:, 0, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 1 $\Omega$')
    axes[0,0].yaxis.set_major_formatter(yfmt)
    axes[0,0].set_xscale('log')
    axes[0,1].plot(lamB_list,am_vplist[:, 2, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 100 $\Omega$')
    axes[0,1].yaxis.set_major_formatter(yfmt)
    axes[0,2].plot(lamB_list,am_vplist[:, 4, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[0,2].yaxis.set_major_formatter(yfmt)
    axes[0,3].plot(lamB_list,am_vplist[:, 6, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[0,3].yaxis.set_major_formatter(yfmt)


    axes[1,0].plot(lamB_list,am_vplist[:, 0, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 1 $\Omega$')
    axes[1,0].yaxis.set_major_formatter(yfmt)
    # axes[1,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,1].plot(lamB_list,am_vplist[:, 2, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 100 $\Omega$')
    axes[1,1].yaxis.set_major_formatter(yfmt)
    # axes[1,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,2].plot(lamB_list,am_vplist[:, 4, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[1,2].yaxis.set_major_formatter(yfmt)
    # axes[1,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,3].plot(lamB_list,am_vplist[:, 6, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[1,3].yaxis.set_major_formatter(yfmt)
    # axes[1,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[2,0].plot(lamB_list,am_vplist[:, 0, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 1 $\Omega$')
    axes[2,0].yaxis.set_major_formatter(yfmt)
    # axes[2,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,1].plot(lamB_list,am_vplist[:, 2, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 10 $\Omega$')
    axes[2,1].yaxis.set_major_formatter(yfmt)
    # axes[2,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,2].plot(lamB_list,am_vplist[:, 4, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[2,2].yaxis.set_major_formatter(yfmt)
    # axes[2,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,3].plot(lamB_list,am_vplist[:, 6, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[2,3].yaxis.set_major_formatter(yfmt)
    # axes[2,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[3,0].plot(lamB_list,am_vplist[:, 0, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 1 $\Omega$')
    axes[3,0].yaxis.set_major_formatter(yfmt)
    # axes[3,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,1].plot(lamB_list,am_vplist[:, 2, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 100 $\Omega$')
    axes[3,1].yaxis.set_major_formatter(yfmt)
    # axes[3,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,2].plot(lamB_list,am_vplist[:, 4, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[3,2].yaxis.set_major_formatter(yfmt)
    # axes[3,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,3].plot(lamB_list,am_vplist[:, 6, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[3,3].yaxis.set_major_formatter(yfmt)
    # axes[3,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    for i in range(4):
        for j in range(4):
            axes[i,j].legend(loc='best')


    plt.subplots_adjust(left=0.05, right=0.98, top=0.90, bottom=0.07, wspace=0.15, hspace=0.17)
    # plt.savefig("fig_vol_fr_sl_Rl_sl_vs_laml.pdf")
    # plt.savefig("fig_vol_fr_sl_Rl_sl_vs_laml.eps")
    # plt.savefig("fig_vol_fr_sl_Rl_sl_vs_laml.jpg",dpi=300)
    plt.show()

def plot_pow_fr_sl_Rl_sl_vs_lamB():
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
    # plt.savefig("fig_pow_fr_sl_Rl_sl_vs_laml.pdf")
    # plt.savefig("fig_pow_fr_sl_Rl_sl_vs_laml.eps")
    # plt.savefig("fig_pow_fr_sl_Rl_sl_vs_laml.jpg",dpi=300)
    plt.show()

if __name__ == '__main__':
    # plot_vol_lamB_vs_fr_Rl()
    # plot_pow_laml_vs_fr_Rl()
    # plot_perf_lamB_0p3_0p4_vs_fr_Rl()
    plot_vol_fr_sl_Rl_sl_vs_lamB()
    # plot_pow_fr_sl_Rl_sl_vs_lamB()
