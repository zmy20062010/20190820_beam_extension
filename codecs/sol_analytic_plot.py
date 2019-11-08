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
# beam extension material constants
le   = 20e-3
Ye   = 2.3e9
rhoe = 1.38e3
he   = 0.25e-3
# external circuit and excitation
fr   = 48
Rl   = 900.0e3

Bp = 2.0e0/3.0e0 * b * ( Ys * hs**3.0e0 + c11E * ((hs + hp)**3.0e0) - hs**3.0e0 )
Be = 2.0e0/3.0e0 * b * Ye * he**3.0e0
Cp = ep33S * b * lp / 2.0e0 / hp
ep = b * e31 * (hs + hp/2.0e0)
mp = 2.0e0 * b * ( rhos * hs + rhop * hp )
me = 2.0e0 * b * rhoe * he

print(ep, lp / Cp / Bp)
# dimensionless parameters
alpha = ep * np.sqrt(lp / Cp / Bp)
beta  = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
nu    = 2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp)
wl    = 1.0 / np.sqrt(mp * lp**4.0e0 / Bp)
lamB  = Be / Bp
lamm  = me / mp
laml  = le / lp
lamh  = 0.0e0

eps = alpha*alpha
sqlam = np.sqrt(nu)

xib = 0.5e-3
rd = xib / lp
rv = ep / Cp














x = np.linspace(0.0, 1.0, 1001)

def beam_disp(x, arg_sqlam = sqlam, arg_beta = beta, arg_eps = eps):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * beta * arg_sqlam * eps) / (1 + 1j * beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * beta * arg_sqlam * eps) / (1 + 1j * beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * beta * arg_sqlam * eps) / (1 + 1j * beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = - Ae
    De = - Be

    #########  Expansion for the function
    ue = Ae * np.cos(arg_sqlam*x) + Be * np.sin(arg_sqlam*x) + Ce * np.cosh(arg_sqlam*x) + De * np.sinh(arg_sqlam*x)

    return ue

def output_vals(arg_sqlam = sqlam, arg_beta = beta, arg_eps = eps, arg_rd = rd, arg_rv = rv, arg_Rl = Rl):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * beta * arg_sqlam * eps) / (1 + 1j * beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Aef = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * beta * arg_sqlam * eps) / (1 + 1j * beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Bef = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * beta * arg_sqlam * eps) / (1 + 1j * beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Cef = - Aef
    Def = - Bef

    #########  Expansion for the function
    ue1 = ( - Aef * np.cos(arg_sqlam) + Bef * np.sin(arg_sqlam) + Cef * np.cosh(arg_sqlam) + Def * np.sinh(arg_sqlam) ) * arg_sqlam
    ve = ( 1j * beta * arg_sqlam * arg_sqlam * eps) / (1 + 1j * beta * arg_sqlam * arg_sqlam ) * arg_rd * arg_rv
    ie = ve / arg_Rl
    pe = ve * ie

    return [ve, ie, pe]

# plt.plot(x, np.abs(beam_disp(x)))
# plt.grid(True)
# plt.show()


sqlam_list = np.logspace(0.0,5.0,101)
plt.subplot(131)
plt.plot(sqlam_list, np.abs(output_vals(sqlam_list)[0]), 'r-', label = 'vol')
plt.xscale('log')

plt.subplot(132)
plt.plot(sqlam_list, np.abs(output_vals(sqlam_list)[1]), 'b-', label = 'cur')
plt.xscale('log')

plt.subplot(133)
plt.xscale('log')
plt.plot(sqlam_list, np.abs(output_vals(sqlam_list)[2]), 'k-', label = 'pow')
plt.xscale('log')
plt.grid(True)
plt.legend()
plt.show()

# print(output_vals())