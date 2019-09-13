function bm_ext_base_lamB

xib  = 0.1e-3;

Rle = [1.0e0, 1.0e1, 1.0e2, 1.0e3, 1.0e4, 1.0e5, 1.0e6, 1.0e7];
Fre = logspace(0,3,601);

[fr,Rl] = meshgrid(Fre,Rle);

Vplist = zeros(size(fr));
Iplist = zeros(size(fr));
Pplist = zeros(size(fr));

md = size(Rl,1);
nd = size(Rl,2);

tic
for m = 1:md
    for n = 1: nd
        [Vp, Ip, Pp] = bm_ext_eig_lamB(fr(m,n), Rl(m,n));
        Vplist(m,n) = Vp;
        Iplist(m,n) = Ip;
        Pplist(m,n) = Pp;
    end
end
toc

%% bending stiffness ratio lamB 0.0055 Ye 2.3e9 Pa; le 30.0e-3 m; rhoe 1.38e3 kg/m^3; he 0.25e-3 m;

% save('bm_ext_base_lamB_Ye_0p01e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_0p02e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_0p03e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_0p04e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_0p05e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_0p06e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_0p07e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_0p08e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_0p09e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_0p1e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
save('bm_ext_base_lamB_Ye_0p2e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_0p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_1p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_2p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_3p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_4p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_5p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_6p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_7p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_8p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_9p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_10p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_20p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_30p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_40p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_50p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_60p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_70p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_80p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_90p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_100p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_200p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_300p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_lamB_Ye_400p3e9','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')







end