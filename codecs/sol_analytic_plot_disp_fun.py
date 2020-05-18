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

delta = alpha*alpha
sqlam = np.sqrt(nu)

xib = 0.5e-3
rd = xib / lp
rv = ep / Cp

fr_list = np.logspace(0.0, 3.0, 3001)
sqlam_list = np.sqrt(2 * np.pi * fr_list * np.sqrt(mp * lp**4.0e0 / Bp))
x = np.linspace(0.0, 1.0, 10001)

def beam_disp(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be
    #########  Expansion for the function
    ue = Ae*np.cos(arg_sqlam*x) + Be*np.sin(arg_sqlam*x) + Ce*np.cosh(arg_sqlam*x) + De*np.sinh(arg_sqlam*x) - 1.0
    return ue

def beam_disp_zero(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be
    #########  Expansion for the function
    ue = Ae*np.cos(arg_sqlam*x) + Be*np.sin(arg_sqlam*x) + Ce*np.cosh(arg_sqlam*x) + De*np.sinh(arg_sqlam*x) - 1.0
    return ue

def beam_disp_infty(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
    #########  Closed form solutions
    coeff_denom = np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam)
    Ae = np.cos(arg_sqlam)*np.sinh(arg_sqlam) / coeff_denom
    Be = np.sin(arg_sqlam)*np.sinh(arg_sqlam) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be
    #########  Expansion for the function
    ue = Ae*np.cos(arg_sqlam*x) + Be*np.sin(arg_sqlam*x) + Ce*np.cosh(arg_sqlam*x) + De*np.sinh(arg_sqlam*x) - 1.0
    return ue



print(beta, nu)

plt.figure(1, figsize=(16,8))
plt.subplot(121)
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'm', label = '$\\delta = $ {0}'.format(0.0), linewidth = 3)
delta = 0.01
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-.', label = '$\\delta = $ {0}'.format(delta))
delta = 0.1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'b--', label = '$\\delta = $ {0}'.format(delta))
delta = 1.0
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'c--', label = '$\\delta = $ {0}'.format(delta))
delta = 10.0
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'g--', label = '$\\delta = $ {0}'.format(delta))
delta = 100.0
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'y-.', label = '$\\delta = $ {0}'.format(delta))
plt.plot(x, np.abs(beam_disp_infty(x, sqlam, beta, delta)), 'k', label = '$\\delta = $ $\\infty$', linewidth = 3)

plt.legend(loc = 'upper left')
plt.grid(True)
# plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}'.format(delta,nu))
plt.xlabel('Dimensionless coordinate $z$',fontsize=16)
plt.ylabel('Modulus of relative displacement function $u(z)$',fontsize=16)




plt.subplot(122)
plt.plot(x, np.angle(beam_disp_zero(x, sqlam, beta, delta))/np.pi*180, 'm', label = '$\\delta = $ {0}'.format(0.0), linewidth = 3)
delta = 0.01
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, delta))/np.pi*180, 'r-.', label = '$\\delta = $ {0}'.format(delta))
delta = 0.1
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, delta))/np.pi*180, 'b--', label = '$\\delta = $ {0}'.format(delta))
delta = 1.0
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, delta))/np.pi*180, 'c--', label = '$\\delta = $ {0}'.format(delta))
delta = 10.0
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, delta))/np.pi*180, 'g--', label = '$\\delta = $ {0}'.format(delta))
delta = 100.0
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, delta))/np.pi*180, 'y-.', label = '$\\delta = $ {0}'.format(delta))
plt.plot(x, np.angle(beam_disp_infty(x, sqlam, beta, delta))/np.pi*180, 'k', label = '$\\delta = $ $\\infty$', linewidth = 3)

plt.legend(loc = 'center right')
plt.grid(True)
# plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}'.format(delta,nu))
plt.xlabel('Dimensionless coordinate $z$',fontsize=16)
plt.ylabel('Phase of relative displacement function $u(z)$',fontsize=16)
plt.ylim([-30,5])

plt.tight_layout()

# plt.axes([.18, .7, .2, .2])
# plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'm', linewidth = 3)
# delta = 0.01
# plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-.')
# delta = 0.1
# plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'b--')
# delta = 1.0
# plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'c--')
# plt.xlim([0.8,1.0])
# plt.ylim([0.27,0.38])

plt.savefig('fig_sol_analytic_disp_fun.jpg',dpi=300)
plt.savefig('fig_sol_analytic_disp_fun.eps')
plt.savefig('fig_sol_analytic_disp_fun.pdf')

plt.show()















































# plt.figure(1, figsize=(12,6))
# print(sqlam,beta,delta)
# plt.subplot(121)
# plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta)), 'm-', label = '$\\delta = 0.0$', linewidth=3)
# plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 0.01)), 'b-.', label = '$\\delta = 0.01$')
# plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 0.1)), 'g-.', label = '$\\delta = 0.1$')
# plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 1.0)), 'k-.', label = '$\\delta = 1.0$')
# plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 10.0)), 'c-', label = '$\\delta = 10.0$')
# plt.plot(x, np.abs(beam_disp_infty(x, sqlam, beta)), 'y-', label = '$\\delta = \\infty$', linewidth=3)
# plt.grid(True)
# plt.legend(loc='best')
# plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
# plt.ylabel('Amplitude of $u(z)$')
# plt.xlabel('Streamwise position $z$')


# plt.subplot(122)
# plt.plot(x, np.angle(beam_disp_zero(x, sqlam, beta)), 'm-', label = '$\\delta = 0.0$', linewidth=3)
# plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 0.01)), 'b-.', label = '$\\delta = 0.01$')
# plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 0.1)), 'g-.', label = '$\\delta = 0.1$')
# plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 1.0)), 'k-.', label = '$\\delta = 1.0$')
# plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 10.0)), 'c-', label = '$\\delta = 10.0$')
# plt.plot(x, np.angle(beam_disp_infty(x, sqlam, beta)), 'y--', label = '$\\delta = \\infty$', linewidth=3)
# plt.grid(True)
# plt.legend(loc='best')
# plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
# plt.xlabel('Streamwise position $z$')
# plt.ylabel('Phase of $u(z)$')
# plt.ylim([-1.0e-2,0.1e-2])
# plt.tight_layout()


# plt.savefig('fig_sol_analytic_disp_fun.jpg',dpi=300)
# plt.savefig('fig_sol_analytic_disp_fun.delta')
# plt.savefig('fig_sol_analytic_disp_fun.pdf')
# plt.show()














# def beam_disp_der1(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
#     #########  Closed form solutions
#     coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
#     Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
#     Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
#     Ce = 1.0 - Ae
#     De = - Be
#     #########  Expansion for the function
#     ue = -Ae*np.sin(arg_sqlam*x) + Be*np.cos(arg_sqlam*x) + Ce*np.sinh(arg_sqlam*x) + De*np.cosh(arg_sqlam*x)
#     ue = ue * arg_sqlam
#     return ue
# plt.figure(1, figsize=(16,8))
# plt.plot(fr_list, np.abs(beam_disp_der1(1.0, sqlam_list, beta, delta)), 'r-', label = 'closed form')
# plt.yscale('log')
# plt.show()