function bm_ext_base_lamB

xib  = 0.1e-3;
%% Rl 100 ohm
Rl   = 1.0e7;
frlist = logspace(0,3,600);
wlist  = 2*pi*frlist;
Vplist = zeros(size(frlist));
Iplist = zeros(size(frlist));
Pplist = zeros(size(frlist));
tic
for k = 1:length(frlist)
    [Vp, Ip, Pp] = bm_ext_eig(frlist(k), Rl);
    Vplist(k) = Vp;
    Iplist(k) = Ip;
    Pplist(k) = Pp;
end

% subplot(131); semilogy(frlist, abs(Vplist)./wlist./wlist/xib, 'r');hold on;
% subplot(132); semilogy(frlist, abs(Iplist)./wlist./wlist/xib, 'r');hold on;
% subplot(133); semilogy(frlist, abs(Pplist)./wlist./wlist/xib, 'r');hold on;
% semilogy(frlist, abs(Vplist)./wlist./wlist/xib, 'r')
% set(gca, 'linewidth', 1.1, 'fontsize', 16, 'fontname', 'times')


%% bending stiffness ratio Ye 4.3e9 Pa
save('bm_ext_base_lamB_Ye_4p3e9_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_4p3e9_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_4p3e9_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_4p3e9_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_4p3e9_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_4p3e9_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_4p3e9_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_4p3e9_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')


%% bending stiffness ratio Ye 3.3e9 Pa
% save('bm_ext_base_lamB_Ye_3p3e9_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_3p3e9_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_3p3e9_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_3p3e9_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_3p3e9_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_3p3e9_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_3p3e9_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_3p3e9_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')



%% bending stiffness ratio lamB 0.0055 Ye 2.3e9 Pa
% save('bm_ext_base_lamB_Ye_2p3e9_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_2p3e9_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_2p3e9_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_2p3e9_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_2p3e9_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_2p3e9_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_2p3e9_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_2p3e9_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')


%% bending stiffness ratio Ye 1.3e9 Pa
% save('bm_ext_base_lamB_Ye_1p3e9_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_1p3e9_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_1p3e9_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_1p3e9_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_1p3e9_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_1p3e9_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_1p3e9_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_1p3e9_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')


%% bending stiffness ratio Ye 0.3e9 Pa
% save('bm_ext_base_lamB_Ye_0p3e9_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_0p3e9_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_0p3e9_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_0p3e9_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_0p3e9_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_0p3e9_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_0p3e9_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_lamB_Ye_0p3e9_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')


toc

end