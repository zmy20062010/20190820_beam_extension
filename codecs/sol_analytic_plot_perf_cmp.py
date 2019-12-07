import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.ticker as ticker
import matplotlib.colors as colors

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
fr   = 40
Rl   = 1e6


Bp = 2.0e0/3.0e0 * b * ( Ys*hs**3.0e0 + c11E*((hs+hp)**3.0e0 - hs**3.0e0) )
Cp = ep33S * b * lp / 2.0e0 / hp
ep = b * e31 * (hs + hp/2.0e0)
mp = 2.0e0 * b * ( rhos * hs + rhop * hp )

# # dimensionless parameters
# alpha = ep * np.sqrt(lp / Cp / Bp)
# beta  = Rl * Cp * np.sqrt(Bp / mp / lp**4.0e0)
# nu    = 2 * np.pi * fr * np.sqrt(mp * lp**4.0e0 / Bp)

# sqlam = np.sqrt(nu)

# delta = alpha*alpha

xib = 0.5e-3
# rd = xib / lp
# rv = ep / Cp


def output_vals(arg_fr=fr, arg_Rl=Rl, arg_ep=ep, arg_Cp=Cp, arg_xib=xib, arg_lp=lp, arg_Bp=Bp, arg_mp=mp):

    alpha = arg_ep * np.sqrt(arg_lp / arg_Cp / arg_Bp)
    delta = alpha*alpha
    beta  = arg_Rl * arg_Cp * np.sqrt(arg_Bp / arg_mp / arg_lp**4.0e0)
    nu    = 2 * np.pi * arg_fr * np.sqrt(arg_mp * arg_lp**4.0e0 / arg_Bp)
    sqlam = np.sqrt(nu)

    rd    = arg_xib / arg_lp
    rv    = arg_ep / arg_Cp

    #########  Closed form solutions
    coeff_denom = 2.0 * ( 1 + np.cos(sqlam)*np.cosh(sqlam) + ( 1j * beta * sqlam * delta) / (1 + 1j * beta * sqlam * sqlam ) * ( np.sin(sqlam)*np.cosh(sqlam) + np.cos(sqlam)*np.sinh(sqlam) ) )
    Aef = ( 1 + np.cos(sqlam)*np.cosh(sqlam) - np.sin(sqlam)*np.sinh(sqlam) + ( 2 * 1j * beta * sqlam * delta) / (1 + 1j * beta * sqlam * sqlam ) * np.cos(sqlam)*np.sinh(sqlam) ) / coeff_denom
    Bef = ( np.sin(sqlam)*np.cosh(sqlam) + np.cos(sqlam)*np.sinh(sqlam) + ( 2 * 1j * beta * sqlam * delta) / (1 + 1j * beta * sqlam * sqlam ) * np.sin(sqlam)*np.sinh(sqlam) ) / coeff_denom
    Cef = 1.0 - Aef
    Def = - Bef
    #########  Expansion for the function
    ue1 = sqlam * ( - Aef * np.sin(sqlam) + Bef * np.cos(sqlam) + Cef * np.sinh(sqlam) + Def * np.cosh(sqlam) )
    ve = -( 1j * beta * sqlam * sqlam) / (1 + 1j * beta * sqlam * sqlam ) * rd * rv * ue1
    ie = ve / arg_Rl
    pe = ve * ie

    return [ue1, ve, ie, pe]



###############################################################################
###############################################################################
###     output performance metrics versus frequency
###############################################################################
###############################################################################
# plt.figure(1, figsize=(18,9))
# fr_list  = np.logspace(0,3,3001)
# wr_list  = 2 * np.pi * fr_list
# Rl    = 1e3

# plt.subplot(211)
# delta = 0.01
# ep    = np.sqrt(delta) / np.sqrt(lp / Cp / Bp)
# vol_list = output_vals(fr_list, Rl, ep)[1]
# plt.plot(fr_list, np.abs(vol_list)/xib/wr_list/wr_list, 'r-', label = '$\\delta =$ {0}, $R_l = $ {1}'.format(delta,Rl))

# delta = 0.1
# ep    = np.sqrt(delta) / np.sqrt(lp / Cp / Bp)
# vol_list = output_vals(fr_list, Rl, ep)[1]
# plt.plot(fr_list, np.abs(vol_list)/xib/wr_list/wr_list, 'b-.', label = '$\\delta =$ {0}, $R_l = $ {1}'.format(delta,Rl))

# delta = 1
# ep    = np.sqrt(delta) / np.sqrt(lp / Cp / Bp)
# vol_list = output_vals(fr_list, Rl, ep)[1]
# plt.plot(fr_list, np.abs(vol_list)/xib/wr_list/wr_list, 'k--', label = '$\\delta =$ {0}, $R_l = $ {1}'.format(delta,Rl))

# delta = 10
# ep    = np.sqrt(delta) / np.sqrt(lp / Cp / Bp)
# vol_list = output_vals(fr_list, Rl, ep)[1]
# plt.plot(fr_list, np.abs(vol_list)/xib/wr_list/wr_list, 'c-.', label = '$\\delta =$ {0}, $R_l = $ {1}'.format(delta,Rl))

