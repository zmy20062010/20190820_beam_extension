import numpy as np
import matplotlib.pyplot as plt


# beam base structure material constants
lp   =  100.0e-3
Ys   =  100.0e9
rhos =  7.165e3
hs   =  0.5e-3
b    =  20.0e-3
# piezo layer material constants
Yp   = 66.0e9
rhop = 7.8e3
hp   = 0.4e-3
ep33S= 15.93e-9
d31  = -190.0e-12
e31  = d31 * Yp
# intermediate quantities
n    = Ys / Yp
hpa  = (hp*hp + 2.0*n*hp*hs + n*hs*hs)/2.0/(hp + n*hs)
hsa  = (hp*hp + 2.0*hp*hs + n*hs*hs)/2.0/(hp + n*hs)
hpc  = n*hs*(hp + hs)/2.0/(hp + n*hs)
ha   = -hsa
hb   = hpa - hp
hc   = hpa


Bp = b/3.0*( Ys*(hb**3.0-ha**3.0) + Yp*(hc**3.0-hb**3.0) )
Cp = ep33S * b * lp / hp
ep = Yp*d31*b/2.0/hp*(hc*hc - hb*hb)
mp = b * ( rhos * hs + rhop * hp )

# external circuit and excitation
fr   = 150
Rl   = 1000.0e3

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

def beam_disp_der1(x, arg_sqlam = sqlam, arg_beta = beta, arg_delta = delta):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Ae = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Be = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_delta) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Ce = 1.0 - Ae
    De = - Be
    #########  Expansion for the function
    ue = -Ae*np.sin(arg_sqlam*x) + Be*np.cos(arg_sqlam*x) + Ce*np.sinh(arg_sqlam*x) + De*np.cosh(arg_sqlam*x)
    ue = ue * arg_sqlam
    return ue


# plt.figure(1, figsize=(16,8))
# plt.plot(x, np.abs(beam_disp(x, sqlam, beta, delta)), 'r-', label = 'closed form')
# plt.show()


plt.figure(1, figsize=(16,8))
plt.plot(fr_list, np.abs(beam_disp_der1(1.0, sqlam_list, beta, delta)), 'r-', label = 'closed form')
plt.yscale('log')
plt.show()
























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
