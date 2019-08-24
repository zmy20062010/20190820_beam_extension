format long;
A = chebop(0,1);
A.op = @(x,u) diff(u,4);
A.lbc = @(u) [u; diff(u)];
A.rbc = @(u) [diff(u,2); diff(u,3)];
lam10 = eigs(A, 10);

lam15 = eigs(A, 15);
lam20 = eigs(A, 20);
lam40 = eigs(A, 40);

display('first eigenvalue for 10, 15, 20, and 40:')
[sqrt(lam10(1)), sqrt(lam15(1)), sqrt(lam20(1)), sqrt(lam40(1))]