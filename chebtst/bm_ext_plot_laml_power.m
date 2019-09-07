clc;clear;close all;



result00 = load('bm_ext_base_laml_l_00e-3.mat'); 
Pplist00  = result00.Pplist;
result01 = load('bm_ext_base_laml_l_10e-3.mat'); 
Pplist01  = result01.Pplist;
result02 = load('bm_ext_base_laml_l_20e-3.mat'); 
Pplist02  = result02.Pplist;
result03 = load('bm_ext_base_laml_l_30e-3.mat'); 
Pplist03  = result03.Pplist;
result04 = load('bm_ext_base_laml_l_40e-3.mat'); 
Pplist04  = result04.Pplist;
result05 = load('bm_ext_base_laml_l_50e-3.mat'); 
Pplist05  = result05.Pplist;
result06 = load('bm_ext_base_laml_l_60e-3.mat'); 
Pplist06  = result06.Pplist;
result07 = load('bm_ext_base_laml_l_70e-3.mat');
Pplist07  = result07.Pplist;
result08 = load('bm_ext_base_laml_l_80e-3.mat'); 
Pplist08  = result08.Pplist;
result09 = load('bm_ext_base_laml_l_90e-3.mat'); 
Pplist09  = result09.Pplist;
result10 = load('bm_ext_base_laml_l_100e-3.mat'); 
Pplist10  = result10.Pplist;

fr = result00.fr;
Rl = result00.Rl;
xib  = result00.xib;

