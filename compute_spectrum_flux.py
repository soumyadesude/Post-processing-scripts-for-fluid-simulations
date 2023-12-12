import sys

sys.path.insert(0, '/home/soumyadeep/1024_sanganak_eps_5_spectrum/tarangPy')

import para as para
from lib.fields.vect_field import VectorField
from lib.solver_fns.compute_nlin_mhd import *
from lib.global_fns.universal import Universal_arrays
from lib.io.io_mhd import *
import h5py

if para.device == "gpu":
      import cupy as ncp 

      dev1 = ncp.cuda.Device(para.device_rank)

      dev1.use()
else:
      import numpy as ncp 

def main():
    if (para.dimension == 2):
        Vkx = ncp.zeros((para.Nx,(para.Nz)//2+1), dtype=complex)
        Vkz = ncp.zeros((para.Nx,(para.Nz)//2+1), dtype=complex)
        Vky = []

    time = ncp.loadtxt("tlist.txt")

    i = time[:] 

    U = VectorField()

    univ = Universal_arrays()

    U.set_arrays()
    W.set_arrays()
    univ.set_arrays()
    j =0

    while j < ncp.shape(i)[0]:

        with h5py.File("Soln_%f.h5"%(i[j]),'r') as f:
            Vkx = ncp.asarray(f['Vkx'][()])
            Vkz = ncp.asarray(f['Vkz'][()])

        t = i[j]

        U.init_cond(Vkx, Vkz, Vky)
    
        univ.compute_nlin_first_flag = True

        univ.compute_dt = False

        compute_nlin_mhd(t, U, univ)
        
        print(j)

        j += 1

    file_save_ekTk_mhd(U, univ)

    return()

if __name__ == "__main__":
    main()



