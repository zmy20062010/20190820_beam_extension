import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.ticker as ticker
import matplotlib.colors as colors

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
fr   = 20
Rl   = 10.0e3


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

xib = 0.5e-3
rd = xib / lp
rv = ep / Cp


print(beta, nu, alpha, delta)


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


delta_list = np.logspace(-4,4,801)
# delta_list = np.transpose(delta_list)
ue1_list = np.zeros(np.shape(delta_list), dtype=complex)
vol_list = np.zeros(np.shape(delta_list), dtype=complex)
cur_list = np.zeros(np.shape(delta_list), dtype=complex)
pow_list = np.zeros(np.shape(delta_list), dtype=complex)

for i in range(delta_list.size):
    delta  = delta_list[i]
    alpha  = np.sqrt(delta)
    ep     = alpha / np.sqrt(lp / Cp / Bp)
    rv     = ep / Cp
    output = output_vals(sqlam, beta, delta, rd, rv, Rl)

    ue1_list[i] = output[0]
    vol_list[i] = output[1]
    cur_list[i] = output[2]
    pow_list[i] = output[3]


plt.figure(1, figsize=(18,6))
plt.subplot(131)
plt.plot(delta_list, np.abs(vol_list))
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.xscale('log')
plt.xlabel('Electromechanical coupling factor $\\delta$',fontsize=16)
plt.ylabel('Amplitude of output voltage $\\tilde{V}_p$',fontsize=16)
plt.grid(True)

plt.subplot(132)
plt.plot(delta_list, np.abs(cur_list))
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.xscale('log')
plt.xlabel('Electromechanical coupling factor $\\delta$',fontsize=16)
plt.ylabel('Amplitude of output current $\\tilde{I}_p$',fontsize=16)
plt.grid(True)

plt.subplot(133)
plt.plot(delta_list, np.abs(pow_list))
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.xscale('log')
plt.xlabel('Electromechanical coupling factor $\\delta$',fontsize=16)
plt.ylabel('Amplitude of output power $\\tilde{P}_p$',fontsize=16)
plt.grid(True)

plt.tight_layout()
# plt.savefig('fig_sol_analytic_perf_fun.jpg',dpi=300)
plt.savefig('fig_sol_analytic_perf_fun.eps')
plt.savefig('fig_sol_analytic_perf_fun.pdf')

plt.show()






# plt.figure(2, figsize=(16,6))

# eps_list = np.logspace(-4,0,401)
# plt.subplot(131)
# plt.plot(eps_list, np.abs(output_vals(sqlam, beta, eps_list)[1]), 'r-', label = 'voltage $\\tilde{V}_p$')
# # plt.xscale('log')
# # plt.yscale('log')
# plt.grid(True)
# plt.legend()
# plt.xlabel('Electromechanical coupling factor $\\delta$')
# plt.ylabel('Output voltage $\\tilde{V}_p$')


# plt.subplot(132)
# plt.plot(eps_list, np.abs(output_vals(sqlam, beta, eps_list)[2]), 'b-', label = 'Current $\\tilde{I}_p$')
# # plt.xscale('log')
# # plt.yscale('log')
# plt.grid(True)
# plt.legend()
# plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
# plt.xlabel('Electromechanical coupling factor $\\delta$')
# plt.ylabel('Output current $\\tilde{I}_p$')


# plt.subplot(133)
# plt.plot(eps_list, np.abs(output_vals(sqlam, beta, eps_list)[3]), 'k-', label = 'Power $\\tilde{P}_p$')
# # plt.xscale('log')
# # plt.yscale('log')
# plt.grid(True)
# plt.legend()
# plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
# plt.xlabel('Electromechanical coupling factor $\\delta$')
# plt.ylabel('Output power $\\tilde{P}_p$')


# plt.tight_layout()

# # plt.savefig('fig_sol_analytic_perf_fun.jpg',dpi=300)
# # plt.savefig('fig_sol_analytic_perf_fun.eps')
# # plt.savefig('fig_sol_analytic_perf_fun.pdf')

# plt.show()