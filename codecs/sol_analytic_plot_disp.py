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
    ue = Ae*np.cos(arg_sqlam*x) + Be*np.sin(arg_sqlam*x) + Ce*np.cosh(arg_sqlam*x) + De*np.sinh(arg_sqlam*x) - 1.0
    return ue


def beam_disp_zero(x, arg_sqlam = sqlam, arg_beta = beta, arg_eps = eps):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be
    #########  Expansion for the function
    ue = Ae*np.cos(arg_sqlam*x) + Be*np.sin(arg_sqlam*x) + Ce*np.cosh(arg_sqlam*x) + De*np.sinh(arg_sqlam*x) - 1.0
    return ue


def beam_disp_one(x, arg_sqlam = sqlam, arg_beta = beta, arg_eps = eps):
    #########  Zeroth order coefficients
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) )
    A0 = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    B0 = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    C0 = 1.0 - A0
    D0 = - B0
    #########  Expansion for the zeroth order
    u0 = A0*np.cos(arg_sqlam*x) + B0*np.sin(arg_sqlam*x) + C0*np.cosh(arg_sqlam*x) + D0*np.sinh(arg_sqlam*x) - 1.0

    #########  First order coefficients
    coeffs1 = 1j * arg_beta * arg_sqlam / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * (np.sinh(arg_sqlam) - np.sin(arg_sqlam)) / ( 1 + np.cosh(arg_sqlam) * np.cos(arg_sqlam) ) / ( 2.0 + 2.0 * np.cosh(arg_sqlam) * np.cos(arg_sqlam) )
    A1 = coeffs1 * ( np.cosh(arg_sqlam) + np.cos(arg_sqlam) )
    B1 = coeffs1 * ( -np.sinh(arg_sqlam) + np.sin(arg_sqlam) )
    C1 = - A1
    D1 = - B1
    #########  Expansion for the zeroth order
    u1 = A1*np.cos(arg_sqlam*x) + B1*np.sin(arg_sqlam*x) + C1*np.cosh(arg_sqlam*x) + D1*np.sinh(arg_sqlam*x)
    
    return u0 + arg_eps * u1


def beam_disp_two(x, arg_sqlam = sqlam, arg_beta = beta, arg_eps = eps):
    #########  Zeroth order coefficients
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) )
    A0 = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    B0 = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    C0 = 1.0 - A0
    D0 = - B0
    #########  Expansion for the zeroth order
    u0 = A0*np.cos(arg_sqlam*x) + B0*np.sin(arg_sqlam*x) + C0*np.cosh(arg_sqlam*x) + D0*np.sinh(arg_sqlam*x) - 1.0

    #########  First order coefficients
    coeffs1 = 1j * arg_beta * arg_sqlam / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * (np.sinh(arg_sqlam) - np.sin(arg_sqlam)) / ( 1 + np.cosh(arg_sqlam) * np.cos(arg_sqlam) ) / ( 2.0 + 2.0 * np.cosh(arg_sqlam) * np.cos(arg_sqlam) )
    A1 = coeffs1 * ( np.cosh(arg_sqlam) + np.cos(arg_sqlam) )
    B1 = coeffs1 * ( -np.sinh(arg_sqlam) + np.sin(arg_sqlam) )
    C1 = - A1
    D1 = - B1
    #########  Expansion for the zeroth order
    u1 = A1*np.cos(arg_sqlam*x) + B1*np.sin(arg_sqlam*x) + C1*np.cosh(arg_sqlam*x) + D1*np.sinh(arg_sqlam*x)
    
    #########  Second order coefficients
    coeffs2 = (1j * arg_beta * arg_sqlam / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ))**2.0 * (np.sinh(arg_sqlam) - np.sin(arg_sqlam)) / ( 1 + np.cosh(arg_sqlam) * np.cos(arg_sqlam) ) * ( np.cos(arg_sqlam) * np.sinh(arg_sqlam) + np.sin(arg_sqlam) * np.cosh(arg_sqlam) ) / ( 1 + np.cosh(arg_sqlam) * np.cos(arg_sqlam) ) / ( 2.0 + 2.0 * np.cosh(arg_sqlam) * np.cos(arg_sqlam) )
    A2 = coeffs2 * ( np.cosh(arg_sqlam) + np.cos(arg_sqlam) )
    B2 = coeffs2 * ( -np.sinh(arg_sqlam) + np.sin(arg_sqlam) )
    C2 = - A2
    D2 = - B2
    #########  Expansion for the zeroth order
    u2 = A2*np.cos(arg_sqlam*x) + B2*np.sin(arg_sqlam*x) + C2*np.cosh(arg_sqlam*x) + D2*np.sinh(arg_sqlam*x)
    
    return u0 + arg_eps * u1 + arg_eps * arg_eps * u2


def beam_disp_infty(x, arg_sqlam = sqlam, arg_beta = beta, arg_eps = eps):
    #########  Closed form solutions
    coeff_denom = np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam)
    Ae = np.cos(arg_sqlam)*np.sinh(arg_sqlam) / coeff_denom
    Be = np.sin(arg_sqlam)*np.sinh(arg_sqlam) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be
    #########  Expansion for the function
    ue = Ae*np.cos(arg_sqlam*x) + Be*np.sin(arg_sqlam*x) + Ce*np.cosh(arg_sqlam*x) + De*np.sinh(arg_sqlam*x) - 1.0
    return ue


plt.figure(1, figsize=(16,8))
plt.subplot(221)
eps = 0.01
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, eps)), 'r-', label = 'closed form')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, eps)), 'b-.', label = '0th order')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, eps)), 'k-', label = '1st order')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, eps)), 'm-.', label = '2nd order')
plt.legend(loc = 'upper left')
plt.grid(True)
plt.title('$\\delta = 0.01$')


plt.subplot(222)
eps = 0.1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, eps)), 'r-', label = 'closed form')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, eps)), 'b-.', label = '0th order')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, eps)), 'k-', label = '1st order')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, eps)), 'm-.', label = '2nd order')
plt.legend(loc = 'upper left')
plt.grid(True)
plt.title('$\\delta = 0.1$')


plt.subplot(223)
eps = 1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, eps)), 'r-', label = 'closed form')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, eps)), 'b-.', label = '0th order')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, eps)), 'k-', label = '1st order')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, eps)), 'm-.', label = '2nd order')
plt.legend(loc = 'upper left')
plt.grid(True)
plt.title('$\\delta = 1$')


plt.subplot(224)
eps = 10
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, eps)), 'r-', label = 'closed form')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, eps)), 'b-.', label = '0th order')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, eps)), 'k-', label = '1st order')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, eps)), 'm-.', label = '2nd order')
plt.legend(loc = 'upper left')
plt.grid(True)
plt.title('$\\delta = 10$')




plt.tight_layout()
plt.savefig('fig_sol_analytic_disp_cmp.jpg',dpi=300)
plt.savefig('fig_sol_analytic_disp_cmp.eps')
plt.savefig('fig_sol_analytic_disp_cmp.pdf')

plt.show()















































# plt.figure(1, figsize=(12,6))
# print(sqlam,beta,eps)
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
# plt.savefig('fig_sol_analytic_disp_fun.eps')
# plt.savefig('fig_sol_analytic_disp_fun.pdf')
# plt.show()