clc;clear;close all;

%% Bimorph, Rl from 1 ohm to 10 Mohm
results0 = load('bm_bim_base_Rl_1e0', 'Vplist', 'frlist', 'xib'); 
Vplist0 = results0.Vplist;
results1 = load('bm_bim_base_Rl_1e1', 'Vplist'); 
Vplist1 = results1.Vplist;
results2 = load('bm_bim_base_Rl_1e2', 'Vplist'); 
Vplist2 = results2.Vplist;
results3 = load('bm_bim_base_Rl_1e3', 'Vplist'); 
Vplist3 = results3.Vplist;
results4 = load('bm_bim_base_Rl_1e4', 'Vplist'); 
Vplist4 = results4.Vplist;
results5 = load('bm_bim_base_Rl_1e5', 'Vplist'); 
Vplist5 = results5.Vplist;
results6 = load('bm_bim_base_Rl_1e6', 'Vplist'); 
Vplist6 = results6.Vplist;
results7 = load('bm_bim_base_Rl_1e7', 'Vplist'); 
Vplist7 = results7.Vplist;

frlist = results0.frlist;
wlist  = 2*pi*frlist;
xib  = results0.xib;


%% plot voltage per acceleration versus frequency
figure(1)
semilogy(frlist, abs(Vplist0)./wlist./wlist/xib, 'r', 'DisplayName','Rl=1e0'); hold on
semilogy(frlist, abs(Vplist1)./wlist./wlist/xib, 'g', 'DisplayName','Rl=1e1'); 
semilogy(frlist, abs(Vplist2)./wlist./wlist/xib, 'b', 'DisplayName','Rl=1e2'); 
semilogy(frlist, abs(Vplist3)./wlist./wlist/xib, 'm', 'DisplayName','Rl=1e3'); 
semilogy(frlist, abs(Vplist4)./wlist./wlist/xib, 'c', 'DisplayName','Rl=1e4'); 
semilogy(frlist, abs(Vplist5)./wlist./wlist/xib, 'k', 'DisplayName','Rl=1e5'); 
semilogy(frlist, abs(Vplist6)./wlist./wlist/xib, 'y.', 'DisplayName','Rl=1e6'); 
% semilogy(frlist, abs(Vplist7)./wlist./wlist/xib, 'm.', 'DisplayName','Rl=1e7'); 
grid on
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
title('Unimorph, Rl from 1 ohm to 10 Mohm')
set(gcf, 'color', 'w')
legend('show')

figure(2)
%% plot voltage versus frequency
semilogy(frlist, abs(Vplist0), 'r', 'DisplayName','Rl=1e0'); hold on
semilogy(frlist, abs(Vplist1), 'g', 'DisplayName','Rl=1e1'); 
semilogy(frlist, abs(Vplist2), 'b', 'DisplayName','Rl=1e2'); 
semilogy(frlist, abs(Vplist3), 'm', 'DisplayName','Rl=1e3'); 
semilogy(frlist, abs(Vplist4), 'c', 'DisplayName','Rl=1e4'); 
semilogy(frlist, abs(Vplist5), 'k', 'DisplayName','Rl=1e5'); 
semilogy(frlist, abs(Vplist6), 'y.', 'DisplayName','Rl=1e6'); 
semilogy(frlist, abs(Vplist7), 'm.', 'DisplayName','Rl=1e7'); 
grid on
set(gca, 'linewidth', 1.1, 'fontsize', 12, 'fontname', 'times')
title('Unimorph, Rl from 1 ohm to 10 Mohm')
set(gcf, 'color', 'w')
legend('show')




