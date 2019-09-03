function bm_ext_base_laml

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
parfor m = 1:md
    for n = 1: nd
        [Vp, Ip, Pp] = bm_ext_eig_laml(fr(m,n), Rl(m,n));
        Vplist(m,n) = Vp;
        Iplist(m,n) = Ip;
        Pplist(m,n) = Pp;
    end
end
toc

%% length ratio laml 0.3 Ye 2.3e9 Pa; le 30.0e-3 m; rhoe 1.38e3 kg/m^3; he 0.25e-3 m;

% save('bm_ext_base_laml_l_10e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_laml_l_20e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_laml_l_30e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_laml_l_40e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_laml_l_50e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_laml_l_60e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_laml_l_70e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_laml_l_80e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_laml_l_90e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')
% save('bm_ext_base_laml_l_100e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')







end