import numpy as np
import matplotlib.pyplot as plt

# beam base structure material constants
lp   = 100.0e-3
Ys   = 100.0e9
rhos = 7.165e3
hs   = 0.25e-3
b    = 20.0e-3
# piezo layer material constants
c11E = 66.0e9
rhop = 7.80e3
hp   = 0.2e-3
ep33S= 15.93e-9
d31  = -190.0e-12
e31  = d31 * c11E
# e31  = -5.35
# external circuit and excitation
fr   = 40
Rl   = 45.0e3


Bp = 2.0e0/3.0e0 * b * ( Ys*hs**3.0e0 + c11E*((hs+hp)**3.0e0 - hs**3.0e0) )
Cp = ep33S * b * lp / 2.0e0 / hp
ep = b * e31 * (hs + hp/2.0e0)
mp = 2.0e0 * b * ( rhos * hs + rhop * hp )

# dimensionless parameters
alpha = ep * np.sqrt(lp / Cp / Bp)
beta  = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
nu    = 2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp)

sqlam = np.sqrt(nu)
delta = alpha*alpha
print(delta)
xib = 0.5e-3
rd = xib / lp
rv = ep / Cp


def output_vals(arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta, arg_rd = rd, arg_rv = rv, arg_Rl = Rl):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Aef = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Bef = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Cef = 1.0 - Aef
    Def = - Bef

    #########  Expansion for the function
    ue1 = arg_sqlam * ( - Aef * np.sin(arg_sqlam) + Bef * np.cos(arg_sqlam) + Cef * np.sinh(arg_sqlam) + Def * np.cosh(arg_sqlam) )
    ve = -( 1j * arg_beta * arg_sqlam * arg_sqlam) / (1 + 1j * beta * arg_sqlam * arg_sqlam ) * arg_rd * arg_rv * ue1
    ie = ve / arg_Rl
    pe = ve * ie

    return [ue1, ve, ie, pe]


fr_list    = np.logspace(0.0, 3.0, 3001)
wr_list    = 2.0 * np.pi * fr_list
sqlam_list = np.sqrt(2 * np.pi * fr_list * np.sqrt(mp * lp**4.0e0 / Bp))

ue1_list = np.zeros(np.shape(sqlam_list), dtype=complex)
vol_list = np.zeros(np.shape(sqlam_list), dtype=complex)
cur_list = np.zeros(np.shape(sqlam_list), dtype=complex)
pow_list = np.zeros(np.shape(sqlam_list), dtype=complex)



plt.figure(1, figsize=(8,6))

Rl = 1.0e2
for i in range(sqlam_list.size):
    sqlam  = sqlam_list[i]
    beta   = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
    output = output_vals(sqlam, beta, delta, rd, rv, Rl)

    ue1_list[i] = output[0]
    vol_list[i] = output[1]
plt.plot(fr_list, np.abs(vol_list)/wr_list/wr_list/xib, 'r.', label='$R_l = 10^2 \\Omega$')
Rl = 1.0e3
for i in range(sqlam_list.size):
    sqlam  = sqlam_list[i]
    beta   = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
    output = output_vals(sqlam, beta, delta, rd, rv, Rl)

    ue1_list[i] = output[0]
    vol_list[i] = output[1]
plt.plot(fr_list, np.abs(vol_list)/wr_list/wr_list/xib, 'b--', label='$R_l = 10^3 \\Omega$')
Rl = 1.0e4
for i in range(sqlam_list.size):
    sqlam  = sqlam_list[i]
    beta   = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
    output = output_vals(sqlam, beta, delta, rd, rv, Rl)

    ue1_list[i] = output[0]
    vol_list[i] = output[1]
plt.plot(fr_list, np.abs(vol_list)/wr_list/wr_list/xib, 'c-.', label='$R_l = 10^4 \\Omega$')
Rl = 1.0e5
for i in range(sqlam_list.size):
    sqlam  = sqlam_list[i]
    beta   = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
    output = output_vals(sqlam, beta, delta, rd, rv, Rl)

    ue1_list[i] = output[0]
    vol_list[i] = output[1]
plt.plot(fr_list, np.abs(vol_list)/wr_list/wr_list/xib, 'm--', label='$R_l = 10^5 \\Omega$')
Rl = 1.0e6
for i in range(sqlam_list.size):
    sqlam  = sqlam_list[i]
    beta   = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
    output = output_vals(sqlam, beta, delta, rd, rv, Rl)

    ue1_list[i] = output[0]
    vol_list[i] = output[1]
plt.plot(fr_list, np.abs(vol_list)/wr_list/wr_list/xib, 'k', label='$R_l = 10^6 \\Omega$')



plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.yscale('log')
plt.xlabel('Base excitation frequency $f_b$ ($Hz$)', fontsize=16)
plt.ylabel('Normalized output voltage $| \\tilde{V}_p/(\\sigma_b^2 \\eta_b) |$ ($V \\cdot s^2 / m$)', fontsize=16)
plt.grid(True)
lgd = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),
          fancybox=True, shadow=True)


# plt.tight_layout()
plt.savefig('fig_sol_analytic_perf_vs_fr.jpg',dpi=300, bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig('fig_sol_analytic_perf_vs_fr.eps', bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig('fig_sol_analytic_perf_vs_fr.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.show()
