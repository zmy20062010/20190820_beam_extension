import numpy as np
import matplotlib.pyplot as plt


# beam base structure material constants
lp   =  50.0e-3
Ys   =  10.8e10
rhos =  8.8e3
hs   =  0.25e-3
b    =  20.0e-3
# piezo layer material constants
c11E = 12.03e10
rhop = 7.75e3
hp   = 0.5e-3
ep33S= 7.32e-9
e31  = -5.35
# external circuit and excitation
fr   = 50
Rl   = 45.0e3


Bp = 2.0e0/3.0e0 * b * ( Ys * hs**3.0e0 + c11E * ((hs + hp)**3.0e0) - hs**3.0e0 )
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


x = np.linspace(0.0, 1.0, 10001)

def beam_disp(x, arg_sqlam = sqlam, arg_beta = beta, arg_eps = eps):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be

    #########  Expansion for the function
    ue = Ae * np.cos(arg_sqlam*x) + Be * np.sin(arg_sqlam*x) + Ce * np.cosh(arg_sqlam*x) + De * np.sinh(arg_sqlam*x)

    return ue
def beam_disp_zero(x, arg_sqlam = sqlam, arg_beta = beta):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be

    #########  Expansion for the function
    ue = Ae * np.cos(arg_sqlam*x) + Be * np.sin(arg_sqlam*x) + Ce * np.cosh(arg_sqlam*x) + De * np.sinh(arg_sqlam*x)

    return ue
def beam_disp_infty(x, arg_sqlam = sqlam, arg_beta = beta):
    #########  Closed form solutions
    coeff_denom = np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam)
    Ae = np.cos(arg_sqlam)*np.sinh(arg_sqlam) / coeff_denom
    Be = np.sin(arg_sqlam)*np.sinh(arg_sqlam) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be

    #########  Expansion for the function
    ue = Ae * np.cos(arg_sqlam*x) + Be * np.sin(arg_sqlam*x) + Ce * np.cosh(arg_sqlam*x) + De * np.sinh(arg_sqlam*x)

    return ue



x1 = 1.0
delta_list = np.logspace(-4,4,801)

fig, ax1 = plt.subplots(figsize=(12,6))

ax2 = ax1.twinx()
ax1.plot(delta_list, np.abs(beam_disp(x1, sqlam, beta, delta_list)), 'r-' , linewidth=3, label='$|u(1)|$')
ax2.plot(delta_list, np.angle(beam_disp(x1, sqlam, beta, delta_list)), 'b--', linewidth=3, label='$\\angle u(1) $')

ax1.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax2.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax1.set_xscale('log')
ax1.grid(True)


ax1.set_xlabel('Electromechanical coupling factor $\\delta$')
ax1.set_ylabel('Amplitude of $u(1)$', color='r')
ax2.set_ylabel('Phase of $u(1)$', color='b')
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






