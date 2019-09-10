import numpy as np


def grabMaxExponent(values, precision=1):
    """Given a list of numericals, returns the exponent of the max
    value in scientific notation, adjusted to have no sig figs in
    decimal places.

    e.g. 190 > 1.9E+02 > 19E+01
    returns exponent (1)"""

    # Grab max value and convert to scientific notation
    str1 = "{" + ":.{}E".format(precision) +"}"
    value = str1.format(max(slist))

    # Pull exponent
    a,m = value.split('E+')
    a,b = a.split('.')
    a,b,m = map(int, (a,b,m))

    # If significant figures non-zero, increase exponent to bring them before decimal point
    if b > 0:
        m-=precision

    return m

slist = np.logspace(-1,2,31)

# str1 = "{" + ":.{}E".format(2) +"}"
# print(str1)
# print(str1.format(max(slist)))
# m = grabMaxExponent(slist)
# print(m)

precision=1
str1 = "{" + ":.{}E".format(precision) +"}"
value = str1.format(max(slist))

# Pull exponent
a,m = value.split('E')
print(a,m)
a,b = a.split('.')
print(a,b)
a,b,m = map(int, (a,b,m))
print(a,b,m)

# If significant figures non-zero, increase exponent to bring them before decimal point
if b > 0:
    m-=precision

print(m)


def plot_pow_fr_sl_Rl_sl_vs_laml():
    fig, axes = plt.subplots(ncols = 4, nrows = 6, figsize=(18,24), sharex=True)


    am_pplist = np.array([am_pplist00, am_pplist01, am_pplist02, am_pplist03,
                 am_pplist04, am_pplist05, am_pplist06, am_pplist07,
                 am_pplist08, am_pplist09, am_pplist10])
    am_pplist = np.array([am_pplist00, am_pplist01, am_pplist02, am_pplist03,
                 am_pplist04, am_pplist05, am_pplist06, am_pplist07,
                 am_pplist08, am_pplist09, am_pplist10])
    laml_list = np.linspace(0.0, 1.0, 11)
    # print(am_pplist.shape)
    # print(am_pplist.shape)
    # print(laml_list)
    class ScalarFormatterForceFormat(mtick.ScalarFormatter):
        def _set_format(self,vmin,vmax):  # Override function that finds format to use.
            self.format = "%1.2f"  # Give format here
    
    yfmt = ScalarFormatterForceFormat()
    yfmt.set_powerlimits((0,0))

    # ticklabel_format(self, *, axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)

    axes[0,0].plot(laml_list,am_pplist[:, 0, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 1 $\Omega$')
    axes[0,0].yaxis.set_major_formatter(yfmt)
    # axes[0,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[0,1].plot(laml_list,am_pplist[:, 2, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 100 $\Omega$')
    axes[0,1].yaxis.set_major_formatter(yfmt)
    # axes[0,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[0,2].plot(laml_list,am_pplist[:, 4, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[0,2].yaxis.set_major_formatter(yfmt)
    # axes[0,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[0,3].plot(laml_list,am_pplist[:, 6, 0], 'r-*', label='fr=1 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[0,3].yaxis.set_major_formatter(yfmt)
    # axes[0,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))


    axes[1,0].plot(laml_list,am_pplist[:, 0, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 1 $\Omega$')
    axes[1,0].yaxis.set_major_formatter(yfmt)
    # axes[1,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,1].plot(laml_list,am_pplist[:, 2, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 100 $\Omega$')
    axes[1,1].yaxis.set_major_formatter(yfmt)
    # axes[1,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,2].plot(laml_list,am_pplist[:, 4, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 10 $\Omega$')
    axes[1,2].yaxis.set_major_formatter(yfmt)
    # axes[1,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[1,3].plot(laml_list,am_pplist[:, 6, 100], 'r-*', label='fr=3.162 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[1,3].yaxis.set_major_formatter(yfmt)
    # axes[1,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[2,0].plot(laml_list,am_pplist[:, 0, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 1 $\Omega$')
    axes[2,0].yaxis.set_major_formatter(yfmt)
    # axes[2,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,1].plot(laml_list,am_pplist[:, 2, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 100 $\Omega$')
    axes[2,1].yaxis.set_major_formatter(yfmt)
    # axes[2,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,2].plot(laml_list,am_pplist[:, 4, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[2,2].yaxis.set_major_formatter(yfmt)
    # axes[2,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[2,3].plot(laml_list,am_pplist[:, 6, 200], 'r-*', label='fr=10 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[2,3].yaxis.set_major_formatter(yfmt)
    # axes[2,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[3,0].plot(laml_list,am_pplist[:, 0, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 1 $\Omega$')
    axes[3,0].yaxis.set_major_formatter(yfmt)
    # axes[3,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,1].plot(laml_list,am_pplist[:, 2, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 100 $\Omega$')
    axes[3,1].yaxis.set_major_formatter(yfmt)
    # axes[3,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,2].plot(laml_list,am_pplist[:, 4, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[3,2].yaxis.set_major_formatter(yfmt)
    # axes[3,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[3,3].plot(laml_list,am_pplist[:, 6, 300], 'r-*', label='fr=31.62 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[3,3].yaxis.set_major_formatter(yfmt)
    # axes[3,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[4,0].plot(laml_list,am_pplist[:, 0, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 1 $\Omega$')
    axes[4,0].yaxis.set_major_formatter(yfmt)
    # axes[4,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[4,1].plot(laml_list,am_pplist[:, 2, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 10 $\Omega$')
    axes[4,1].yaxis.set_major_formatter(yfmt)
    # axes[4,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[4,2].plot(laml_list,am_pplist[:, 4, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[4,2].yaxis.set_major_formatter(yfmt)
    # axes[4,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[4,3].plot(laml_list,am_pplist[:, 6, 325], 'r-*', label='fr=42.17 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[4,3].yaxis.set_major_formatter(yfmt)
    # axes[4,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    axes[5,0].plot(laml_list,am_pplist[:, 0, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 1 $\Omega$')
    axes[5,0].yaxis.set_major_formatter(yfmt)
    # axes[5,0].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[5,1].plot(laml_list,am_pplist[:, 2, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 100 $\Omega$')
    axes[5,1].yaxis.set_major_formatter(yfmt)
    # axes[5,1].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[5,2].plot(laml_list,am_pplist[:, 4, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 10 k$\Omega$')
    axes[5,2].yaxis.set_major_formatter(yfmt)
    # axes[5,2].ticklabel_format(axis='y', style='sci',scilimits=(0,0))
    axes[5,3].plot(laml_list,am_pplist[:, 6, 400], 'r-*', label='fr=100 $Hz$, $R_l$ = 1 M$\Omega$')
    axes[5,3].yaxis.set_major_formatter(yfmt)
    # axes[5,3].ticklabel_format(axis='y', style='sci',scilimits=(0,0))

    for i in range(6):
        for j in range(4):
            axes[i,j].legend(loc='best')