%% Rl from 1 ohm to 10 Mohm, different laml
f = figure(1);
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')
colormap lines
subplot(231)
mesh(fr,Rl,abs(Pplist00), 'DisplayName','\lambda_l=0.0')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');
subplot(232)
mesh(fr,Rl,abs(Pplist02), 'DisplayName','\lambda_l=0.2')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');
subplot(233)
mesh(fr,Rl,abs(Pplist04), 'DisplayName','\lambda_l=0.4')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');
subplot(234)
mesh(fr,Rl,abs(Pplist06), 'DisplayName','\lambda_l=0.6')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');
subplot(235)
mesh(fr,Rl,abs(Pplist08), 'DisplayName','\lambda_l=0.8')
set(gca,'XScale','log');
set(gca,'YScale','log');
set(gca,'ZScale','log');
subplot(236)
mesh(fr,Rl,abs(Pplist10), 'DisplayName','\lambda_l=1.0')
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
% plot(fr(1,:),abs(Pplist00(1,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
% plot(fr(1,:),abs(Pplist01(1,:)),'g', 'DisplayName','\lambda_l=0.1')
% plot(fr(1,:),abs(Pplist02(1,:)),'b', 'DisplayName','\lambda_l=0.2')
% plot(fr(1,:),abs(Pplist03(1,:)),'k', 'DisplayName','\lambda_l=0.3')
% plot(fr(1,:),abs(Pplist04(1,:)),'c', 'DisplayName','\lambda_l=0.4')
% plot(fr(1,:),abs(Pplist05(1,:)),'r.-', 'DisplayName','\lambda_l=0.5')
% plot(fr(1,:),abs(Pplist06(1,:)),'g.-', 'DisplayName','\lambda_l=0.6')
% plot(fr(1,:),abs(Pplist07(1,:)),'b.-', 'DisplayName','\lambda_l=0.7')
% plot(fr(1,:),abs(Pplist08(1,:)),'k.-', 'DisplayName','\lambda_l=0.8')
% plot(fr(1,:),abs(Pplist09(1,:)),'c.-', 'DisplayName','\lambda_l=0.9')
% plot(fr(1,:),abs(Pplist10(1,:)),'y', 'DisplayName','\lambda_l=1.0')
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
% plot(fr(1,:),abs(Pplist00(2,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
% plot(fr(1,:),abs(Pplist01(2,:)),'g', 'DisplayName','\lambda_l=0.1')
% plot(fr(1,:),abs(Pplist02(2,:)),'b', 'DisplayName','\lambda_l=0.2')
% plot(fr(1,:),abs(Pplist03(2,:)),'k', 'DisplayName','\lambda_l=0.3')
% plot(fr(1,:),abs(Pplist04(2,:)),'c', 'DisplayName','\lambda_l=0.4')
% plot(fr(1,:),abs(Pplist05(2,:)),'r.-', 'DisplayName','\lambda_l=0.5')
% plot(fr(1,:),abs(Pplist06(2,:)),'g.-', 'DisplayName','\lambda_l=0.6')
% plot(fr(1,:),abs(Pplist07(2,:)),'b.-', 'DisplayName','\lambda_l=0.7')
% plot(fr(1,:),abs(Pplist08(2,:)),'k.-', 'DisplayName','\lambda_l=0.8')
% plot(fr(1,:),abs(Pplist09(2,:)),'c.-', 'DisplayName','\lambda_l=0.9')
% plot(fr(1,:),abs(Pplist10(2,:)),'y', 'DisplayName','\lambda_l=1.0')
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
% plot(fr(1,:),abs(Pplist00(3,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
% plot(fr(1,:),abs(Pplist01(3,:)),'g', 'DisplayName','\lambda_l=0.1')
% plot(fr(1,:),abs(Pplist02(3,:)),'b', 'DisplayName','\lambda_l=0.2')
% plot(fr(1,:),abs(Pplist03(3,:)),'k', 'DisplayName','\lambda_l=0.3')
% plot(fr(1,:),abs(Pplist04(3,:)),'c', 'DisplayName','\lambda_l=0.4')
% plot(fr(1,:),abs(Pplist05(3,:)),'r.-', 'DisplayName','\lambda_l=0.5')
% plot(fr(1,:),abs(Pplist06(3,:)),'g.-', 'DisplayName','\lambda_l=0.6')
% plot(fr(1,:),abs(Pplist07(3,:)),'b.-', 'DisplayName','\lambda_l=0.7')
% plot(fr(1,:),abs(Pplist08(3,:)),'k.-', 'DisplayName','\lambda_l=0.8')
% plot(fr(1,:),abs(Pplist09(3,:)),'c.-', 'DisplayName','\lambda_l=0.9')
% plot(fr(1,:),abs(Pplist10(3,:)),'y', 'DisplayName','\lambda_l=1.0')
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
% figure(8)
% plot(fr(1,:),abs(Pplist00(7,:)),'r', 'DisplayName','\lambda_l=0.0'); hold on
% plot(fr(1,:),abs(Pplist01(7,:)),'g', 'DisplayName','\lambda_l=0.1')
% plot(fr(1,:),abs(Pplist02(7,:)),'b', 'DisplayName','\lambda_l=0.2')
% plot(fr(1,:),abs(Pplist03(7,:)),'k', 'DisplayName','\lambda_l=0.3')
% plot(fr(1,:),abs(Pplist04(7,:)),'c', 'DisplayName','\lambda_l=0.4')
% plot(fr(1,:),abs(Pplist05(7,:)),'r.-', 'DisplayName','\lambda_l=0.5')
% plot(fr(1,:),abs(Pplist06(7,:)),'g.-', 'DisplayName','\lambda_l=0.6')
% plot(fr(1,:),abs(Pplist07(7,:)),'b.-', 'DisplayName','\lambda_l=0.7')
% plot(fr(1,:),abs(Pplist08(7,:)),'k.-', 'DisplayName','\lambda_l=0.8')
% plot(fr(1,:),abs(Pplist09(7,:)),'c.-', 'DisplayName','\lambda_l=0.9')
% plot(fr(1,:),abs(Pplist10(7,:)),'y', 'DisplayName','\lambda_l=1.0')
% % set(gca,'XScale','log');
% set(gca,'YScale','log');
% xlim([1,100]);
% xlabel('base excitation frequency');
% ylabel('output voltage amplitude');
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% set(gcf, 'color', 'w')
% legend('show')
% title('external electrical load R\_l = 1000000.0 \Omega')

