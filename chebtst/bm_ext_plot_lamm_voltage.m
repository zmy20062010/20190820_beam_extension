clc;clear;close all;



result01 = load('bm_ext_base_lamm_rhoe_1p38e1.mat'); 
vplist01  = result01.Vplist;
result02 = load('bm_ext_base_lamm_rhoe_1p38e2.mat'); 
vplist02  = result02.Vplist;
result03 = load('bm_ext_base_lamm_rhoe_1p38e3.mat'); 
vplist03  = result03.Vplist;
result04 = load('bm_ext_base_lamm_rhoe_1p38e4.mat'); 
vplist04  = result04.Vplist;
result05 = load('bm_ext_base_lamm_rhoe_1p38e5.mat'); 
vplist05  = result05.Vplist;


fr = result01.fr;
Rl = result01.Rl;
xib  = result01.xib;

%% Rl from 1 ohm to 10 Mohm, different lamm or rhoe
% figure(1)
% mesh(fr,Rl,abs(vplist01), 'DisplayName','\rho_e=1.38e1'); hold on
% mesh(fr,Rl,abs(vplist02), 'DisplayName','\rho_e=1.38e2')
% mesh(fr,Rl,abs(vplist03), 'DisplayName','\rho_e=1.38e3')
% mesh(fr,Rl,abs(vplist04), 'DisplayName','\rho_e=1.38e4')
% mesh(fr,Rl,abs(vplist05), 'DisplayName','\rho_e=1.38e5')
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

% 
% 
% %% Rl  1 ohm, different laml
% figure(2)
% plot(fr(1,:),abs(vplist00(1,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
% plot(fr(1,:),abs(vplist01(1,:)),'g', 'DisplayName','\lambda_l=0.1')
% plot(fr(1,:),abs(vplist02(1,:)),'b', 'DisplayName','\lambda_l=0.2')
% plot(fr(1,:),abs(vplist03(1,:)),'k', 'DisplayName','\lambda_l=0.3')
% plot(fr(1,:),abs(vplist04(1,:)),'c', 'DisplayName','\lambda_l=0.4')
% plot(fr(1,:),abs(vplist05(1,:)),'r.-', 'DisplayName','\lambda_l=0.5')
% plot(fr(1,:),abs(vplist06(1,:)),'g.-', 'DisplayName','\lambda_l=0.6')
% plot(fr(1,:),abs(vplist07(1,:)),'b.-', 'DisplayName','\lambda_l=0.7')
% plot(fr(1,:),abs(vplist08(1,:)),'k.-', 'DisplayName','\lambda_l=0.8')
% plot(fr(1,:),abs(vplist09(1,:)),'c.-', 'DisplayName','\lambda_l=0.9')
% plot(fr(1,:),abs(vplist10(1,:)),'y', 'DisplayName','\lambda_l=1.0')
% set(gca,'XScale','log');
% set(gca,'YScale','log');
% xlabel('base excitation frequency');
% ylabel('output voltage amplitude');
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% set(gcf, 'color', 'w')
% legend('show')
% title('external electrical load R\_l = 1.0 \Omega')
% 
% 
% %% Rl  10 ohm, different laml
% figure(3)
% plot(fr(1,:),abs(vplist00(2,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
% plot(fr(1,:),abs(vplist01(2,:)),'g', 'DisplayName','\lambda_l=0.1')
% plot(fr(1,:),abs(vplist02(2,:)),'b', 'DisplayName','\lambda_l=0.2')
% plot(fr(1,:),abs(vplist03(2,:)),'k', 'DisplayName','\lambda_l=0.3')
% plot(fr(1,:),abs(vplist04(2,:)),'c', 'DisplayName','\lambda_l=0.4')
% plot(fr(1,:),abs(vplist05(2,:)),'r.-', 'DisplayName','\lambda_l=0.5')
% plot(fr(1,:),abs(vplist06(2,:)),'g.-', 'DisplayName','\lambda_l=0.6')
% plot(fr(1,:),abs(vplist07(2,:)),'b.-', 'DisplayName','\lambda_l=0.7')
% plot(fr(1,:),abs(vplist08(2,:)),'k.-', 'DisplayName','\lambda_l=0.8')
% plot(fr(1,:),abs(vplist09(2,:)),'c.-', 'DisplayName','\lambda_l=0.9')
% plot(fr(1,:),abs(vplist10(2,:)),'y', 'DisplayName','\lambda_l=1.0')
% set(gca,'XScale','log');
% set(gca,'YScale','log');
% xlabel('base excitation frequency');
% ylabel('output voltage amplitude');
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% set(gcf, 'color', 'w')
% legend('show')
% title('external electrical load R\_l = 10.0 \Omega')
% 
% 
% 
%% Rl  100 ohm, different laml
figure(4)
plot(fr(1,:),abs(vplist01(3,:)),'r', 'DisplayName','\rho_e=1.38e1'); hold on
plot(fr(1,:),abs(vplist02(3,:)),'m', 'DisplayName','\rho_e=1.38e2')
plot(fr(1,:),abs(vplist03(3,:)),'b', 'DisplayName','\rho_e=1.38e3')
plot(fr(1,:),abs(vplist04(3,:)),'k', 'DisplayName','\rho_e=1.38e4')
plot(fr(1,:),abs(vplist05(3,:)),'c', 'DisplayName','\rho_e=1.38e5')
% set(gca,'XScale','log');
% set(gca,'YScale','log');
xlim([1,100]);
xlabel('base excitation frequency');
ylabel('output voltage amplitude');
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
legend('show')
title('external electrical load R\_l = 100.0 \Omega')



