import numpy as np
import scipy as sp
import h5py
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')
plt.rcParams['xtick.major.size'] = 0.7*4.0
plt.rcParams['xtick.major.width'] = 2*0.5
plt.rcParams['xtick.minor.size'] = 0.7*2.5
plt.rcParams['xtick.minor.width'] = 2*0.5
plt.rcParams['ytick.major.size'] = 0.7*4.0
plt.rcParams['ytick.major.width'] = 2*0.5
plt.rcParams['ytick.minor.size'] = 0.7*2.5
plt.rcParams['ytick.minor.width'] = 2*0.5
A=2*9.3#1.5*9.3
font = {'family' : 'serif', 'weight' : 'normal', 'size' : A}
plt.rc('font', **font)

fig, axes = plt.subplots(figsize = (8, 6))

def vector_multiply(A, B):
    return(A*B)


with h5py.File("ekTk.h5",'r') as f:
     Tk = f['Tk'][()]

     t = f['t'][()]

i = 0

Tk_sum = 0

count = 0

while i < np.shape(Tk_zp)[0]:
    Tk_sum += Tk[i, :]
    
    i += 1

    count += 1


Tk_avg = Tk_sum/count

P_u = -np.cumsum(Tk_avg)

k = np.arange(0, np.shape(P_u)[0], 1)


axes.plot(k, P_u, "r", lw = 2, label=r"$\Pi(k)$")

axes.set_yscale("symlog", linthresh=1e-4)

axes.set_xscale("log")

axes.set_xlabel("$k$")
axes.set_ylabel(r"$\Pi(k)$")

axes.set_xlim(1, 4096/3)

plt.legend(fontsize=A, ncol=2, scatterpoints=1, loc="lower right", frameon=False)

plt.tight_layout()
plt.savefig("flux.pdf", dpi=600)
plt.show()


