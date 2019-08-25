clc;clear;close all;

figure(1)
%% laml = 0.1, Rl from 1 ohm to 10 Mohm
% results0 = load('bm_ext_base_laml_0p1_Rl_1e0', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p1_Rl_1e1', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p1_Rl_1e2', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p1_Rl_1e3', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p1_Rl_1e4', 'Pplist'); 
% Pplist4 = results4.Pplist;
% results5 = load('bm_ext_base_laml_0p1_Rl_1e5', 'Pplist'); 
% Pplist5 = results5.Pplist;
% results6 = load('bm_ext_base_laml_0p1_Rl_1e6', 'Pplist'); 
% Pplist6 = results6.Pplist;
% results7 = load('bm_ext_base_laml_0p1_Rl_1e7', 'Pplist'); 
% Pplist7 = results7.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','Rl=1e0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','Rl=1e1'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','Rl=1e2'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','Rl=1e3'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','Rl=1e4'); 
% semilogy(frlist, abs(Pplist5)./wlist./wlist/xib, 'k', 'DisplayName','Rl=1e5'); 
% semilogy(frlist, abs(Pplist6)./wlist./wlist/xib, 'y.', 'DisplayName','Rl=1e6'); 
% semilogy(frlist, abs(Pplist7)./wlist./wlist/xib, 'm.', 'DisplayName','Rl=1e7'); 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio \lambda\_l = 0.1')
% set(gcf, 'color', 'w')
% legend('show')

%% laml = 0.2, Rl from 1 ohm to 10 Mohm
% results0 = load('bm_ext_base_laml_0p2_Rl_1e0', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p2_Rl_1e1', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p2_Rl_1e2', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p2_Rl_1e3', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p2_Rl_1e4', 'Pplist'); 
% Pplist4 = results4.Pplist;
% results5 = load('bm_ext_base_laml_0p2_Rl_1e5', 'Pplist'); 
% Pplist5 = results5.Pplist;
% results6 = load('bm_ext_base_laml_0p2_Rl_1e6', 'Pplist'); 
% Pplist6 = results6.Pplist;
% results7 = load('bm_ext_base_laml_0p2_Rl_1e7', 'Pplist'); 
% Pplist7 = results7.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','Rl=1e0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','Rl=1e1'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','Rl=1e2'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','Rl=1e3'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','Rl=1e4'); 
% semilogy(frlist, abs(Pplist5)./wlist./wlist/xib, 'k', 'DisplayName','Rl=1e5'); 
% semilogy(frlist, abs(Pplist6)./wlist./wlist/xib, 'y.', 'DisplayName','Rl=1e6'); 
% semilogy(frlist, abs(Pplist7)./wlist./wlist/xib, 'm.', 'DisplayName','Rl=1e7'); 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio \lambda\_l = 0.2')
% set(gcf, 'color', 'w')
% legend('show')

%% laml = 0.3, Rl from 1 ohm to 10 Mohm
% results0 = load('bm_ext_base_laml_0p3_Rl_1e0', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p3_Rl_1e1', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p3_Rl_1e2', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p3_Rl_1e3', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p3_Rl_1e4', 'Pplist'); 
% Pplist4 = results4.Pplist;
% results5 = load('bm_ext_base_laml_0p3_Rl_1e5', 'Pplist'); 
% Pplist5 = results5.Pplist;
% results6 = load('bm_ext_base_laml_0p3_Rl_1e6', 'Pplist'); 
% Pplist6 = results6.Pplist;
% results7 = load('bm_ext_base_laml_0p3_Rl_1e7', 'Pplist'); 
% Pplist7 = results7.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','Rl=1e0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','Rl=1e1'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','Rl=1e2'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','Rl=1e3'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','Rl=1e4'); 
% semilogy(frlist, abs(Pplist5)./wlist./wlist/xib, 'k', 'DisplayName','Rl=1e5'); 
% semilogy(frlist, abs(Pplist6)./wlist./wlist/xib, 'y.', 'DisplayName','Rl=1e6'); 
% semilogy(frlist, abs(Pplist7)./wlist./wlist/xib, 'm.', 'DisplayName','Rl=1e7'); 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio \lambda\_l = 0.3')
% set(gcf, 'color', 'w')
% legend('show')

