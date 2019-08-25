clc;clear;
% frlist = logspace(0,2,400);
frlist = logspace(0,3,600);
wlist  = 2*pi*frlist;
xib  = 0.1e-3;

% results0 = load('bm_ext_base_laml_0p5_Rl_1e0', 'Vplist'); 
% Vplist0 = results0.Vplist;
% results1 = load('bm_ext_base_laml_0p5_Rl_1e1', 'Vplist'); 
% Vplist1 = results1.Vplist;
% results2 = load('bm_ext_base_laml_0p5_Rl_1e2', 'Vplist'); 
% Vplist2 = results2.Vplist;
% results3 = load('bm_ext_base_laml_0p5_Rl_1e3', 'Vplist'); 
% Vplist3 = results3.Vplist;
% results4 = load('bm_ext_base_laml_0p5_Rl_1e4', 'Vplist'); 
% Vplist4 = results4.Vplist;
% results5 = load('bm_ext_base_laml_0p5_Rl_1e5', 'Vplist'); 
% Vplist5 = results5.Vplist;

results0 = load('bm_ext_base_laml_0p1_Rl_1e0', 'Vplist'); 
Vplist0 = results0.Vplist;
results1 = load('bm_ext_base_laml_0p1_Rl_1e1', 'Vplist'); 
Vplist1 = results1.Vplist;
results2 = load('bm_ext_base_laml_0p1_Rl_1e2', 'Vplist'); 
Vplist2 = results2.Vplist;
results3 = load('bm_ext_base_laml_0p1_Rl_1e3', 'Vplist'); 
Vplist3 = results3.Vplist;
results4 = load('bm_ext_base_laml_0p1_Rl_1e4', 'Vplist'); 
Vplist4 = results4.Vplist;
results5 = load('bm_ext_base_laml_0p1_Rl_1e5', 'Vplist'); 
Vplist5 = results5.Vplist;
results6 = load('bm_ext_base_laml_0p1_Rl_1e6', 'Vplist'); 
Vplist6 = results6.Vplist;
results7 = load('bm_ext_base_laml_0p1_Rl_1e7', 'Vplist'); 
Vplist7 = results7.Vplist;

figure(1)
% semilogy(frlist, abs(Vplist0)./wlist./wlist/xib, 'r'); hold on
% semilogy(frlist, abs(Vplist1)./wlist./wlist/xib, 'g'); 
% semilogy(frlist, abs(Vplist2)./wlist./wlist/xib, 'b'); 
% semilogy(frlist, abs(Vplist3)./wlist./wlist/xib, 'm'); 
% semilogy(frlist, abs(Vplist4)./wlist./wlist/xib, 'c'); 
% semilogy(frlist, abs(Vplist5)./wlist./wlist/xib, 'k'); 

semilogy(frlist, abs(Vplist0)./wlist./wlist/xib, 'r'); hold on
semilogy(frlist, abs(Vplist1)./wlist./wlist/xib, 'g'); 
semilogy(frlist, abs(Vplist2)./wlist./wlist/xib, 'b'); 
semilogy(frlist, abs(Vplist3)./wlist./wlist/xib, 'm'); 
semilogy(frlist, abs(Vplist4)./wlist./wlist/xib, 'c'); 
semilogy(frlist, abs(Vplist5)./wlist./wlist/xib, 'k'); 
semilogy(frlist, abs(Vplist6)./wlist./wlist/xib, 'y.'); 
semilogy(frlist, abs(Vplist7)./wlist./wlist/xib, 'm.'); 
% grid on
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
set(gcf, 'color', 'w')






% figure(2)
% plot(frlist, angle(Vplist0)/pi*180, 'r'); hold on
% plot(frlist, angle(Vplist1)/pi*180, 'g'); 
% plot(frlist, angle(Vplist2)/pi*180, 'b'); 
% plot(frlist, angle(Vplist3)/pi*180, 'm'); 
% plot(frlist, angle(Vplist4)/pi*180, 'c'); 
% plot(frlist, angle(Vplist5)/pi*180, 'k'); 
% ylim([-180,180]);
% yTickLocations = linspace(-180, 180, 5);
% set(gca,'YTick', yTickLocations);
% grid on
