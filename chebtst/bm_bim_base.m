function bm_bim_base
clc;clear;
xib  = 0.1e-3;
%% Rl assignment and simulation results
Rl   = 1.0e3;
frlist = logspace(0,3,600);
wlist  = 2*pi*frlist;
Vplist = zeros(size(frlist));
Iplist = zeros(size(frlist));
Pplist = zeros(size(frlist));
tic
for k = 1:length(frlist)
    [Vp, Ip, Pp] = bm_bim_eig(frlist(k), Rl);
    Vplist(k) = Vp;
    Iplist(k) = Ip;
    Pplist(k) = Pp;
end

% subplot(131); semilogy(frlist, abs(Vplist)./wlist./wlist/xib, 'r');hold on;
% subplot(132); semilogy(frlist, abs(Iplist)./wlist./wlist/xib, 'r');hold on;
% subplot(133); semilogy(frlist, abs(Pplist)./wlist./wlist/xib, 'r');hold on;
% semilogy(frlist, abs(Vplist)./wlist./wlist/xib, 'r')
% set(gca, 'linewidth', 1.1, 'fontsize', 16, 'fontname', 'times')

%% Bimorph, different R_load, frequency sweep
% save('bm_bim_base_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_bim_base_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_bim_base_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_bim_base_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
save('bm_bim_base_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_bim_base_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_bim_base_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_bim_base_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')

toc

end