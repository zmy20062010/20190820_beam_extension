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
fr   = 45
Rl   = 50.0e3


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

def beam_disp_der(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be
    #########  Expansion for the function
    ude = - Ae*np.sin(arg_sqlam*x) + Be*np.cos(arg_sqlam*x) + Ce*np.sinh(arg_sqlam*x) + De*np.cosh(arg_sqlam*x)
    return ude * arg_sqlam
def beam_disp_der2(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be
    #########  Expansion for the function
    ude = - Ae*np.cos(arg_sqlam*x) - Be*np.sin(arg_sqlam*x) + Ce*np.cosh(arg_sqlam*x) + De*np.sinh(arg_sqlam*x)
    return ude * arg_sqlam * arg_sqlam

def beam_disp_der_zero(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be
    #########  Expansion for the function
    ue = -Ae*np.sin(arg_sqlam*x) + Be*np.cos(arg_sqlam*x) + Ce*np.sinh(arg_sqlam*x) + De*np.cosh(arg_sqlam*x)
    ue = ue * arg_sqlam
    return ue

def beam_disp_der_one(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
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
    
    return u0 + arg_delta * u1

def beam_disp_der_two(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
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
    
    return u0 + arg_delta * u1 + arg_delta * arg_delta * u2

def beam_disp_der_infty(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
    #########  Closed form solutions
    coeff_denom = np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam)
    Ae = np.cos(arg_sqlam)*np.sinh(arg_sqlam) / coeff_denom
    Be = np.sin(arg_sqlam)*np.sinh(arg_sqlam) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be
    #########  Expansion for the function
    ue = Ae*np.cos(arg_sqlam*x) + Be*np.sin(arg_sqlam*x) + Ce*np.cosh(arg_sqlam*x) + De*np.sinh(arg_sqlam*x) - 1.0
    return ue


###############################################################################
###############################################################################

# plt.figure(1, figsize=(16,8))

# delta = 0.01
# plt.plot(x, np.abs(beam_disp_der(x, sqlam, beta, delta)), 'r-', label = 'closed form')
# plt.plot(x, np.abs(beam_disp_der2(x, sqlam, beta, delta)), 'b-', label = 'closed form')

# plt.legend(loc = 'upper left')
# plt.grid(True)
# plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr))
# plt.show()



###############################################################################
###############################################################################

plt.figure(2, figsize=(16,8))
delta_list = np.logspace(-4,4,801)
x1 = 1.0

fr = 1
sqlam = np.sqrt(2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp))
plt.plot(delta_list, np.abs(beam_disp_der(x1, sqlam, beta, delta_list)), 'r->', label = '$f_b =$ {} $Hz$'.format(fr))

fr = 20
sqlam = np.sqrt(2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp))
plt.plot(delta_list, np.abs(beam_disp_der(x1, sqlam, beta, delta_list)), 'r--', label = '$f_b =$ {} $Hz$'.format(fr), linewidth=6)

fr = 45
sqlam = np.sqrt(2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp))
plt.plot(delta_list, np.abs(beam_disp_der(x1, sqlam, beta, delta_list)), 'b-.', label = '$f_b =$ {} $Hz$'.format(fr), linewidth=6)

fr = 45.2
sqlam = np.sqrt(2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp))
plt.plot(delta_list, np.abs(beam_disp_der(x1, sqlam, beta, delta_list)), 'k-s', label = '$f_b =$ {} $Hz$'.format(fr))

fr = 50
sqlam = np.sqrt(2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp))
plt.plot(delta_list, np.abs(beam_disp_der(x1, sqlam, beta, delta_list)), 'c-d', label = '$f_b =$ {} $Hz$'.format(fr))

fr = 60
sqlam = np.sqrt(2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp))
plt.plot(delta_list, np.abs(beam_disp_der(x1, sqlam, beta, delta_list)), 'y-*', label = '$f_b =$ {} $Hz$'.format(fr))

fr = 70
sqlam = np.sqrt(2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp))
plt.plot(delta_list, np.abs(beam_disp_der(x1, sqlam, beta, delta_list)), 'm-o', label = '$f_b =$ {} $Hz$'.format(fr))

