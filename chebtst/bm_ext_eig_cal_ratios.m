%     beam base structure material constants
lp   =  100.0e-3;
Ys   =  10.0e10;
rhos =  7.165e3;
hs   =  0.25e-3;
b    =  20.0e-3;
%     piezo layer material constants
Yp   = 66.0e9;
rhop = 7.80e3;
hp   = 0.2e-3;
ep33S= 15.93e-9;
d31  = -190e-12;
e31  = d31 * Yp;
%     external circuit and excitation
fr   = 90;
Rl   = 100.0e3;
%     beam extension material constants
le   = 30.0e-3;
Ye   = 0.01e9;
rhoe = 1.38e3;
he   = 0.25e-3;


Ye_list = [0.01e9, 0.02e9, 0.03e9, 0.04e9, 0.05e9,...
           0.06e9, 0.07e9, 0.08e9, 0.09e9, 0.1e9, ...
           0.2e9, 0.3e9, 1.3e9, 2.3e9, 3.3e9, ...
           4.3e9, 5.3e9, 6.3e9, 7.3e9, 8.3e9, ...
           9.3e9, 10.3e9, 20.3e9, 30.3e9, 40.3e9, ...
           50.3e9, 60.3e9, 70.3e9, 80.3e9, 90.3e9, ...
           100.3e9, 200.3e9, 300.3e9, 400.3e9];

rhoe_list = [1.38e1, 1.38e2, 1.38e3, 1.38e4, 1.38e5];
       
xib  = 0.1e-3;
rd   = xib / lp;

%     structural, electrical, and piezoelectric parameters
Bp = 2.0/3.0 * b * ( Ys * hs^3.0 + Yp * ((hs + hp)^3.0 - hs^3.0) );
Be = 2.0/3.0 * b * Ye * he^3.0;
Be_list = 2.0/3.0 * b * Ye_list * he^3.0;
Cp = ep33S * b * lp / 2.0 / hp;
ep = b * e31 * (hs + hp/2.0);
mp = 2.0 * b * ( rhos * hs + rhop * hp );
me = 2.0 * b * rhoe * he;
me_list = 2.0 * b * rhoe_list * he;

alpha = ep * sqrt(lp / Cp / Bp);
% alpha = -0.3329;
beta  = Rl * Cp * sqrt(Bp / mp / lp^4.0 );
% beta  = 0.6427;
nu    = 2 * pi * fr * sqrt(mp * lp^4.0 / Bp);
% nu    = 7.0083;
lamB  = Be / Bp;
lamB_list = Be_list / Bp;
% lamB  = 0.0055;
lamm  = me / mp;
lamm_list = me_list / mp;
% lamm  = 0.1029;
laml  = le / lp;
% laml  = 0.3000;
save('bm_ext_base_lamB_Ye_list','lamB_list','Be_list','Ye_list');
save('bm_ext_base_lamm_rhoe_list','lamm_list','me_list','rhoe_list');
