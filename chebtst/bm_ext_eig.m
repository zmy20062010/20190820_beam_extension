function [Vp, Ip, Pp] = bm_ext_eig(fr,Rl)
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
%     beam extension material constants
le   = 40e-3;
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
% lamB  = 0.005;
lamm  = me / mp;
laml  = le / lp;


A = chebop(0,1);
A.op = @(x, u1, u2) [diff(u1,4) - nu*nu*u1; diff(u2,4) - lamm*laml^4.0/lamB * nu*nu*u2;];
A.bc = @(x, u1, u2) [u1(0) - 1.0; 
                     feval(diff(u1), 0); 
                     u1(1) - u2(0); 
                     laml * feval(diff(u1), 1) - feval(diff(u2), 0);
                     feval(diff(u1,2), 1) + ...
                     1i*nu*beta/(1i*nu*beta+1) * alpha*alpha * feval(diff(u1), 1) - ...
                     lamB/laml/laml* feval(diff(u2,2), 0);
                     feval(diff(u1,3), 1) - lamB/laml^3.0 * feval(diff(u2,3), 0);
                     feval(diff(u2,2), 1);
                     feval(diff(u2,3), 1);
                     ];
[u1,u2] = A\0;
x = 0:0.01:1;

u1x  = u1(x);
u2x  = u2(x);
% plot(x*lp, abs(u1x),'r', 'LineWidth', 2); hold on;
% plot(x*le+lp, abs(u2x),'b', 'LineWidth', 2);

Vp = 1i*nu*beta/(1i*nu*beta + 1) * ep / Cp * rd * feval(diff(u1),1);
Ip = Vp / Rl;
Pp = Vp * Ip;
end