fr = 71.8
sqlam = np.sqrt(2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp))
plt.plot(delta_list, np.abs(beam_disp_der(x1, sqlam, beta, delta_list)), 'g-p', label = '$f_b =$ {} $Hz$'.format(fr))

fr = 80
sqlam = np.sqrt(2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp))
plt.plot(delta_list, np.abs(beam_disp_der(x1, sqlam, beta, delta_list)), 'k-.', label = '$f_b =$ {} $Hz$'.format(fr))

fr = 100
sqlam = np.sqrt(2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp))
plt.plot(delta_list, np.abs(beam_disp_der(x1, sqlam, beta, delta_list)), 'm--', label = '$f_b =$ {} $Hz$'.format(fr))

plt.xscale('log')
plt.yscale('log')
plt.legend(loc = 'best', ncol = 2)
plt.xlabel('Electromechanical coupling factor $\\delta$', fontsize=16)
plt.ylabel('Output index $\\chi_p$', fontsize=16)
# plt.title('End displacement slope $u^\\prime(1)$ at $fr =$ {}'.format(fr))
plt.grid(True)
plt.tight_layout()
plt.savefig('./img/fig_sol_analytic_out_index_vs_delta.jpg',dpi=300)
plt.savefig('./img/fig_sol_analytic_out_index_vs_delta.eps')
plt.savefig('./img/fig_sol_analytic_out_index_vs_delta.pdf')
plt.show()


###############################################################################
###############################################################################
# fig, ax = plt.subplots(figsize=(12, 6))
# fr_list = np.logspace(0.0, 3.0, 3001)
# sqlam_list = np.sqrt(2 * np.pi * fr_list * np.sqrt(mp * lp**4.0e0 / Bp))
# x1 = 1.0

# plt.plot(fr_list, np.abs(beam_disp_der_zero(x1, sqlam_list, beta, delta)), 'y--', label = '$\\delta =$ {}'.format(0.0))
# delta = 0.01
# plt.plot(fr_list, np.abs(beam_disp_der(x1, sqlam_list, beta, delta)), 'r-', label = '$\\delta =$ {}'.format(delta))
# delta = 0.1
# plt.plot(fr_list, np.abs(beam_disp_der(x1, sqlam_list, beta, delta)), 'b--', label = '$\\delta =$ {}'.format(delta))
# delta = 1
# plt.plot(fr_list, np.abs(beam_disp_der(x1, sqlam_list, beta, delta)), 'k-.', label = '$\\delta =$ {}'.format(delta))
# delta = 10
# plt.plot(fr_list, np.abs(beam_disp_der(x1, sqlam_list, beta, delta)), 'c-d', label = '$\\delta =$ {}'.format(delta))
# delta = 100
# plt.plot(fr_list, np.abs(beam_disp_der(x1, sqlam_list, beta, delta)), 'm-p', label = '$\\delta =$ {}'.format(delta))


# plt.legend(loc='lower right', ncol=2)
# plt.grid(True)
# # plt.xscale('log')
# plt.yscale('log')
# plt.xlabel('Base excitation frequency $f_b$', fontsize=16)
# plt.ylabel('Output index $\\chi_p$', fontsize=16)
# # plt.arrow(0.6, 0.7, -0.1, -0.4, transform=ax.transAxes, length_includes_head=True, head_width=0.05, head_length=0.1, fc='k', ec='k')
# plt.annotate('', xy=(0.5, 0.2), xytext=(0.6, 0.7), 
#             xycoords='axes fraction',
#             arrowprops=dict(facecolor='black', shrink=0.0)
#             )
# plt.text(0.55, 0.72, '$\\delta$ increases', 
#         transform=ax.transAxes, fontsize=16)


# plt.tight_layout()
# plt.savefig('./img/fig_sol_analytic_out_index_vs_fr.jpg',dpi=300)
# plt.savefig('./img/fig_sol_analytic_out_index_vs_fr.eps')
# plt.savefig('./img/fig_sol_analytic_out_index_vs_fr.pdf')
# plt.show()




































































