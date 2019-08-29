function bm_ext_base

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

%% length ratio 0.0
% save('bm_ext_base_laml_0p0_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p0_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p0_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p0_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p0_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p0_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p0_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p0_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
%% length ratio 0.1
% save('bm_ext_base_laml_0p1_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p1_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p1_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p1_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p1_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p1_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p1_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p1_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
%% length ratio 0.2
% save('bm_ext_base_laml_0p2_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p2_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p2_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p2_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p2_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p2_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p2_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p2_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
%% length ratio 0.3
% save('bm_ext_base_laml_0p3_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p3_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p3_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p3_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p3_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p3_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p3_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p3_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
%% length ratio 0.4
% save('bm_ext_base_laml_0p4_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p4_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p4_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p4_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p4_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p4_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p4_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p4_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
%% length ratio 0.5
% save('bm_ext_base_laml_0p5_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p5_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p5_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p5_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p5_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p5_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p5_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p5_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
%% length ratio 0.8
% save('bm_ext_base_laml_0p8_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p8_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p8_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p8_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p8_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p8_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p8_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_0p8_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')

%% length ratio 1.0
% save('bm_ext_base_laml_1p0_Rl_1e7','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_1p0_Rl_1e6','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_1p0_Rl_1e5','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_1p0_Rl_1e4','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_1p0_Rl_1e3','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_1p0_Rl_1e2','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_1p0_Rl_1e1','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')
% save('bm_ext_base_laml_1p0_Rl_1e0','frlist', 'Vplist', 'Iplist', 'Pplist', 'wlist', 'xib', 'Rl')







toc

end