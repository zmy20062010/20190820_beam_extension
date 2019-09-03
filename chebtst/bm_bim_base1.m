function bm_bim_base1
clc;clear;close all;
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
        [Vp, Ip, Pp] = bm_bim_eig(fr(m,n), Rl(m,n));
        Vplist(m,n) = Vp;
        Iplist(m,n) = Ip;
        Pplist(m,n) = Pp;
    end
end
toc

%% bending stiffness ratio lamB 0.0055 Ye 2.3e9 Pa; le 30.0e-3 m; rhoe 1.38e3 kg/m^3; he 0.25e-3 m;

save('bm_ext_base_laml_l_00e-3','fr', 'Rl', 'Vplist', 'Iplist', 'Pplist', 'xib')



end