%% laml = 0.4, Rl from 1 ohm to 10 Mohm
results0 = load('bm_ext_base_laml_0p4_Rl_1e0', 'Pplist', 'frlist', 'xib'); 
Pplist0 = results0.Pplist;
results1 = load('bm_ext_base_laml_0p4_Rl_1e1', 'Pplist'); 
Pplist1 = results1.Pplist;
results2 = load('bm_ext_base_laml_0p4_Rl_1e2', 'Pplist'); 
Pplist2 = results2.Pplist;
results3 = load('bm_ext_base_laml_0p4_Rl_1e3', 'Pplist'); 
Pplist3 = results3.Pplist;
results4 = load('bm_ext_base_laml_0p4_Rl_1e4', 'Pplist'); 
Pplist4 = results4.Pplist;
results5 = load('bm_ext_base_laml_0p4_Rl_1e5', 'Pplist'); 
Pplist5 = results5.Pplist;
results6 = load('bm_ext_base_laml_0p4_Rl_1e6', 'Pplist'); 
Pplist6 = results6.Pplist;
results7 = load('bm_ext_base_laml_0p4_Rl_1e7', 'Pplist'); 
Pplist7 = results7.Pplist;

frlist = results0.frlist;
wlist  = 2*pi*frlist;
xib  = results0.xib;

semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','Rl=1e0'); hold on
semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','Rl=1e1'); 
semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','Rl=1e2'); 
semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','Rl=1e3'); 
semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','Rl=1e4'); 
semilogy(frlist, abs(Pplist5)./wlist./wlist/xib, 'k', 'DisplayName','Rl=1e5'); 
semilogy(frlist, abs(Pplist6)./wlist./wlist/xib, 'y.', 'DisplayName','Rl=1e6'); 
semilogy(frlist, abs(Pplist7)./wlist./wlist/xib, 'm.', 'DisplayName','Rl=1e7'); 
% grid on
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
title('length ratio \lambda\_l = 0.4')
set(gcf, 'color', 'w')
legend('show')

%% laml = 0.5, Rl from 1 ohm to 10 Mohm
% results0 = load('bm_ext_base_laml_0p5_Rl_1e0', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p5_Rl_1e1', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p5_Rl_1e2', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p5_Rl_1e3', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p5_Rl_1e4', 'Pplist'); 
% Pplist4 = results4.Pplist;
% results5 = load('bm_ext_base_laml_0p5_Rl_1e5', 'Pplist'); 
% Pplist5 = results5.Pplist;
% results6 = load('bm_ext_base_laml_0p5_Rl_1e6', 'Pplist'); 
% Pplist6 = results6.Pplist;
% results7 = load('bm_ext_base_laml_0p5_Rl_1e7', 'Pplist'); 
% Pplist7 = results7.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','Rl=1e0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','Rl=1e1'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','Rl=1e2'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','Rl=1e3'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','Rl=1e4'); 
% semilogy(frlist, abs(Pplist5)./wlist./wlist/xib, 'k', 'DisplayName','Rl=1e5'); 
% semilogy(frlist, abs(Pplist6)./wlist./wlist/xib, 'y.', 'DisplayName','Rl=1e6'); 
% semilogy(frlist, abs(Pplist7)./wlist./wlist/xib, 'm.', 'DisplayName','Rl=1e7'); 
% grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio \lambda\_l = 0.5')
% set(gcf, 'color', 'w')
% legend('show')

%% laml = 0.8, Rl from 1 ohm to 10 Mohm
% results0 = load('bm_ext_base_laml_0p8_Rl_1e0', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p8_Rl_1e1', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p8_Rl_1e2', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p8_Rl_1e3', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p8_Rl_1e4', 'Pplist'); 
% Pplist4 = results4.Pplist;
% results5 = load('bm_ext_base_laml_0p8_Rl_1e5', 'Pplist'); 
% Pplist5 = results5.Pplist;
% results6 = load('bm_ext_base_laml_0p8_Rl_1e6', 'Pplist'); 
% Pplist6 = results6.Pplist;
% results7 = load('bm_ext_base_laml_0p8_Rl_1e7', 'Pplist'); 
% Pplist7 = results7.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','Rl=1e0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','Rl=1e1'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','Rl=1e2'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','Rl=1e3'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','Rl=1e4'); 
% semilogy(frlist, abs(Pplist5)./wlist./wlist/xib, 'k', 'DisplayName','Rl=1e5'); 
% semilogy(frlist, abs(Pplist6)./wlist./wlist/xib, 'y.', 'DisplayName','Rl=1e6'); 
% semilogy(frlist, abs(Pplist7)./wlist./wlist/xib, 'm.', 'DisplayName','Rl=1e7'); 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio \lambda\_l = 0.8')
% set(gcf, 'color', 'w')
% legend('show')

