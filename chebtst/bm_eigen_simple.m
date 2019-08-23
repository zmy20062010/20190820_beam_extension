function bm_eigen_simple

alpha = -0.2646;
beta  = 0.6805;
nu    = 0.0735;

A = chebop(0,1);
A.op = @(x,u) diff(u,4) - nu*nu*u;
A.lbc = @(u) [u-1; diff(u)];
A.rbc = @(u) [diff(u,2) + 1i*nu*beta/(1i*nu*beta+1)*alpha*alpha*diff(u); diff(u,3)];
u = A\0;

end