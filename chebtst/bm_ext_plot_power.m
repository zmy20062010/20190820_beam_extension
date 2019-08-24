clc;clear;
% frlist = logspace(0,2,400);
frlist = logspace(0,3,600);
wlist  = 2*pi*frlist;
xib  = 0.1e-3;

% results0 = load('bm_ext_base_laml_0p5_Rl_1e0', 'Pplist'); 
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

results0 = load('bm_ext_base_laml_0p1_Rl_1e0', 'Pplist'); 
Pplist0 = results0.Pplist;
results1 = load('bm_ext_base_laml_0p1_Rl_1e1', 'Pplist'); 
Pplist1 = results1.Pplist;
results2 = load('bm_ext_base_laml_0p1_Rl_1e2', 'Pplist'); 
Pplist2 = results2.Pplist;
results3 = load('bm_ext_base_laml_0p1_Rl_1e3', 'Pplist'); 
Pplist3 = results3.Pplist;
results4 = load('bm_ext_base_laml_0p1_Rl_1e4', 'Pplist'); 
Pplist4 = results4.Pplist;
results5 = load('bm_ext_base_laml_0p1_Rl_1e5', 'Pplist'); 
Pplist5 = results5.Pplist;
results6 = load('bm_ext_base_laml_0p1_Rl_1e6', 'Pplist'); 
Pplist6 = results6.Pplist;
results7 = load('bm_ext_base_laml_0p1_Rl_1e7', 'Pplist'); 
Pplist7 = results7.Pplist;

figure(1)
% semilogy(frlist, abs(Pplist0)./wlist./wlist/xib, 'r'); hold on
% semilogy(frlist, abs(Pplist1)./wlist./wlist/xib, 'g'); 
% semilogy(frlist, abs(Pplist2)./wlist./wlist/xib, 'b'); 
% semilogy(frlist, abs(Pplist3)./wlist./wlist/xib, 'm'); 
% semilogy(frlist, abs(Pplist4)./wlist./wlist/xib, 'c'); 
% semilogy(frlist, abs(Pplist5)./wlist./wlist/xib, 'k'); 

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
set(gcf, 'color', 'w')
legend('show')






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
