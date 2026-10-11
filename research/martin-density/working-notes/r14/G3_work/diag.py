import numpy as np
from selfpin import build, tune, Dval
from conserve import solve_switch
np.set_printoptions(precision=4, suppress=True, linewidth=160)
for name, Dt in [('D=0 thick', 0.0), ('D=-0.004 thick', -0.004), ('D=-0.001 thick', -0.001)]:
    row, rr = tune(Dt, 'thick', 0.15)
    D, val, w = Dval(row)
    print(f"\n== {name}: r_mass={rr:.4f} D={D:.3e} val={val} wblk={row.w} peaks={row.peaks()} sigma={row.sigma:.4f} q0={row.q0:.4f}")
    for t in [3e-2, 1e-2]:
        v, st, Ap, Am, Wp, Wm = solve_switch(row, t, 0, +1)
        gam = row.lam * ((row.w - Wm) / t - (Wp - row.w) / t)
        V = (Ap + Am - 2 * row.a) / t
        print(f"  t={t}: [{st}] gamma={gam}  ")
        print(f"     V={V}")
        print(f"     Wp-w={(Wp-row.w)/t}  w-Wm={(row.w-Wm)/t}")
        print(f"     |Wp|max={np.abs(Wp).max():.5f} |Wm|max={np.abs(Wm).max():.5f} s(t)={np.sqrt(1+t*t):.6f}")
