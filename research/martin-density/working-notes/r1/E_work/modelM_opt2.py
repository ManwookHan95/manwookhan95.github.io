import numpy as np
from modelM import solve_scale, profile_f
from modelM_opt import nelder_mead, sup_profile_fprime

r = 0.5; M = 0.5; A = 1.0; B = 0.5
taus_wide = np.exp(np.linspace(np.log(r**12), np.log(r**-30), 260))
tf, vf = profile_f(r, 1.0, A, B, M)
gf = vf.max()
print("sup P_f =", gf)
# geometric ansatz x_fr_i proportional to q^{-i} for i in [-J+1, 0], i.e. finest gets most
for J in [5, 8, 12]:
    best = None
    for q in [0.2, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6]:
        w = q**np.arange(J-1, -1, -1).astype(float)   # coarse..fine: q^{J-1},...,1
        w = w/w.sum()
        v = sup_profile_fprime(w[:-1], r, A, B, M, taus_wide, J)
        if best is None or v < best[1]: best = (q, v)
    print(f"J={J}: best geometric ansatz q={best[0]}  sup P_f'={best[1]:.4f}  R={best[1]/gf:.4f}")
