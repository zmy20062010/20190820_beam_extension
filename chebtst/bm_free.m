format long;
A = chebop(0,1);
A.op = @(x,u) diff(u,4);
A.lbc = @(u) [u; diff(u)];
A.rbc = @(u) [diff(u,2); diff(u,3)];
lam = eigs(A, 10);
sqrt(lam)