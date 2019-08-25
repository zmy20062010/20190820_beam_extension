% comparison of the constanst used in AUTO and chebfun

%% Parameters used in AUTO
% beam base structure material constants
lp   =  100.0e-3;
Ys   =  10.0e10;
rhos =  7.165e3;
hs   =  0.25e-3;
b    =  20.0e-3;
% piezo layer material constants
c11E = 66.0e9;
rhop = 7.80e3;
hp   = 0.2e-3;
ep33S= 15.93e-9;
e31  = -12.54;
% beam extension material constants
le   = 50e-3;
Ye   = 2.3e9;
rhoe = 1.38e3;
he   = 0.25e-3;
% external circuit and excitation
fr   = 120;
Rl   = 900.0e3;
% structural, electrical, and piezoelectric parameters
Bp = 2.0e0/3.0e0 * b * ( Ys * hs^3.0e0 ...
   + c11E * ( (hs + hp)^3.0e0 - hs^3.0e0) );
Be = 2.0e0/3.0e0 * b * Ye * he^3.0e0;
Cp = ep33S * b * lp / 2.0e0 / hp;
ep = b * e31 * (hs + hp/2.0e0);
mp = 2.0e0 * b * ( rhos * hs + rhop * hp );
me = 2.0e0 * b * rhoe * he;

alpha = ep * sqrt(lp / Cp / Bp);
beta  = Rl * Cp * sqrt(Bp / mp / lp^4.0e0);
nu    = 2 * pi * fr * sqrt(mp * lp^4.0e0 / Bp);
lamB  = Be / Bp;
lamm  = me / mp;
laml  = le / lp;

nuref = 2 * pi * sqrt(mp * lp^4.0e0 / Bp);
% nu1   = 7.87486e-1;
nu1   = 2.61379;
fr1   = nu1 / nuref

%% Parameters used in chebfun
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
fr   = 120;
Rl   = 900.0e3;
%     beam extension material constants
le   = 100e-3;
Ye   = 2.3e9;
rhoe = 1.38e3;
he   = 0.25e-3;

xib  = 0.1e-3;
rd   = xib/lp;
%     structural, electrical, and piezoelectric parameters
Bp = 2.0/3.0 * b * ( Ys * hs^3.0 + Yp * ((hs + hp)^3.0 - hs^3.0) );
Be = 2.0/3.0 * b * Ye * he^3.0;
Cp = ep33S * b * lp / 2.0 / hp;
ep = b * e31 * (hs + hp/2.0);
mp = 2.0 * b * ( rhos * hs + rhop * hp );
me = 2.0 * b * rhoe * he;

alpha = ep * sqrt(lp / Cp / Bp);
beta  = Rl * Cp * sqrt(Bp / mp / lp^4.0 );
nu    = 2 * pi * fr * sqrt(mp * lp^4.0 / Bp);
lamB  = Be / Bp;
lamm  = me / mp;
laml  = le / lp;