# delta = 100
# ep    = np.sqrt(delta) / np.sqrt(lp / Cp / Bp)
# vol_list = output_vals(fr_list, Rl, ep)[1]
# plt.plot(fr_list, np.abs(vol_list)/xib/wr_list/wr_list, 'm--', label = '$\\delta =$ {0}, $R_l = $ {1}'.format(delta,Rl))

# plt.xlabel('Base excitation frequency $f_b$ ($Hz$)')
# plt.ylabel('Normalized output voltage $| \\tilde{V}_p/(\\sigma_b^2 \\xi_b) |$ ($V \\cdot s^2 / m$)')
# plt.yscale('log')
# plt.grid(True)
# plt.legend(loc = 'best')


# plt.subplot(212)
# delta = 0.01
# ep    = np.sqrt(delta) / np.sqrt(lp / Cp / Bp)
# pow_list = output_vals(fr_list, Rl, ep)[3]
# plt.plot(fr_list, np.abs(pow_list)/xib/wr_list/wr_list, 'r-', label = '$\\delta =$ {0}, $R_l = $ {1}'.format(delta,Rl))

# delta = 0.1
# ep    = np.sqrt(delta) / np.sqrt(lp / Cp / Bp)
# pow_list = output_vals(fr_list, Rl, ep)[3]
# plt.plot(fr_list, np.abs(pow_list)/xib/wr_list/wr_list, 'b-.', label = '$\\delta =$ {0}, $R_l = $ {1}'.format(delta,Rl))

# delta = 1
# ep    = np.sqrt(delta) / np.sqrt(lp / Cp / Bp)
# pow_list = output_vals(fr_list, Rl, ep)[3]
# plt.plot(fr_list, np.abs(pow_list)/xib/wr_list/wr_list, 'k--', label = '$\\delta =$ {0}, $R_l = $ {1}'.format(delta,Rl))

# delta = 10
# ep    = np.sqrt(delta) / np.sqrt(lp / Cp / Bp)
# pow_list = output_vals(fr_list, Rl, ep)[3]
# plt.plot(fr_list, np.abs(pow_list)/xib/wr_list/wr_list, 'c-.', label = '$\\delta =$ {0}, $R_l = $ {1}'.format(delta,Rl))

# delta = 100
# ep    = np.sqrt(delta) / np.sqrt(lp / Cp / Bp)
# pow_list = output_vals(fr_list, Rl, ep)[3]
# plt.plot(fr_list, np.abs(pow_list)/xib/wr_list/wr_list, 'm--', label = '$\\delta =$ {0}, $R_l = $ {1}'.format(delta,Rl))

# plt.xlabel('Base excitation frequency $f_b$ ($Hz$)')
# plt.ylabel('Output power $|\\tilde{P}_p|$')
# plt.yscale('log')
# plt.grid(True)
# plt.legend(loc = 'best')


# plt.tight_layout()
# plt.show()



###############################################################################
###############################################################################
###     output performance metrics versus delta
###############################################################################
###############################################################################

# plt.figure(2, figsize=(18,9))
# delta_list  = np.logspace(-4,4,801)
# ep_list     = np.sqrt(delta_list) / np.sqrt(lp / Cp / Bp)
# Rl    = 1e3

# plt.subplot(211)
# fr = 20
# wr = 2 * np.pi * fr
# vol_list = output_vals(fr, Rl, ep_list)[1]
# plt.plot(delta_list, np.abs(vol_list)/xib/wr/wr, 'r-', label = '$f_b =$ {0}, $R_l = $ {1}'.format(fr,Rl))

# plt.subplot(211)
# fr = 40
# wr = 2 * np.pi * fr
# vol_list = output_vals(fr, Rl, ep_list)[1]
# plt.plot(delta_list, np.abs(vol_list)/xib/wr/wr, 'b-', label = '$f_b =$ {0}, $R_l = $ {1}'.format(fr,Rl))

# plt.subplot(211)
# fr = 60
# wr = 2 * np.pi * fr
# vol_list = output_vals(fr, Rl, ep_list)[1]
# plt.plot(delta_list, np.abs(vol_list)/xib/wr/wr, 'k-', label = '$f_b =$ {0}, $R_l = $ {1}'.format(fr,Rl))

# plt.subplot(211)
# fr = 80
# wr = 2 * np.pi * fr
# vol_list = output_vals(fr, Rl, ep_list)[1]
# plt.plot(delta_list, np.abs(vol_list)/xib/wr/wr, 'c-', label = '$f_b =$ {0}, $R_l = $ {1}'.format(fr,Rl))

# plt.subplot(211)
# fr = 100
# wr = 2 * np.pi * fr
# vol_list = output_vals(fr, Rl, ep_list)[1]
# plt.plot(delta_list, np.abs(vol_list)/xib/wr/wr, 'm-', label = '$f_b =$ {0}, $R_l = $ {1}'.format(fr,Rl))


