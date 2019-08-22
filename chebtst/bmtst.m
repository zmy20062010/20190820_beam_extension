function bmtst
% 
% %     beam base structure material constants
% lp   =  100.0e-3;
% Ys   =  10.0e10;
% rhos =  7.165e3;
% hs   =  0.5e-3;
% b    =  20.0e-3;
% %     piezo layer material constants
% Yp   = 66.0e9;
% rhop = 7.80e3;
% hp   = 0.4e-3;
% ep33S= 15.93e-9;
% d31  = -190e-12;
% e31  = d31 * Yp;
% %     external circuit and excitation
% fr   = 1;
% Rl   = 100.0e3;
% 
% %     positions from the neutral axis as a reference
% nY  = Ys / Yp;
% hpa = ( hp*hp + 2*nY*hp*hs + nY*hs*hs) / (hp+nY*hs) / 2.0e0;
% hsa = ( hp*hp + 2*hp*hs + nY*hs*hs) / (hp+nY*hs) / 2.0e0;
% hpc = nY*hs*(hp + hs) / (hp+nY*hs) / 2.0e0;
% ya  = -hsa;
% yb  = hpa - hp;
% yc  = hpa;
% 
% %     structural, electrical, and piezoelectric parameters
% Bp = b/3.0e0*( Ys*(yb*yb*yb - ya*ya*ya) + Yp*(yc*yc*yc - yb*yb*yb) );
% Cp = ep33S * b * lp / hp;
% ep = b * Yp * d31 * (yc*yc - yb*yb) / 2.0e0 / hp;
% mp = b * ( rhos * hs + rhop * hp );
% 
% alpha = ep * sqrt(lp / Cp / Bp);
% beta  = Rl * Cp * sqrt(Bp / mp / lp^4.0e0);
% nu    = 2 * pi * fr * sqrt(mp * lp^4.0e0 / Bp);


A = chebop(0,1);
A.op = @(x,u) diff(u,4);
A.lbc = @(u) [u; diff(u)];
A.rbc = @(u) [diff(u,2); diff(u,3)];
lam = eigs(A, 15);
sqrt(lam)






