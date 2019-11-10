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
fr   = 48
Rl   = 900.0e3


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

print(sqlam,beta,eps)
plt.subplot(211)
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 0.0)), 'm-', label = '$\\delta = 0.0$')
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 0.05)), 'b-.', label = '$\\delta = 0.05$')
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 0.1)), 'g-.', label = '$\\delta = 0.1$')
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 0.5)), 'c-.', label = '$\\delta = 0.5$')
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 1.0)), 'k-.', label = '$\\delta = 1.0$')
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 5.0)), 'r-', label = '$\\delta = 5.0$')
plt.grid(True)
plt.legend()
plt.ylabel('amplitude function')

plt.subplot(212)
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 0)), 'm-', label = '$\\delta = 0.0$')
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 0.05)), 'b-.', label = '$\\delta = 0.05$')
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 0.1)), 'g-.', label = '$\\delta = 0.1$')
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 0.5)), 'c-.', label = '$\\delta = 0.5$')
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 1.0)), 'k-.', label = '$\\delta = 1.0$')
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 5.0)), 'r-', label = '$\\delta = 5.0$')
plt.grid(True)
plt.legend()

plt.xlabel('Streamwise position $z$')
plt.ylabel('phase angle function')


plt.savefig('fig_sol_analytic_disp_fun.jpg',dpi=300)
plt.savefig('fig_sol_analytic_disp_fun.eps')
plt.savefig('fig_sol_analytic_disp_fun.pdf')
plt.show()









def output_vals(arg_sqlam = sqlam, arg_beta = beta, arg_eps = eps, arg_rd = rd, arg_rv = rv, arg_Rl = Rl):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Aef = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Bef = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Cef = 1.0 - Aef
    Def = - Bef

    #########  Expansion for the function
    ue1 = arg_sqlam * ( - Aef * np.cos(arg_sqlam) + Bef * np.sin(arg_sqlam) + Cef * np.cosh(arg_sqlam) + Def * np.sinh(arg_sqlam) )
    ve = -( 1j * arg_beta * arg_sqlam * arg_sqlam) / (1 + 1j * beta * arg_sqlam * arg_sqlam ) * arg_rd * arg_rv * ue1
    ie = ve / arg_Rl
    pe = ve * ie

    return [ve, ie, pe]



# sqlam_list = np.linspace(0.0,10.0,1001)
# plt.subplot(131)
# plt.plot(sqlam_list, np.abs(output_vals(sqlam_list)[0]), 'r-', label = 'vol')
# plt.xscale('log')
# plt.yscale('log')

# plt.subplot(132)
# plt.plot(sqlam_list, np.abs(output_vals(sqlam_list)[1]), 'b-', label = 'cur')
# plt.xscale('log')
# plt.yscale('log')

# plt.subplot(133)
# plt.xscale('log')
# plt.plot(sqlam_list, np.abs(output_vals(sqlam_list)[2]), 'k-', label = 'pow')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True)
# plt.legend()
# plt.show()






# sqlam_list = np.linspace(0.0,100.0,10001)
# outperfs = output_vals(sqlam_list, beta, 0.0)
# plt.plot(sqlam_list, np.abs(outperfs[0]), 'r-', label = 'vol')
# outperfs = output_vals(sqlam_list, beta, 0.05)
# plt.plot(sqlam_list, np.abs(outperfs[0]), 'g-', label = 'vol')
# outperfs = output_vals(sqlam_list, beta, 0.1)
# plt.plot(sqlam_list, np.abs(outperfs[0]), 'b-', label = 'vol')
# outperfs = output_vals(sqlam_list, beta, 0.5)
# plt.plot(sqlam_list, np.abs(outperfs[0]), 'c-', label = 'vol')
# outperfs = output_vals(sqlam_list, beta, 1.0)
# plt.plot(sqlam_list, np.abs(outperfs[0]), 'k-', label = 'vol')
# outperfs = output_vals(sqlam_list, beta, 5.0)
# plt.plot(sqlam_list, np.abs(outperfs[0]), 'm-', label = 'vol')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True)
# plt.show()