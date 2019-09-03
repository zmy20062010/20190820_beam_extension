clc;clear;close all;

result00 = load('bm_ext_base_lamB_Ye_0p01e9.mat'); 
vplist00  = result00.Vplist;
result01 = load('bm_ext_base_lamB_Ye_0p02e9.mat'); 
vplist01  = result01.Vplist;
result02 = load('bm_ext_base_lamB_Ye_0p03e9.mat'); 
vplist02  = result02.Vplist;
result03 = load('bm_ext_base_lamB_Ye_0p04e9.mat'); 
vplist03  = result03.Vplist;
result04 = load('bm_ext_base_lamB_Ye_0p05e9.mat'); 
vplist04  = result04.Vplist;
result05 = load('bm_ext_base_lamB_Ye_0p06e9.mat'); 
vplist05  = result05.Vplist;
result06 = load('bm_ext_base_lamB_Ye_0p07e9.mat'); 
vplist06  = result06.Vplist;
result07 = load('bm_ext_base_lamB_Ye_0p08e9.mat');
vplist07  = result07.Vplist;
result08 = load('bm_ext_base_lamB_Ye_0p09e9.mat'); 
vplist08  = result08.Vplist;
result09 = load('bm_ext_base_lamB_Ye_0p1e9.mat'); 
vplist09  = result09.Vplist;
result10 = load('bm_ext_base_lamB_Ye_0p2e9.mat'); 
vplist10  = result10.Vplist;
result11 = load('bm_ext_base_lamB_Ye_0p3e9.mat'); 
vplist11  = result11.Vplist;
result12 = load('bm_ext_base_lamB_Ye_1p3e9.mat'); 
vplist12  = result12.Vplist;
result13 = load('bm_ext_base_lamB_Ye_2p3e9.mat'); 
vplist13  = result13.Vplist;
result14 = load('bm_ext_base_lamB_Ye_3p3e9.mat'); 
vplist14  = result14.Vplist;
result15 = load('bm_ext_base_lamB_Ye_4p3e9.mat'); 
vplist15  = result15.Vplist;
result16 = load('bm_ext_base_lamB_Ye_5p3e9.mat'); 
vplist16  = result16.Vplist;
result17 = load('bm_ext_base_lamB_Ye_6p3e9.mat'); 
vplist17  = result17.Vplist;
result18 = load('bm_ext_base_lamB_Ye_7p3e9.mat'); 
vplist18  = result18.Vplist;
result19 = load('bm_ext_base_lamB_Ye_8p3e9.mat'); 
vplist19  = result19.Vplist;
result20 = load('bm_ext_base_lamB_Ye_9p3e9.mat'); 
vplist20  = result20.Vplist;
result21 = load('bm_ext_base_lamB_Ye_10p3e9.mat'); 
vplist21  = result21.Vplist;
result22 = load('bm_ext_base_lamB_Ye_20p3e9.mat'); 
vplist22  = result22.Vplist;
result23 = load('bm_ext_base_lamB_Ye_30p3e9.mat'); 
vplist23  = result23.Vplist;
result24 = load('bm_ext_base_lamB_Ye_40p3e9.mat'); 
vplist24  = result24.Vplist;
result25 = load('bm_ext_base_lamB_Ye_50p3e9.mat'); 
vplist25  = result25.Vplist;
result26 = load('bm_ext_base_lamB_Ye_60p3e9.mat'); 
vplist26  = result26.Vplist;
result27 = load('bm_ext_base_lamB_Ye_70p3e9.mat'); 
vplist27  = result27.Vplist;
result28 = load('bm_ext_base_lamB_Ye_80p3e9.mat'); 
vplist28  = result28.Vplist;
result29 = load('bm_ext_base_lamB_Ye_90p3e9.mat'); 
vplist29  = result29.Vplist;
result30 = load('bm_ext_base_lamB_Ye_100p3e9.mat'); 
vplist30  = result30.Vplist;
result31 = load('bm_ext_base_lamB_Ye_200p3e9.mat'); 
vplist31  = result31.Vplist;
result32 = load('bm_ext_base_lamB_Ye_300p3e9.mat'); 
vplist32  = result32.Vplist;
result33 = load('bm_ext_base_lamB_Ye_400p3e9.mat'); 
vplist33  = result33.Vplist;