%% laml = 1.0, Rl from 1 ohm to 10 Mohm
% results0 = load('bm_ext_base_laml_1p0_Rl_1e0', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_1p0_Rl_1e1', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_1p0_Rl_1e2', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_1p0_Rl_1e3', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_1p0_Rl_1e4', 'Pplist'); 
% Pplist4 = results4.Pplist;
% results5 = load('bm_ext_base_laml_1p0_Rl_1e5', 'Pplist'); 
% Pplist5 = results5.Pplist;
% results6 = load('bm_ext_base_laml_1p0_Rl_1e6', 'Pplist'); 
% Pplist6 = results6.Pplist;
% results7 = load('bm_ext_base_laml_1p0_Rl_1e7', 'Pplist'); 
% Pplist7 = results7.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','Rl=1e0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','Rl=1e1'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','Rl=1e2'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','Rl=1e3'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','Rl=1e4'); 
% semilogy(frlist, abs(Pplist5)./wlist./wlist/xib, 'k', 'DisplayName','Rl=1e5'); 
% semilogy(frlist, abs(Pplist6)./wlist./wlist/xib, 'y.', 'DisplayName','Rl=1e6'); 
% semilogy(frlist, abs(Pplist7)./wlist./wlist/xib, 'm.', 'DisplayName','Rl=1e7'); 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio \lambda\_l = 1.0')
% set(gcf, 'color', 'w')
% legend('show')



figure(2)
%%  Rl = 1e0 ohm, laml from 0.10 to 1.0
results0 = load('bm_ext_base_laml_1p0_Rl_1e0', 'Pplist', 'frlist', 'xib'); 
Pplist0 = results0.Pplist;
results1 = load('bm_ext_base_laml_0p8_Rl_1e0', 'Pplist'); 
Pplist1 = results1.Pplist;
results2 = load('bm_ext_base_laml_0p5_Rl_1e0', 'Pplist'); 
Pplist2 = results2.Pplist;
results3 = load('bm_ext_base_laml_0p4_Rl_1e0', 'Pplist'); 
Pplist3 = results3.Pplist;
results4 = load('bm_ext_base_laml_0p3_Rl_1e0', 'Pplist'); 
Pplist4 = results4.Pplist;
results5 = load('bm_ext_base_laml_0p2_Rl_1e0', 'Pplist'); 
Pplist5 = results5.Pplist;
results6 = load('bm_ext_base_laml_0p1_Rl_1e0', 'Pplist'); 
Pplist6 = results6.Pplist;

frlist = results0.frlist;
wlist  = 2*pi*frlist;
xib  = results0.xib;

semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','\lambda_l=1.0'); hold on
semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','\lambda_l=0.8'); 
semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','\lambda_l=0.5'); 
semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','\lambda_l=0.4'); 
semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','\lambda_l=0.3'); 
semilogy(frlist, abs(Pplist5)./wlist./wlist/xib, 'k', 'DisplayName','\lambda_l=0.2'); 
semilogy(frlist, abs(Pplist6)./wlist./wlist/xib, 'y.', 'DisplayName','\lambda_l=0.1'); 

% grid on
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
title('connected load R\_l = 1.0e0 \Omega')
set(gcf, 'color', 'w')
legend('show')

%%  Rl = 1e1 ohm, laml from 0.10 to 1.0
% results0 = load('bm_ext_base_laml_1p0_Rl_1e1', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p8_Rl_1e1', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p5_Rl_1e1', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p2_Rl_1e1', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p1_Rl_1e1', 'Pplist'); 
% Pplist4 = results4.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','\lambda_l=1.0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','\lambda_l=0.8'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','\lambda_l=0.5'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','\lambda_l=0.2'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','\lambda_l=0.1'); 
% 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio R\_l = 1.0e1 \Omega')
% set(gcf, 'color', 'w')
% legend('show')

%%  Rl = 1e2 ohm, laml from 0.10 to 1.0
% results0 = load('bm_ext_base_laml_1p0_Rl_1e2', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p8_Rl_1e2', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p5_Rl_1e2', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p2_Rl_1e2', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p1_Rl_1e2', 'Pplist'); 
% Pplist4 = results4.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','\lambda_l=1.0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','\lambda_l=0.8'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','\lambda_l=0.5'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','\lambda_l=0.2'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','\lambda_l=0.1'); 
% 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio R\_l = 1.0e2 \Omega')
% set(gcf, 'color', 'w')
% legend('show')

