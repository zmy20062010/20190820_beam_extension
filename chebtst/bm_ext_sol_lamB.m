% function bm_ext_sol_lamB
% This piece of code serves to provide 

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
fr   = 10;
Rl   = 1.0e4;
%     beam extension material constants
le   = 100.0e-3;
Ye   = 80.0e9;
rhoe = 1.38e3;
he   = 0.25e-3;

xib  = 0.1e-3;
rd   = xib / lp;

%     structural, electrical, and piezoelectric parameters
Bp = 2.0/3.0 * b * ( Ys * hs^3.0 + Yp * ((hs + hp)^3.0 - hs^3.0) );
Be = 2.0/3.0 * b * Ye * he^3.0;
Cp = ep33S * b * lp / 2.0 / hp;
ep = b * e31 * (hs + hp/2.0);
mp = 2.0 * b * ( rhos * hs + rhop * hp );
me = 2.0 * b * rhoe * he;

alpha = ep * sqrt(lp / Cp / Bp);
% alpha = -0.3329;
beta  = Rl * Cp * sqrt(Bp / mp / lp^4.0 );
% beta  = 0.6427;
nu    = 2 * pi * fr * sqrt(mp * lp^4.0 / Bp);
% nu    = 7.0083;
lamB  = Be / Bp;
% lamB  = 0.0055;
lamm  = me / mp;
% lamm  = 0.1029;
laml  = le / lp;
% laml  = 0.3000;

A = chebop(0,1);
A.op = @(x, u1, u2) [diff(u1,4) - nu*nu*u1; lamB * diff(u2,4) - lamm*laml^4.0 * nu*nu*u2;];
A.bc = @(x, u1, u2) [u1(0) - 1.0; 
                     feval(diff(u1), 0); 
                     u1(1) - u2(0); 
                     laml * feval(diff(u1), 1) - feval(diff(u2), 0);
                     feval(diff(u1,2), 1) + ...
                     1i*nu*beta /(1i*nu*beta+1) * alpha*alpha * laml*laml * feval(diff(u1), 1) - ...
                     lamB * feval(diff(u2,2), 0);
                     laml^3.0 * feval(diff(u1,3), 1) - lamB * feval(diff(u2,3), 0);
                     feval(diff(u2,2), 1);
                     feval(diff(u2,3), 1);
                     ];
[u1,u2] = A\0;

x = 0:0.01:1;
u1f = feval(u1,x);
u2f = feval(u2,x);

xall = [x*lp, le*x + lp];
uall = [u1f, u2f];

% subplot(121)
% plot(x*lp, abs(2-u1f), 'b-'); hold on
% plot(le*x + lp, abs(2-u2f), 'r--')

plot(x*lp, abs(u1f), 'b-'); hold on
plot(le*x + lp, abs(u2f), 'r--')


% subplot(122)
% plot(x*lp, abs(2-u1f), 'b-'); hold on
% plot(le*x + lp, abs(2-u2f), 'r--')

% plot(x*lp, angle(u1f)/pi*180, 'b-'); hold on
% plot(le*x + lp, angle(u2f)/pi*180, 'r--')


% save('bm_ext_sol_lamB_fr_90_Rl_1e4','u1f', 'u2f', 'x');
% save('bm_ext_sol_lamB_fr_70_Rl_1e4','u1f', 'u2f', 'x');
% save('bm_ext_sol_lamB_fr_50_Rl_1e4','u1f', 'u2f', 'x');
% save('bm_ext_sol_lamB_fr_30_Rl_1e4','u1f', 'u2f', 'x');
% save('bm_ext_sol_lamB_fr_10_Rl_1e4','u1f', 'u2f', 'x');


% end