fr = result00.fr;
Rl = result00.Rl;
xib  = result00.xib;


%% Rl from 1 ohm to 10 Mohm, different laml
% figure(1)
% mesh(fr,Rl,abs(vplist00), 'DisplayName','Y_e=0.01e9'); hold on
% mesh(fr,Rl,abs(vplist01), 'DisplayName','Y_e=0.02e9')
% mesh(fr,Rl,abs(vplist02), 'DisplayName','Y_e=0.03e9')
% mesh(fr,Rl,abs(vplist03), 'DisplayName','Y_e=0.04e9')
% mesh(fr,Rl,abs(vplist04), 'DisplayName','Y_e=0.05e9')
% mesh(fr,Rl,abs(vplist05), 'DisplayName','Y_e=0.06e9')
% mesh(fr,Rl,abs(vplist06), 'DisplayName','Y_e=0.07e9')
% mesh(fr,Rl,abs(vplist07), 'DisplayName','Y_e=0.08e9')
% mesh(fr,Rl,abs(vplist08), 'DisplayName','Y_e=0.09e9')
% mesh(fr,Rl,abs(vplist09), 'DisplayName','Y_e=0.1e9')
% mesh(fr,Rl,abs(vplist10), 'DisplayName','Y_e=0.2e9')
% mesh(fr,Rl,abs(vplist11), 'DisplayName','Y_e=0.3e9')
% mesh(fr,Rl,abs(vplist12), 'DisplayName','Y_e=1.3e9')
% mesh(fr,Rl,abs(vplist13), 'DisplayName','Y_e=2.3e9')
% mesh(fr,Rl,abs(vplist14), 'DisplayName','Y_e=3.3e9')
% set(gca,'XScale','log');
% set(gca,'YScale','log');
% set(gca,'ZScale','log');
% xlabel('fr');
% ylabel('Rl');
% zlabel('output voltage amplitude');
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% set(gcf, 'color', 'w')
% legend('show')
% title('length ratio \lambda\_l = 0.0')




%% Rl  1 ohm, different laml
figure(2)
plot(fr(1,:),abs(vplist00(1,:)),'r', 'DisplayName','Y_e=0.01e9'); hold on
plot(fr(1,:),abs(vplist01(1,:)),'g', 'DisplayName','Y_e=0.02e9')
plot(fr(1,:),abs(vplist02(1,:)),'b', 'DisplayName','Y_e=0.03e9')
plot(fr(1,:),abs(vplist03(1,:)),'k', 'DisplayName','Y_e=0.04e9')
plot(fr(1,:),abs(vplist04(1,:)),'c', 'DisplayName','Y_e=0.05e9')
plot(fr(1,:),abs(vplist05(1,:)),'r.-', 'DisplayName','Y_e=0.06e9')
plot(fr(1,:),abs(vplist06(1,:)),'g.-', 'DisplayName','Y_e=0.07e9')
plot(fr(1,:),abs(vplist07(1,:)),'b.-', 'DisplayName','Y_e=0.08e9')
plot(fr(1,:),abs(vplist08(1,:)),'k.-', 'DisplayName','Y_e=0.09e9')
plot(fr(1,:),abs(vplist09(1,:)),'c.-', 'DisplayName','Y_e=0.1e9')
plot(fr(1,:),abs(vplist10(1,:)),'y', 'DisplayName','Y_e=0.2e9')
plot(fr(1,:),abs(vplist11(1,:)),'y', 'DisplayName','Y_e=0.3e9')
plot(fr(1,:),abs(vplist12(1,:)),'y', 'DisplayName','Y_e=1.3e9')
plot(fr(1,:),abs(vplist13(1,:)),'y', 'DisplayName','Y_e=2.3e9')
plot(fr(1,:),abs(vplist14(1,:)),'y', 'DisplayName','Y_e=3.3e9')
set(gca, 'XScale', 'log');
set(gca, 'YScale', 'log');
xlabel('base excitation frequency');
ylabel('output voltage amplitude');
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
legend('show')
title('external electrical load R\_l = 1.0 \Omega')


