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

eps = alpha*alpha
sqlam = np.sqrt(nu)

xib = 0.5e-3
rd = xib / lp
rv = ep / Cp


print(e31, ep)


x = np.linspace(0.0, 1.0, 10001)

def beam_disp(x, arg_sqlam = sqlam, arg_beta = beta, arg_eps = eps):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be

    #########  Expansion for the function
    ue = Ae * np.cos(arg_sqlam*x) + Be * np.sin(arg_sqlam*x) + Ce * np.cosh(arg_sqlam*x) + De * np.sinh(arg_sqlam*x) - 1.0

    return ue
def beam_disp_zero(x, arg_sqlam = sqlam, arg_beta = beta):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be

    #########  Expansion for the function
    ue = Ae * np.cos(arg_sqlam*x) + Be * np.sin(arg_sqlam*x) + Ce * np.cosh(arg_sqlam*x) + De * np.sinh(arg_sqlam*x) - 1.0

    return ue
def beam_disp_infty(x, arg_sqlam = sqlam, arg_beta = beta):
    #########  Closed form solutions
    coeff_denom = np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam)
    Ae = np.cos(arg_sqlam)*np.sinh(arg_sqlam) / coeff_denom
    Be = np.sin(arg_sqlam)*np.sinh(arg_sqlam) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be

    #########  Expansion for the function
    ue = Ae * np.cos(arg_sqlam*x) + Be * np.sin(arg_sqlam*x) + Ce * np.cosh(arg_sqlam*x) + De * np.sinh(arg_sqlam*x) - 1.0

    return ue

print(beta, nu)

x1 = 1.0
delta_list = np.logspace(-4,4,801)

fig, ax1 = plt.subplots(figsize=(12,6))

ax2 = ax1.twinx()
ax1.plot(delta_list, np.abs(beam_disp(x1, sqlam, beta, delta_list)), 'r-' , linewidth=3, label='$|u(1;\\delta)|$')
ax2.plot(delta_list, np.angle(beam_disp(x1, sqlam, beta, delta_list))/np.pi*180, 'b--', linewidth=3, label='$\\angle u(1;\\delta) $')

ax1.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax2.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax1.set_xscale('log')
ax1.grid(True)


ax1.set_xlabel('Electromechanical coupling factor $\\delta$',fontsize=16)
ax1.set_ylabel('Modulus of $u(1;\\delta)$', color='r',fontsize=16)
ax2.set_ylabel('Phase of $u(1;\\delta)$', color='b',fontsize=16)
ax1.legend(loc = 'lower left')
ax2.legend(loc = 'lower right')

plt.tight_layout()
plt.savefig('fig_sol_analytic_disp_end.jpg',dpi=300)
plt.savefig('fig_sol_analytic_disp_end.eps')
plt.savefig('fig_sol_analytic_disp_end.pdf')
plt.show()







# plt.xlabel('Streamwise position $z$')
# plt.ylabel('Phase of $u(z)$')
# plt.ylim([-1.0e-2,0.1e-2])






