clc;clear;
% beam base structure material constants
lp   =  50.0e-3;
Ys   =  10.8e10;
rhos =  8.8e3;
hs   =  0.25e-3;
b    =  20.0e-3;
% piezo layer material constants
c11E = 12.03e10;
rhop = 7.75e3;
hp   = 0.5e-3;
ep33S= 7.32e-9;
e31  = -5.35;
%  external circuit and excitation
fr   = 48;
Rl   = 900.0e3;


Bp = 2.0e0/3.0e0 * b * ( Ys * hs^3.0e0 + c11E * ((hs + hp)^3.0e0) - hs^3.0e0 );
Cp = ep33S * b * lp / 2.0e0 / hp;
ep = b * e31 * (hs + hp/2.0e0);
mp = 2.0e0 * b * ( rhos * hs + rhop * hp );

% dimensionless parameters
alpha = ep * np.sqrt(lp / Cp / Bp);
beta  = Rl * Cp * np.sqrt(Bp / mp / lp^4.0e0);
nu    = 2 * np.pi * fr * np.sqrt(mp * lp^4.0e0 / Bp);

eps = alpha*alpha;
sqlam = np.sqrt(nu);

xib = 0.5e-3;
rd = xib / lp;
rv = ep / Cp;


