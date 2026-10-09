"""Referee check: FAR PULLS (flip a swallowing contact j in S_l0 to -eps and put a tiny mass of sign -eps there)
LOWER eps*u_l0(zhat) by 2 v_l0(j) at first order, leave the other carriers essentially unchanged, and cost
p*(f# - f) = O(v_l0(j)) (finite model; log factors invisible).  Also: with a DIAGONAL base, a bank (mass of sign z_j)
at a private signature contact j' of carrier l raises eps*u_l(zhat) and not the others.
Model: toy.Model (copied read-only from ../Y4_work), one block, diagonal U, F = {0}, maximal contact."""
import sys, numpy as np
sys.path.insert(0, '../Y4_work')
from toy import Model

n = 44
s = 0.8 * 2.0 ** (-0.12 * np.arange(n))
U = np.diag(s)
E = np.eye(n)
# carriers: 5 "peak-ish" carriers with targets on 1..6, 2 test carriers l0=5, l1=6 with targets on 7..10
targets = [0.8*E[1], -0.8*E[2], 0.6*E[3]+0.2*E[4], -0.7*E[5], 0.5*E[6]-0.3*E[1], 0.25*E[7]-0.1*E[8], 0.2*E[9]+0.15*E[10]]
sig_sets, nxt = [], 11
for k in range(len(targets)):
    sig_sets.append(list(range(nxt, nxt + 4))); nxt += 4
us, Phis = [], []
for k, y in enumerate(targets):
    h = np.zeros(n); h[sig_sets[k]] = 2.0 ** (-np.arange(1, 5))
    us.append(y + 0.15 * h); Phis.append(0.05 * 2.0 ** (-k) if k < 5 else 2e-3)
blk = dict(u=np.array(us), Phi=np.array(Phis), m=1)
M = Model(U, [blk])
a = np.zeros(n); a[0] = 1.0; a /= M.qstar(a)
z = np.ones(n)                      # maximal contact, all signs +1 (eps_l = +1 on every signature set)
D = M.first_row(a, z)
l0, l1 = 5, 6
w = D['w'][0]; Mm = D['M'][0]
print("status: |w(l0)|, |w(l1)|, M =", abs(w[l0]), abs(w[l1]), Mm)
def vals(Dd):
    return np.array([blk['u'][k] @ Dd['zhat'] for k in range(len(us))])
v0 = vals(D)
print(f"{'j':>3} {'v_l0(j)':>10} {'m_j':>9} {'d(u_l0)':>11} {'-2v(j)':>11} {'max|d u_other|':>14} {'p*(f#-f)':>10} {'ratio':>7}")
for j in sig_sets[l0]:
    vj = blk['u'][l0][j]
    for mfac in [0.5, 0.05]:
        mj = mfac * vj
        A = a.copy(); A[j] = -mj; A /= M.qstar(A)
        zs = z.copy(); zs[j] = -1.0
        Ds = M.first_row(A, zs)
        dv = vals(Ds) - v0
        other = np.max(np.abs(np.delete(dv, l0)))
        cost = M.pstar(Ds['f'] - D['f'])
        print(f"{j:3d} {vj:10.3e} {mj:9.2e} {dv[l0]:+11.4e} {-2*vj:+11.4e} {other:14.3e} {cost:10.3e} {cost/vj:7.3f}")
# private banks (diagonal U): mass m at j' in S_l0 with sign z_j' = +1
print("banks at a private signature contact (diagonal U):")
for jp in sig_sets[l0][:2]:
    for m in [1e-3, 1e-4]:
        A = a.copy(); A[jp] = m; A /= M.qstar(A)
        Ds = M.first_row(A, z)
        dv = vals(Ds) - v0
        pred = m * s[jp] ** 2 * blk['u'][l0][jp] / D['nu']
        print(f"  j'={jp} m={m:.0e}: d(u_l0)={dv[l0]:+.4e} predicted {pred:+.4e}; max|d u_other|={np.max(np.abs(np.delete(dv, l0))):.2e}")
