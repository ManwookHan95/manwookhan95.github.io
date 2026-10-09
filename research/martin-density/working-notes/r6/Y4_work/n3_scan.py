import sys, numpy as np
from n3_ray import build, ray_module, min_switch
from toy import s_of
for eps_rel in [1.0, 0.1, 0.01, 0.001]:
    M, D, l1, l2 = build(eps_rel)
    ts = np.geomspace(3e-3, 1.0, 12)
    best = None
    for c in [0.01, 0.015, 0.02, 0.022, 0.024, 0.026, 0.028]:
        g, om = ray_module(M, D, l1, l2, c)
        worst = max(max(M.pstar(D['f'] + t * g), M.pstar(D['f'] - t * g)) - s_of(t) for t in ts)
        if worst <= 1e-7: best = (c, g)
    if best is None:
        print(f"eps_rel={eps_rel}: no valid c in scan"); continue
    c, g = best
    vals = [min_switch(M, D, g, l1, l2, t)[0] for t in ts]
    print(f"eps_rel={eps_rel}: largest valid c={c}; max_t min-switch/t = {max(vals):.3e} at t={ts[int(np.argmax(vals))]:.2e}; "
          f"profile: " + " ".join(f"{v:.1e}" for v in vals))
