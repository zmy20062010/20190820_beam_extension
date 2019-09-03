clc;clear;close all;



result00 = load('bm_ext_base_laml_l_00e-3.mat'); 
pplist00  = result00.Pplist;
result01 = load('bm_ext_base_laml_l_10e-3.mat'); 
pplist01  = result01.Pplist;
result02 = load('bm_ext_base_laml_l_20e-3.mat'); 
pplist02  = result02.Pplist;
result03 = load('bm_ext_base_laml_l_30e-3.mat'); 
pplist03  = result03.Pplist;
result04 = load('bm_ext_base_laml_l_40e-3.mat'); 
pplist04  = result04.Pplist;
result05 = load('bm_ext_base_laml_l_50e-3.mat'); 
pplist05  = result05.Pplist;
result06 = load('bm_ext_base_laml_l_60e-3.mat'); 
pplist06  = result06.Pplist;
result07 = load('bm_ext_base_laml_l_70e-3.mat');
pplist07  = result07.Pplist;
result08 = load('bm_ext_base_laml_l_80e-3.mat'); 
pplist08  = result08.Pplist;
result09 = load('bm_ext_base_laml_l_90e-3.mat'); 
pplist09  = result09.Pplist;
result10 = load('bm_ext_base_laml_l_100e-3.mat'); 
pplist10  = result10.Pplist;

fr = result00.fr;
Rl = result00.Rl;
xib  = result00.xib;

%% Rl from 1 ohm to 10 Mohm, different laml
% figure(1)
% mesh(fr,Rl,abs(pplist00), 'DisplayName','\lambda_l=0.0'); hold on
% mesh(fr,Rl,abs(pplist01), 'DisplayName','\lambda_l=0.1')
% mesh(fr,Rl,abs(pplist02), 'DisplayName','\lambda_l=0.2')
% mesh(fr,Rl,abs(pplist03), 'DisplayName','\lambda_l=0.3')
% mesh(fr,Rl,abs(pplist04), 'DisplayName','\lambda_l=0.4')
% mesh(fr,Rl,abs(pplist05), 'DisplayName','\lambda_l=0.5')
% mesh(fr,Rl,abs(pplist06), 'DisplayName','\lambda_l=0.6')
% mesh(fr,Rl,abs(pplist07), 'DisplayName','\lambda_l=0.7')
% mesh(fr,Rl,abs(pplist08), 'DisplayName','\lambda_l=0.8')
% mesh(fr,Rl,abs(pplist09), 'DisplayName','\lambda_l=0.9')
% surf(fr,Rl,abs(pplist10), 'DisplayName','\lambda_l=1.0')
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
plot(fr(1,:),abs(pplist00(1,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
plot(fr(1,:),abs(pplist01(1,:)),'g', 'DisplayName','\lambda_l=0.1')
plot(fr(1,:),abs(pplist02(1,:)),'b', 'DisplayName','\lambda_l=0.2')
plot(fr(1,:),abs(pplist03(1,:)),'k', 'DisplayName','\lambda_l=0.3')
plot(fr(1,:),abs(pplist04(1,:)),'c', 'DisplayName','\lambda_l=0.4')
plot(fr(1,:),abs(pplist05(1,:)),'r.-', 'DisplayName','\lambda_l=0.5')
plot(fr(1,:),abs(pplist06(1,:)),'g.-', 'DisplayName','\lambda_l=0.6')
plot(fr(1,:),abs(pplist07(1,:)),'b.-', 'DisplayName','\lambda_l=0.7')
plot(fr(1,:),abs(pplist08(1,:)),'k.-', 'DisplayName','\lambda_l=0.8')
plot(fr(1,:),abs(pplist09(1,:)),'c.-', 'DisplayName','\lambda_l=0.9')
plot(fr(1,:),abs(pplist10(1,:)),'y', 'DisplayName','\lambda_l=1.0')
set(gca,'XScale','log');
set(gca,'YScale','log');
xlabel('base excitation frequency');
ylabel('output voltage amplitude');
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
legend('show')
title('external electrical load R\_l = 1.0 \Omega')


%% Rl  10 ohm, different laml
figure(3)
plot(fr(1,:),abs(pplist00(2,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
plot(fr(1,:),abs(pplist01(2,:)),'g', 'DisplayName','\lambda_l=0.1')
plot(fr(1,:),abs(pplist02(2,:)),'b', 'DisplayName','\lambda_l=0.2')
plot(fr(1,:),abs(pplist03(2,:)),'k', 'DisplayName','\lambda_l=0.3')
plot(fr(1,:),abs(pplist04(2,:)),'c', 'DisplayName','\lambda_l=0.4')
plot(fr(1,:),abs(pplist05(2,:)),'r.-', 'DisplayName','\lambda_l=0.5')
plot(fr(1,:),abs(pplist06(2,:)),'g.-', 'DisplayName','\lambda_l=0.6')
plot(fr(1,:),abs(pplist07(2,:)),'b.-', 'DisplayName','\lambda_l=0.7')
plot(fr(1,:),abs(pplist08(2,:)),'k.-', 'DisplayName','\lambda_l=0.8')
plot(fr(1,:),abs(pplist09(2,:)),'c.-', 'DisplayName','\lambda_l=0.9')
plot(fr(1,:),abs(pplist10(2,:)),'y', 'DisplayName','\lambda_l=1.0')
set(gca,'XScale','log');
set(gca,'YScale','log');
xlabel('base excitation frequency');
ylabel('output voltage amplitude');
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
legend('show')
title('external electrical load R\_l = 10.0 \Omega')



%% Rl  100 ohm, different laml
figure(4)
plot(fr(1,:),abs(pplist00(3,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
plot(fr(1,:),abs(pplist01(3,:)),'g', 'DisplayName','\lambda_l=0.1')
plot(fr(1,:),abs(pplist02(3,:)),'b', 'DisplayName','\lambda_l=0.2')
plot(fr(1,:),abs(pplist03(3,:)),'k', 'DisplayName','\lambda_l=0.3')
plot(fr(1,:),abs(pplist04(3,:)),'c', 'DisplayName','\lambda_l=0.4')
plot(fr(1,:),abs(pplist05(3,:)),'r.-', 'DisplayName','\lambda_l=0.5')
plot(fr(1,:),abs(pplist06(3,:)),'g.-', 'DisplayName','\lambda_l=0.6')
plot(fr(1,:),abs(pplist07(3,:)),'b.-', 'DisplayName','\lambda_l=0.7')
plot(fr(1,:),abs(pplist08(3,:)),'k.-', 'DisplayName','\lambda_l=0.8')
plot(fr(1,:),abs(pplist09(3,:)),'c.-', 'DisplayName','\lambda_l=0.9')
plot(fr(1,:),abs(pplist10(3,:)),'y', 'DisplayName','\lambda_l=1.0')
% set(gca,'XScale','log');
% set(gca,'YScale','log');
xlim([1,100]);
xlabel('base excitation frequency');
ylabel('output voltage amplitude');
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
legend('show')
title('external electrical load R\_l = 100.0 \Omega')



