"""X2-referee check 2: a zero-value absorber cannot follow a lever / window move at its own coordinate s.
Model: one block (m = 1); carriers: c (robust peak), l (coarse strict non-peak, signature on S_l = {3,4,5} containing s = 4), a (absorber:
tiny Phi_a, target beta e_s^* + e_{p0}^* - c1 e_{p1}^*, c1 chosen so that the absorber is TUNABLE to value 0 by its S-mass m_0 at p0, as in
U1 Lemma 3.3; mu_{p0} small because p0 is a fresh, late coordinate).  A lever of l acts at s (inward z-move of size P/v_l(s), which lowers
u_l by P).  Printed: the absorber's value room theta*Phi_a/m (strict non-peak iff m|u_a| < theta Phi_a), its value after the move, its
status, and the S-mass at p0 needed to restore u_a = 0 (compared with m_0; masses must stay >= 0)."""
import numpy as np, sys
sys.path.insert(0, '.')
from rmodel import Row
from scipy.optimize import brentq
n = 12; s, p0, p1 = 4, 9, 10
mu = np.array([0.6, 0.5, 0.45] + [0.4*0.6**j for j in range(n - 3)]); mu[p0] = 1e-3; mu[p1] = 5e-4
for beta in (+1, -1):
    U = np.zeros((3, n))
    U[0, 0] = 1.0; U[0, 1] = 0.6; U[0, 6] = 0.1
    U[1, 0] = 0.3; U[1, 1] = -0.5; U[1, [3, 4, 5]] = [0.08, 0.04, 0.02]
    c1 = beta + 1 + 3e-8                      # bracket beta*z_s + z_p0 - c1*z_p1-term ~ -3e-8 (tunable by the p0 mass)
    U[2, s] = beta; U[2, p0] = 1.0; U[2, p1] = c1
    Phi = np.array([0.2, 0.05, 1e-7]); blk = np.array([1, 1, 1])
    R = Row(mu, U, blk, Phi, [0, 1])
    q = [R.qstar(u) for u in U]; R.U = np.array([u/qq for u, qq in zip(U, q)])
    z = np.zeros(n); z[0] = z[1] = 1; z[[3, 4, 5]] = 1; z[6] = 1; z[p0] = 1; z[p1] = -1; z[[7, 8, 11]] = 0.2
    A = np.zeros(n); A[0], A[1] = 0.8, 0.5; A[p1] = -1e-9
    def val_a(m0, zz, AA):
        A2 = AA.copy(); A2[p0] = m0
        return R.forced(A2, zz)['val'][2]
    lo, hi = 1e-9, 1e-1
    if np.sign(val_a(lo, z, A)) == np.sign(val_a(hi, z, A)):
        print('beta=%+d: not tunable in [1e-9, 1e-1]: %.2e %.2e' % (beta, val_a(lo, z, A), val_a(hi, z, A))); continue
    m0 = brentq(lambda m: val_a(m, z, A), lo, hi, xtol=1e-22)
    A0 = A.copy(); A0[p0] = m0
    D0 = R.forced(A0, z); B = D0['blocks'][1]
    room = B['theta']*Phi[2]
    vl_s = R.U[1, s]
    for P in (1e-3, 1e-6):
        z2 = z.copy(); z2[s] = 1 - P/vl_s
        D1 = R.forced(A0, z2); B1 = D1['blocks'][1]; ua1 = D1['val'][2]
        g = lambda m: val_a(m, z2, A0)
        grid = np.concatenate([np.linspace(0, m0, 40)[:-1], m0*np.logspace(0, 14, 300)])
        vals = np.array([g(m) for m in grid])
        sc = np.where(np.sign(vals[:-1]) != np.sign(vals[1:]))[0]
        need = brentq(g, grid[sc[0]], grid[sc[0] + 1], xtol=1e-25) if len(sc) else np.nan
        msg = 'none in [0, 1e14*m0] (masses must stay >= 0)' if np.isnan(need) else '%.3e (= %.1e x m0)' % (need, need/m0)
        print('beta=%+d  P=%.0e: m0=%.3e  room theta*Phi_a=%.2e  |u_a| after the lever move=%.2e (ratio %.1e) -> %s ; S-mass restoring u_a=0: %s'
              % (beta, P, m0, room, abs(ua1), abs(ua1)/room, 'PEAK' if B1['P'][2] else 'strict non-peak', msg))
