"""cert2 (DC-c): gap preservation needs |C'-C| <= C gap/(2(1-gap)), not |C'-C| <= gap/4 (X2 Lemma DC step (5), UE-1(c)).
Block with C ~ 0.1, an Omega carrier k0 near threshold (gap ~ 1e-2); keep its normalized value nv EXACT (d-consistency) and move C by
raising another (non-Omega) carrier's value; observe gap' from the identity and from the solver."""
import numpy as np
from dc_cert import block_norming
Phi = np.array([0.05, 0.08, 0.30, 0.10, 0.25])
lam = Phi.copy()                                   # block m = 1
base = np.array([2.0, -1.5, 0.0, 0.05, 0.02])      # carrier 2 = Omega carrier (value tuned below), 3 = non-Omega carrier we move
def solve(vals):
    B = block_norming(lam*vals, Phi); return B
# tune carrier 2 to be a strict non-peak with small gap
from scipy.optimize import brentq
def gap2(x):
    v = base.copy(); v[2] = x; B = solve(v); return B['M'] - abs(B['w'][2])
x0 = brentq(lambda x: gap2(x) - 0.01, 1e-4, 1.0)
v0 = base.copy(); v0[2] = x0; B0 = solve(v0)
nv0 = lam[2]*v0[2]/B0['A']; g0 = B0['M'] - abs(B0['w'][2])
print(f"f0: C {B0['C']:.4f} M {B0['M']:.4f} gap(k0) {g0:.4f} peaks {B0['P']}")
for dv in [0.0002, 0.0004, 0.0006, 0.0008, 0.001, 0.0012, 0.0015]:
    v = v0.copy(); v[3] += dv
    # restore nv(k0) exactly: v[2] scaled with A' (fixed point)
    for _ in range(200):
        B = solve(v); v[2] = nv0*B['A']/lam[2]
    B = solve(v); g1 = B['M'] - abs(B['w'][2]) if not B['P'][2] else -(abs(B['w'][2]) - B['M'])
    dC = B['C'] - B0['C']; pred = (B['C']/B0['C'])*g0 + 1 - B['C']/B0['C']
    print(f"dC = {dC:+.5f} (gap0/4 = {g0/4:.5f}; C gap0/2 = {B0['C']*g0/2:.5f})  k0 peak? {bool(B['P'][2])}  gap' (solver) {g1:+.5f}  identity {pred:+.5f}")
