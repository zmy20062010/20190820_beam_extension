clc;clear;close all;



result00 = load('bm_ext_base_laml_l_00e-3.mat'); 
vplist00  = result00.Vplist;
result01 = load('bm_ext_base_laml_l_10e-3.mat'); 
vplist01  = result01.Vplist;
result02 = load('bm_ext_base_laml_l_20e-3.mat'); 
vplist02  = result02.Vplist;
result03 = load('bm_ext_base_laml_l_30e-3.mat'); 
vplist03  = result03.Vplist;
result04 = load('bm_ext_base_laml_l_40e-3.mat'); 
vplist04  = result04.Vplist;
result05 = load('bm_ext_base_laml_l_50e-3.mat'); 
vplist05  = result05.Vplist;
result06 = load('bm_ext_base_laml_l_60e-3.mat'); 
vplist06  = result06.Vplist;
result07 = load('bm_ext_base_laml_l_70e-3.mat');
vplist07  = result07.Vplist;
result08 = load('bm_ext_base_laml_l_80e-3.mat'); 
vplist08  = result08.Vplist;
result09 = load('bm_ext_base_laml_l_90e-3.mat'); 
vplist09  = result09.Vplist;
result10 = load('bm_ext_base_laml_l_100e-3.mat'); 
vplist10  = result10.Vplist;

fr = result00.fr;
Rl = result00.Rl;
xib  = result00.xib;

%% Rl from 1 ohm to 10 Mohm, different laml
f = figure(1);
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
colormap pink
subplot(231)
mesh(fr,Rl,abs(vplist00), 'DisplayName','\lambda_l=0.0')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');
subplot(232)
surf(fr,Rl,abs(vplist02), 'DisplayName','\lambda_l=0.2')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');
subplot(233)
surf(fr,Rl,abs(vplist04), 'DisplayName','\lambda_l=0.4')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');
subplot(234)
surf(fr,Rl,abs(vplist06), 'DisplayName','\lambda_l=0.6')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');
subplot(235)
surf(fr,Rl,abs(vplist08), 'DisplayName','\lambda_l=0.8')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');
subplot(236)
surf(fr,Rl,abs(vplist10), 'DisplayName','\lambda_l=1.0')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');


% legend('show')

% ax = findobj(f,'Type','Axes');
% for i=1:length(ax)
%     ylabel(ax(i),{'Nice'})
%     title(ax(i),{'Very Nice'})
% end




% title('Output voltage amplitude at different frequency and load')
% print(gcf,'fig_output_voltage_vs_fr_Rl_laml_all','-dpdf');
% print(gcf,'fig_output_voltage_vs_fr_Rl_laml_all','-depsc');
% print(gcf,'fig_output_voltage_vs_fr_Rl_laml_all','-djpeg','-r300','-noui');      

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
% %% Rl  100 ohm, different laml
% figure(4)
% plot(fr(1,:),abs(vplist00(3,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
% plot(fr(1,:),abs(vplist01(3,:)),'g', 'DisplayName','\lambda_l=0.1')
% plot(fr(1,:),abs(vplist02(3,:)),'b', 'DisplayName','\lambda_l=0.2')
% plot(fr(1,:),abs(vplist03(3,:)),'k', 'DisplayName','\lambda_l=0.3')
% plot(fr(1,:),abs(vplist04(3,:)),'c', 'DisplayName','\lambda_l=0.4')
% plot(fr(1,:),abs(vplist05(3,:)),'r.-', 'DisplayName','\lambda_l=0.5')
% plot(fr(1,:),abs(vplist06(3,:)),'g.-', 'DisplayName','\lambda_l=0.6')
% plot(fr(1,:),abs(vplist07(3,:)),'b.-', 'DisplayName','\lambda_l=0.7')
% plot(fr(1,:),abs(vplist08(3,:)),'k.-', 'DisplayName','\lambda_l=0.8')
% plot(fr(1,:),abs(vplist09(3,:)),'c.-', 'DisplayName','\lambda_l=0.9')
% plot(fr(1,:),abs(vplist10(3,:)),'y', 'DisplayName','\lambda_l=1.0')
% % set(gca,'XScale','log');
% % set(gca,'YScale','log');
% xlim([1,100]);
% xlabel('base excitation frequency');
% ylabel('output voltage amplitude');
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% set(gcf, 'color', 'w')
% legend('show')
% title('external electrical load R\_l = 100.0 \Omega')




%% Rl  1000000 ohm, different laml
figure(8)
plot(fr(1,:),abs(vplist00(7,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
plot(fr(1,:),abs(vplist01(7,:)),'g', 'DisplayName','\lambda_l=0.1')
plot(fr(1,:),abs(vplist02(7,:)),'b', 'DisplayName','\lambda_l=0.2')
plot(fr(1,:),abs(vplist03(7,:)),'k', 'DisplayName','\lambda_l=0.3')
plot(fr(1,:),abs(vplist04(7,:)),'c', 'DisplayName','\lambda_l=0.4')
plot(fr(1,:),abs(vplist05(7,:)),'r.-', 'DisplayName','\lambda_l=0.5')
plot(fr(1,:),abs(vplist06(7,:)),'g.-', 'DisplayName','\lambda_l=0.6')
plot(fr(1,:),abs(vplist07(7,:)),'b.-', 'DisplayName','\lambda_l=0.7')
plot(fr(1,:),abs(vplist08(7,:)),'k.-', 'DisplayName','\lambda_l=0.8')
plot(fr(1,:),abs(vplist09(7,:)),'c.-', 'DisplayName','\lambda_l=0.9')
plot(fr(1,:),abs(vplist10(7,:)),'y', 'DisplayName','\lambda_l=1.0')
% set(gca,'XScale','log');
set(gca,'YScale','log');
xlim([1,100]);
xlabel('base excitation frequency');
ylabel('output voltage amplitude');
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
legend('show')
title('external electrical load R\_l = 1000000.0 \Omega')

