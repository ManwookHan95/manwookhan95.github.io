"""Two-regime profile (Corollary 1.8 / Lemma 2.8(c)): thick anti-aligned coordinate r, oriented minor D of either sign.
Predicted: D > 0 (wrong sign): gamma'_+ order one for t >> D, pinned (<= C t/D) for t << D;  D <= 0: free."""
import numpy as np, warnings
warnings.filterwarnings('ignore')
import cvxpy as cp
import model
from selfpin import tune, Dval
ts = [3e-2, 1e-2, 3e-3, 1e-3, 3e-4]
for Dt in [1e-3, 1e-4, 0.0, -1e-4]:
    row, rr = tune(Dt, 'thick', 0.15)
    D, val, w = Dval(row)
    sl = abs(val[1])/(2*row.q0*D) if D > 0 else float('inf')
    print(f"\n== THICK r, D={D:.2e}  val={val.round(4)}  peaks={row.peaks()}  j-bound slope |val_-|/(2 q0 D)={sl:.1f}")
    for t in ts:
        try:
            g, st = row.max_switch(t, 0, +1)
        except Exception as ex:
            model.SOLVER = dict(solver=cp.SCS, eps=1e-9, max_iters=200000)
            g, st = row.max_switch(t, 0, +1)
            model.SOLVER = dict(solver=cp.CLARABEL)
            st = 'SCS:' + st
        print(f"   t={t:7.1e}  max gamma'_+ = {g:10.4e}  /t = {g/t:10.2f}  [{st}]")