%%  Rl = 1e3 ohm, laml from 0.10 to 1.0
% results0 = load('bm_ext_base_laml_1p0_Rl_1e3', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p8_Rl_1e3', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p5_Rl_1e3', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p2_Rl_1e3', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p1_Rl_1e3', 'Pplist'); 
% Pplist4 = results4.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','\lambda_l=1.0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','\lambda_l=0.8'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','\lambda_l=0.5'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','\lambda_l=0.2'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','\lambda_l=0.1'); 
% 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio R\_l = 1.0e3 \Omega')
% set(gcf, 'color', 'w')
% legend('show')

%%  Rl = 1e4 ohm, laml from 0.10 to 1.0
% results0 = load('bm_ext_base_laml_1p0_Rl_1e4', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p8_Rl_1e4', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p5_Rl_1e4', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p2_Rl_1e4', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p1_Rl_1e4', 'Pplist'); 
% Pplist4 = results4.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','\lambda_l=1.0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','\lambda_l=0.8'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','\lambda_l=0.5'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','\lambda_l=0.2'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','\lambda_l=0.1'); 
% 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio R\_l = 1.0e4 \Omega')
% set(gcf, 'color', 'w')
% legend('show')

%%  Rl = 1e5 ohm, laml from 0.10 to 1.0
% results0 = load('bm_ext_base_laml_1p0_Rl_1e5', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p8_Rl_1e5', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p5_Rl_1e5', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p2_Rl_1e5', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p1_Rl_1e5', 'Pplist'); 
% Pplist4 = results4.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','\lambda_l=1.0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','\lambda_l=0.8'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','\lambda_l=0.5'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','\lambda_l=0.2'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','\lambda_l=0.1'); 
% 
% grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio R\_l = 1.0e5 \Omega')
% set(gcf, 'color', 'w')
% legend('show')

%%  Rl = 1e6 ohm, laml from 0.10 to 1.0
% results0 = load('bm_ext_base_laml_1p0_Rl_1e6', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p8_Rl_1e6', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p5_Rl_1e6', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p2_Rl_1e6', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p1_Rl_1e6', 'Pplist'); 
% Pplist4 = results4.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','\lambda_l=1.0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','\lambda_l=0.8'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','\lambda_l=0.5'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','\lambda_l=0.2'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','\lambda_l=0.1'); 
% 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio R\_l = 1.0e6 \Omega')
% set(gcf, 'color', 'w')
% legend('show')

%%  Rl = 1e7 ohm, laml from 0.10 to 1.0
% results0 = load('bm_ext_base_laml_1p0_Rl_1e7', 'Pplist', 'frlist', 'xib'); 
% Pplist0 = results0.Pplist;
% results1 = load('bm_ext_base_laml_0p8_Rl_1e7', 'Pplist'); 
% Pplist1 = results1.Pplist;
% results2 = load('bm_ext_base_laml_0p5_Rl_1e7', 'Pplist'); 
% Pplist2 = results2.Pplist;
% results3 = load('bm_ext_base_laml_0p2_Rl_1e7', 'Pplist'); 
% Pplist3 = results3.Pplist;
% results4 = load('bm_ext_base_laml_0p1_Rl_1e7', 'Pplist'); 
% Pplist4 = results4.Pplist;
% 
% frlist = results0.frlist;
% wlist  = 2*pi*frlist;
% xib  = results0.xib;
% 
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r', 'DisplayName','\lambda_l=1.0'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g', 'DisplayName','\lambda_l=0.8'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b', 'DisplayName','\lambda_l=0.5'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm', 'DisplayName','\lambda_l=0.2'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c', 'DisplayName','\lambda_l=0.1'); 
% 
% % grid on
% set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
% title('length ratio R\_l = 1.0e7 \Omega')
% set(gcf, 'color', 'w')
% legend('show')

%% for phase angle
% figure(2)
% plot(frlist, angle(Pplist0)/pi*180, 'r'); hold on
% plot(frlist, angle(Pplist1)/pi*180, 'g'); 
% plot(frlist, angle(Pplist2)/pi*180, 'b'); 
% plot(frlist, angle(Pplist3)/pi*180, 'm'); 
% plot(frlist, angle(Pplist4)/pi*180, 'c'); 
% plot(frlist, angle(Pplist5)/pi*180, 'k'); 
% ylim([-180,180]);
% yTickLocations = linspace(-180, 180, 5);
% set(gca,'YTick', yTickLocations);
% grid on






