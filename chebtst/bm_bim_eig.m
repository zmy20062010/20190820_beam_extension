function [Vp, Ip, Pp] = bm_bim_eig(fr,Rl)

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
% fr   = 90;
% Rl   = 100.0e3;

xib  = 0.1e-3;
rd   = xib / lp;

%     structural, electrical, and piezoelectric parameters
Bp = 2.0/3.0 * b * ( Ys * hs^3.0 + Yp * ((hs + hp)^3.0 - hs^3.0) );
Cp = ep33S * b * lp / 2.0 / hp;
ep = b * e31 * (hs + hp/2.0);
mp = 2.0 * b * ( rhos * hs + rhop * hp );

alpha = ep * sqrt(lp / Cp / Bp);
beta  = Rl * Cp * sqrt(Bp / mp / lp^4.0 );
nu    = 2 * pi * fr * sqrt(mp * lp^4.0 / Bp);

A = chebop(0,1);
A.op = @(x,u) diff(u,4) - nu*nu*u;
A.lbc = @(u) [u-1; diff(u)];
A.rbc = @(u) [diff(u,2) + 1i*nu*beta/(1i*nu*beta+1)*alpha*alpha*diff(u); diff(u,3)];
u = A\0;

% x = 0:0.01:1;
% ux  = u(x);

% plot(x*lp, abs(u1x),'r', 'LineWidth', 2); hold on;
% plot(x*le+lp, abs(u2x),'b', 'LineWidth', 2);

Vp = 1i*nu*beta/(1i*nu*beta + 1) * ep / Cp * rd * feval(diff(u),1);
Ip = Vp / Rl;
Pp = Vp * Ip;

end