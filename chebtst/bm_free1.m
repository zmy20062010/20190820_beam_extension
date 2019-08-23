format long;
clc;clear;
n = 70; 
dom = [0 1]; x = chebfun('x',dom); 
A = chebop(dom); A.op = @(x,u) diff(u,4); 

T = chebpoly(0:n-1,dom); 
AA = A(x,T);  Q = T; 
u0 = feval(T,dom(1)); u1 = feval(diff(T),dom(1)); 
v0 = feval(diff(T,2),dom(2)); v1 = feval(diff(T,3),dom(2)); 
BC = [u0;u1;v0;v1]; BClam = zeros(size(BC)); 

d = size(BC,1); 

[QA,RA] = qr([AA Q]); [U,S,V] = svd(RA,0); 
UU = QA*U(:,1:n-d); 

At = UU'*AA; Bt = UU'*Q; At = [At;BC]; Bt = [Bt;BClam]; 
[V,D] = eig(At,Bt); V = Q*V; 

res = A(x,V)-V*D; 
for ii = 1:size(D,2), ress(ii) = norm(res(:,ii)); end 
ix = find(ress<1e-2); % 1e-2 is a tolerance 
D = D(ix,ix); V = V(:,ix); 
[D,ixx] = sort(diag(D)); V = V(:,ixx); 
sqrt(D) 