# plt.xscale('log')
# plt.xlabel('Electromechanical coupling factor $\\delta$')
# plt.ylabel('Normalized output voltage $| \\tilde{V}_p/(\\sigma_b^2 \\xi_b) |$ ($V \\cdot s^2 / m$)')
# plt.grid(True)
# plt.legend(loc = 'best')
# plt.yscale('log')
# # plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))


# plt.subplot(212)
# fr = 20
# wr = 2 * np.pi * fr
# pow_list = output_vals(fr, Rl, ep_list)[3]
# plt.plot(delta_list, np.abs(pow_list)/xib/wr/wr, 'r-', label = '$f_b =$ {0}, $R_l = $ {1}'.format(fr,Rl))

# fr = 40
# wr = 2 * np.pi * fr
# pow_list = output_vals(fr, Rl, ep_list)[3]
# plt.plot(delta_list, np.abs(pow_list)/xib/wr/wr, 'b-', label = '$f_b =$ {0}, $R_l = $ {1}'.format(fr,Rl))

# fr = 60
# wr = 2 * np.pi * fr
# pow_list = output_vals(fr, Rl, ep_list)[3]
# plt.plot(delta_list, np.abs(pow_list)/xib/wr/wr, 'k-', label = '$f_b =$ {0}, $R_l = $ {1}'.format(fr,Rl))

# fr = 80
# wr = 2 * np.pi * fr
# pow_list = output_vals(fr, Rl, ep_list)[3]
# plt.plot(delta_list, np.abs(pow_list)/xib/wr/wr, 'c-', label = '$f_b =$ {0}, $R_l = $ {1}'.format(fr,Rl))

# fr = 100
# wr = 2 * np.pi * fr
# pow_list = output_vals(fr, Rl, ep_list)[3]
# plt.plot(delta_list, np.abs(pow_list)/xib/wr/wr, 'm-', label = '$f_b =$ {0}, $R_l = $ {1}'.format(fr,Rl))

# plt.xscale('log')
# plt.xlabel('Electromechanical coupling factor $\\delta$')
# plt.ylabel('Normalized output power $| \\tilde{P}_p/(\\sigma_b^2 \\xi_b) |$ ($V \\cdot s^2 / m$)')
# plt.grid(True)
# plt.legend(loc = 'best')
# plt.yscale('log')
# # plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))


# plt.tight_layout()

# plt.show()





###############################################################################
###############################################################################
###     output performance metrics versus delta and f_b contour plot
###############################################################################
###############################################################################


plt.figure(3, figsize=(12,6))
delta_list = np.logspace(-4,4,801)
ep_list    = np.sqrt(delta_list) / np.sqrt(lp / Cp / Bp)
Rl    = 1e3
fr_list    = np.logspace(0,3,301)
list_fr, list_ep    = np.meshgrid(fr_list, ep_list)
list_fr, list_delta = np.meshgrid(fr_list, delta_list)

list_out = output_vals(list_fr, Rl, list_ep)


plt.contourf(list_fr, list_delta, np.abs(list_out[3]), levels=np.logspace(-20,6,53), locator=ticker.LogLocator(), cmap=cm.jet)
# plt.contourf(list_fr, list_delta, np.abs(list_out[3]), locator=ticker.LogLocator(), cmap=cm.jet)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Base excitation frequency $f_b$ $(Hz)$', fontsize=16)
plt.ylabel('Electromechanical coupling factor $\\delta$', fontsize=16)
plt.colorbar(orientation="vertical", fraction=0.05)
plt.axis(aspect='image')
plt.tight_layout()
plt.savefig('./img/fig_sol_analytic_out_vol_contour.jpg',dpi=300)
plt.savefig('./img/fig_sol_analytic_out_vol_contour.eps')
plt.savefig('./img/fig_sol_analytic_out_vol_contour.pdf')
# plt.show()





plt.figure(4, figsize=(12,6))
delta_list = np.logspace(-4,4,801)
ep_list    = np.sqrt(delta_list) / np.sqrt(lp / Cp / Bp)
Rl    = 1e3
fr_list    = np.logspace(0,3,301)
list_fr, list_ep    = np.meshgrid(fr_list, ep_list)
list_fr, list_delta = np.meshgrid(fr_list, delta_list)

list_out = output_vals(list_fr, Rl, list_ep)

plt.contourf(list_fr, list_delta, np.abs(list_out[1]), levels=np.logspace(-9,5,57), locator=ticker.LogLocator(), cmap=cm.jet)
# plt.contourf(list_fr, list_delta, np.abs(list_out[1]), locator=ticker.LogLocator(), cmap=cm.jet)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Base excitation frequency $f_b$ $(Hz)$', fontsize=16)
plt.ylabel('Electromechanical coupling factor $\\delta$', fontsize=16)
plt.colorbar(orientation="vertical", fraction=0.05)
plt.axis(aspect='image')
plt.tight_layout()
plt.savefig('./img/fig_sol_analytic_out_pow_contour.jpg',dpi=300)
plt.savefig('./img/fig_sol_analytic_out_pow_contour.eps')
plt.savefig('./img/fig_sol_analytic_out_pow_contour.pdf')
plt.show()