%% Rl  10 ohm, different laml
figure(3)
plot(fr(1,:),abs(vplist00(2,:)),'r', 'DisplayName','Y_e=0.01e9'); hold on
plot(fr(1,:),abs(vplist01(2,:)),'g', 'DisplayName','Y_e=0.02e9')
plot(fr(1,:),abs(vplist02(2,:)),'b', 'DisplayName','Y_e=0.03e9')
plot(fr(1,:),abs(vplist03(2,:)),'k', 'DisplayName','Y_e=0.04e9')
plot(fr(1,:),abs(vplist04(2,:)),'c', 'DisplayName','Y_e=0.05e9')
plot(fr(1,:),abs(vplist05(2,:)),'r.-', 'DisplayName','Y_e=0.06e9')
plot(fr(1,:),abs(vplist06(2,:)),'g.-', 'DisplayName','Y_e=0.07e9')
plot(fr(1,:),abs(vplist07(2,:)),'b.-', 'DisplayName','Y_e=0.08e9')
plot(fr(1,:),abs(vplist08(2,:)),'k.-', 'DisplayName','Y_e=0.09e9')
plot(fr(1,:),abs(vplist09(2,:)),'c.-', 'DisplayName','Y_e=0.1e9')
plot(fr(1,:),abs(vplist10(2,:)),'r--', 'DisplayName','Y_e=0.2e9')
plot(fr(1,:),abs(vplist11(2,:)),'g--', 'DisplayName','Y_e=0.3e9')
plot(fr(1,:),abs(vplist12(2,:)),'b--', 'DisplayName','Y_e=1.3e9')
plot(fr(1,:),abs(vplist13(2,:)),'k--', 'DisplayName','Y_e=2.3e9')
plot(fr(1,:),abs(vplist14(2,:)),'c--', 'DisplayName','Y_e=3.3e9')
set(gca, 'XScale', 'log');
set(gca, 'YScale', 'log');
xlabel('base excitation frequency');
ylabel('output voltage amplitude');
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
legend('show')
title('external electrical load R\_l = 10.0 \Omega')



%% Rl  100 ohm, different laml
figure(4)
plot(fr(1,:),abs(vplist00(3,:)),'r', 'DisplayName','Y_e=0.01e9'); hold on
plot(fr(1,:),abs(vplist01(3,:)),'g', 'DisplayName','Y_e=0.02e9')
plot(fr(1,:),abs(vplist02(3,:)),'b', 'DisplayName','Y_e=0.03e9')
plot(fr(1,:),abs(vplist03(3,:)),'k', 'DisplayName','Y_e=0.04e9')
plot(fr(1,:),abs(vplist04(3,:)),'c', 'DisplayName','Y_e=0.05e9')
plot(fr(1,:),abs(vplist05(3,:)),'r.-', 'DisplayName','Y_e=0.06e9')
plot(fr(1,:),abs(vplist06(3,:)),'g.-', 'DisplayName','Y_e=0.07e9')
plot(fr(1,:),abs(vplist07(3,:)),'b.-', 'DisplayName','Y_e=0.08e9')
plot(fr(1,:),abs(vplist08(3,:)),'k.-', 'DisplayName','Y_e=0.09e9')
plot(fr(1,:),abs(vplist09(3,:)),'c.-', 'DisplayName','Y_e=0.1e9')
plot(fr(1,:),abs(vplist10(3,:)),'r--', 'DisplayName','Y_e=0.2e9')
plot(fr(1,:),abs(vplist11(3,:)),'g--', 'DisplayName','Y_e=0.3e9')
plot(fr(1,:),abs(vplist12(3,:)),'b--', 'DisplayName','Y_e=1.3e9')
plot(fr(1,:),abs(vplist13(3,:)),'k--', 'DisplayName','Y_e=2.3e9')
plot(fr(1,:),abs(vplist14(3,:)),'c--', 'DisplayName','Y_e=3.3e9')
set(gca, 'XScale', 'log');
set(gca, 'YScale', 'log');
xlabel('base excitation frequency');
ylabel('output voltage amplitude');
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
legend('show')
title('external electrical load R\_l = 100.0 \Omega')



