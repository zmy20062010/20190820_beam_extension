function bm_ext_base

xib  = 0.1e-3;
%% Rl 100 ohm
Rl   = 100.0e3;
frlist = logspace(0,3,400);
wlist  = 2*pi*frlist;
Vplist = zeros(size(frlist));
Iplist = zeros(size(frlist));
Pplist = zeros(size(frlist));
for k = 1:length(frlist)
    [Vp, Ip, Pp] = bm_ext_eig(frlist(k), Rl);
    Vplist(k) = Vp;
    Iplist(k) = Ip;
    Pplist(k) = Pp;
end

subplot(131); semilogy(frlist, abs(Vplist)./wlist./wlist/xib, 'r');hold on;
subplot(132); semilogy(frlist, abs(Iplist)./wlist./wlist/xib, 'r');hold on;
subplot(133); semilogy(frlist, abs(Pplist)./wlist./wlist/xib, 'r');hold on;



end