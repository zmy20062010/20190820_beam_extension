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


plt.figure(1, figsize=(12,6))
print(sqlam,beta,eps)
plt.subplot(121)
plt.plot(x, np.abs(beam_disp_zero(x, sqlam, beta)), 'm-', label = '$\\delta = 0.0$')
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 0.01)), 'b-.', label = '$\\delta = 0.01$')
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 0.1)), 'g-.', label = '$\\delta = 0.1$')
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 1.0)), 'k-.', label = '$\\delta = 1.0$')
plt.plot(x, np.abs(beam_disp(x, sqlam, beta, 10.0)), 'c-', label = '$\\delta = 10.0$')
plt.plot(x, np.abs(beam_disp_infty(x, sqlam, beta)), 'y-', label = '$\\delta = \\infty$')
plt.grid(True)
plt.legend(loc='best')
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.ylabel('Amplitude function')
plt.xlabel('Streamwise position $z$')


plt.subplot(122)
plt.plot(x, np.angle(beam_disp_zero(x, sqlam, beta)), 'm-', label = '$\\delta = 0.0$')
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 0.01)), 'b-.', label = '$\\delta = 0.01$')
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 0.1)), 'g-.', label = '$\\delta = 0.1$')
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 1.0)), 'k-.', label = '$\\delta = 1.0$')
plt.plot(x, np.angle(beam_disp(x, sqlam, beta, 10.0)), 'c-', label = '$\\delta = 10.0$')
plt.plot(x, np.angle(beam_disp_infty(x, sqlam, beta)), 'y-', label = '$\\delta = \\infty$')
plt.grid(True)
plt.legend(loc='best')
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.xlabel('Streamwise position $z$')
plt.ylabel('Phase angle function')
plt.tight_layout()


plt.savefig('fig_sol_analytic_disp_fun.jpg',dpi=300)
plt.savefig('fig_sol_analytic_disp_fun.eps')
plt.savefig('fig_sol_analytic_disp_fun.pdf')
# plt.show()









def output_vals(arg_sqlam = sqlam, arg_beta = beta, arg_eps = eps, arg_rd = rd, arg_rv = rv, arg_Rl = Rl):
    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) + ( 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) )  )
    Aef = ( 1 + np.cos(arg_sqlam)*np.cosh(arg_sqlam) - np.sin(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.cos(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Bef = ( np.sin(arg_sqlam)*np.cosh(arg_sqlam) + np.cos(arg_sqlam)*np.sinh(arg_sqlam) + ( 2 * 1j * arg_beta * arg_sqlam * arg_eps) / (1 + 1j * arg_beta * arg_sqlam * arg_sqlam ) * np.sin(arg_sqlam)*np.sinh(arg_sqlam) ) / coeff_denom
    Cef = 1.0 - Aef
    Def = - Bef

    #########  Expansion for the function
    ue1 = arg_sqlam * ( - Aef * np.sin(arg_sqlam) + Bef * np.cos(arg_sqlam) + Cef * np.sinh(arg_sqlam) + Def * np.cosh(arg_sqlam) )
    ve = -( 1j * arg_beta * arg_sqlam * arg_sqlam) / (1 + 1j * beta * arg_sqlam * arg_sqlam ) * arg_rd * arg_rv * ue1
    ie = ve / arg_Rl
    pe = ve * ie

    return [ve, ie, pe]

plt.figure(2, figsize=(16,6))

eps_list = np.logspace(-4,0,401)
plt.subplot(131)
plt.plot(eps_list, np.abs(output_vals(sqlam, beta, eps_list)[0]), 'r-', label = 'voltage $\\tilde{V}_p$')
# plt.xscale('log')
# plt.yscale('log')
plt.grid(True)
plt.legend()
plt.xlabel('Electromechanical coupling factor $\\delta$')
plt.ylabel('Output voltage $\\tilde{V}_p$')


plt.subplot(132)
plt.plot(eps_list, np.abs(output_vals(sqlam, beta, eps_list)[1]), 'b-', label = 'Current $\\tilde{I}_p$')
# plt.xscale('log')
# plt.yscale('log')
plt.grid(True)
plt.legend()
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.xlabel('Electromechanical coupling factor $\\delta$')
plt.ylabel('Output current $\\tilde{I}_p$')


plt.subplot(133)
plt.plot(eps_list, np.abs(output_vals(sqlam, beta, eps_list)[2]), 'k-', label = 'Power $\\tilde{P}_p$')
# plt.xscale('log')
# plt.yscale('log')
plt.grid(True)
plt.legend()
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.xlabel('Electromechanical coupling factor $\\delta$')
plt.ylabel('Output power $\\tilde{P}_p$')


plt.tight_layout()

plt.savefig('fig_sol_analytic_perf_fun.jpg',dpi=300)
plt.savefig('fig_sol_analytic_perf_fun.eps')
plt.savefig('fig_sol_analytic_perf_fun.pdf')

plt.show()






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