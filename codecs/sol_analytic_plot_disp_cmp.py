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


Bp = 2.0e0/3.0e0 * b * ( Ys*hs**3.0e0 + c11E*( (hs+hp)**3.0e0 - hs**3.0e0) )
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

print(delta)

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

# plt.figure(1, figsize=(16,8))
# plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = 'closed form')
# plt.show()

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

def beam_disp_one(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
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

def beam_disp_two(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
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



fr   = 1
Rl   = 50.0e3
# dimensionless parameters
alpha = ep * np.sqrt(lp / Cp / Bp)
beta  = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
nu    = 2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp)

delta = alpha*alpha
sqlam = np.sqrt(nu)

plt.figure(1, figsize=(24,32))
plt.subplot(7,3,1)
delta = 0.01
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,2)
delta = 0.1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,3)
delta = 1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))



fr   = 20
Rl   = 50.0e3
# dimensionless parameters
alpha = ep * np.sqrt(lp / Cp / Bp)
beta  = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
nu    = 2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp)

delta = alpha*alpha
sqlam = np.sqrt(nu)

plt.subplot(7,3,4)
delta = 0.01
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,5)
delta = 0.1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,6)
delta = 1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))




fr   = 80
Rl   = 40.0e3
# dimensionless parameters
alpha = ep * np.sqrt(lp / Cp / Bp)
beta  = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
nu    = 2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp)

delta = alpha*alpha
sqlam = np.sqrt(nu)

plt.subplot(7,3,7)
delta = 0.01
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,8)
delta = 0.1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,9)
delta = 1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))




fr   = 45
Rl   = 50.0e3
# dimensionless parameters
alpha = ep * np.sqrt(lp / Cp / Bp)
beta  = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
nu    = 2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp)

delta = alpha*alpha
sqlam = np.sqrt(nu)

plt.subplot(7,3,10)
delta = 0.01
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,11)
delta = 0.1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,12)
delta = 1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))






fr   = 60
Rl   = 50.0e3
# dimensionless parameters
alpha = ep * np.sqrt(lp / Cp / Bp)
beta  = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
nu    = 2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp)

delta = alpha*alpha
sqlam = np.sqrt(nu)

plt.subplot(7,3,13)
delta = 0.01
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,14)
delta = 0.1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,15)
delta = 1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))




fr   = 80
Rl   = 50.0e3
# dimensionless parameters
alpha = ep * np.sqrt(lp / Cp / Bp)
beta  = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
nu    = 2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp)

delta = alpha*alpha
sqlam = np.sqrt(nu)

plt.subplot(7,3,16)
delta = 0.01
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,17)
delta = 0.1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


plt.subplot(7,3,18)
delta = 1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))




fr   = 100
Rl   = 50.0e3
# dimensionless parameters
alpha = ep * np.sqrt(lp / Cp / Bp)
beta  = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
nu    = 2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp)

delta = alpha*alpha
sqlam = np.sqrt(nu)

plt.subplot(7,3,19)
delta = 0.01
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
plt.xlabel('Streamwise position $z$',fontsize=16)

plt.subplot(7,3,20)
delta = 0.1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
plt.xlabel('Streamwise position $z$',fontsize=16)


plt.subplot(7,3,21)
delta = 1
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = '$u(z;\\delta)$')
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta, delta)), 'b-.', label = '$u^{(0)}(z)$')
plt.plot(x, np.abs(beam_disp_one(x, sqlam, beta, delta)), 'k-', label = '$u^{(1)}(z)$')
plt.plot(x, np.abs(beam_disp_two(x, sqlam, beta, delta)), 'm-.', label = '$u^{(2)}(z)$')
plt.legend(loc = 'upper left',fontsize=16)
plt.grid(True)
plt.title('$\\delta = $ {0}, $\\sigma = $ {1:1.2f}, $f_b = $ {2} $Hz$'.format(delta,nu, fr),fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
plt.xlabel('Streamwise position $z$',fontsize=16)




























































































































































plt.tight_layout()
# plt.savefig('./img/fig_sol_analytic_disp_cmp_fr045.jpg',dpi=300)
# plt.savefig('./img/fig_sol_analytic_disp_cmp_fr045.eps')
# plt.savefig('./img/fig_sol_analytic_disp_cmp_fr045.pdf')

# plt.savefig('./img/fig_sol_analytic_disp_cmp_fr_all.jpg',dpi=300)
plt.savefig('./img/fig_sol_analytic_disp_cmp_fr_all.eps')
plt.savefig('./img/fig_sol_analytic_disp_cmp_fr_all.pdf')

plt.show()




































