%% Rl  100 ohm, different laml
figure(8)
hold on
% plot(fr(1,:),abs(vplist00(7,:)),'r', 'DisplayName','Y_e=0.01e9'); hold on
% plot(fr(1,:),abs(vplist01(7,:)),'g', 'DisplayName','Y_e=0.02e9')
plot(fr(1,:),abs(vplist02(7,:)),'b', 'DisplayName','Y_e=0.03e9')
% plot(fr(1,:),abs(vplist03(7,:)),'k', 'DisplayName','Y_e=0.04e9')
% plot(fr(1,:),abs(vplist04(7,:)),'c', 'DisplayName','Y_e=0.05e9')
% plot(fr(1,:),abs(vplist05(7,:)),'r.-', 'DisplayName','Y_e=0.06e9')
% plot(fr(1,:),abs(vplist06(7,:)),'g.-', 'DisplayName','Y_e=0.07e9')
% plot(fr(1,:),abs(vplist07(7,:)),'b.-', 'DisplayName','Y_e=0.08e9')
% plot(fr(1,:),abs(vplist08(7,:)),'k.-', 'DisplayName','Y_e=0.09e9')
% plot(fr(1,:),abs(vplist09(7,:)),'c.-', 'DisplayName','Y_e=0.1e9')
% plot(fr(1,:),abs(vplist10(7,:)),'r--', 'DisplayName','Y_e=0.2e9')
plot(fr(1,:),abs(vplist11(7,:)),'g--', 'DisplayName','Y_e=0.3e9')
% plot(fr(1,:),abs(vplist12(7,:)),'b--', 'DisplayName','Y_e=1.3e9')
plot(fr(1,:),abs(vplist13(7,:)),'k--', 'DisplayName','Y_e=2.3e9')
% plot(fr(1,:),abs(vplist14(7,:)),'c--', 'DisplayName','Y_e=3.3e9')
plot(fr(1,:),abs(vplist15(7,:)),'r--', 'DisplayName','Y_e=4.3e9')
% plot(fr(1,:),abs(vplist16(7,:)),'c--', 'DisplayName','Y_e=5.3e9')
plot(fr(1,:),abs(vplist17(7,:)),'c--', 'DisplayName','Y_e=6.3e9')
% plot(fr(1,:),abs(vplist18(7,:)),'c--', 'DisplayName','Y_e=7.3e9')
plot(fr(1,:),abs(vplist19(7,:)),'m--', 'DisplayName','Y_e=8.3e9')
% plot(fr(1,:),abs(vplist20(7,:)),'c--', 'DisplayName','Y_e=9.3e9')
plot(fr(1,:),abs(vplist21(7,:)),'b--', 'DisplayName','Y_e=10.3e9')
plot(fr(1,:),abs(vplist22(7,:)),'r', 'DisplayName','Y_e=20.3e9')
% plot(fr(1,:),abs(vplist23(7,:)),'c--', 'DisplayName','Y_e=30.3e9')
plot(fr(1,:),abs(vplist24(7,:)),'g', 'DisplayName','Y_e=40.3e9')
% plot(fr(1,:),abs(vplist25(7,:)),'c--', 'DisplayName','Y_e=50.3e9')
plot(fr(1,:),abs(vplist26(7,:)),'k', 'DisplayName','Y_e=60.3e9')
% plot(fr(1,:),abs(vplist27(7,:)),'c--', 'DisplayName','Y_e=70.3e9')
plot(fr(1,:),abs(vplist28(7,:)),'c', 'DisplayName','Y_e=80.3e9')
% plot(fr(1,:),abs(vplist29(7,:)),'c--', 'DisplayName','Y_e=90.3e9')
plot(fr(1,:),abs(vplist30(7,:)),'m', 'DisplayName','Y_e=100.3e9')
plot(fr(1,:),abs(vplist31(7,:)),'c-.', 'DisplayName','Y_e=200.3e9')
% plot(fr(1,:),abs(vplist32(7,:)),'c--', 'DisplayName','Y_e=300.3e9')
plot(fr(1,:),abs(vplist33(7,:)),'m-.', 'DisplayName','Y_e=400.3e9')
set(gca, 'XScale', 'log');
set(gca, 'YScale', 'log');
xlabel('base excitation frequency');
ylabel('output voltage amplitude');
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
xlim([1,100]);
legend('show')
title('external electrical load R\_l = 1000000.0 \Omega')



