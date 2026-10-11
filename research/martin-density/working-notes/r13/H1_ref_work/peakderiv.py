"""Signed derivative of kappa_m (U1 Lemma 1.3 form) w.r.t. the block-vector entries of PEAKS: is it sgn(zeta_c)(1 - X_m) with the SAME
1 - X_m for every peak (Lemma NP(b) / R-PK)?  Random blocks with 2-3 peaks, mixed signs, Omega = all strict non-peaks."""
import sys, numpy as np
sys.path.insert(0, '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r12/J1_ref_work/rerun')
from model import block
def kappa_fn(zeta, Phi, Om):
    b = block(zeta, Phi); Q = ~b['P']; out = Q & ~Om
    S = (b['nu'][out]**2*Phi[out]**2).sum()
    return b['A'] + b['theta']*(Phi[b['P']]**2).sum() + S/b['theta'], b
rng = np.random.default_rng(3)
worst = 0; cnt = 0; Xs = []
for trial in range(400):
    n = rng.integers(5, 12); Phi = rng.uniform(0.02, 0.3, n)
    zeta = rng.normal(size=n)*Phi**2*rng.uniform(0.2, 3, n)
    b = block(zeta, Phi); P = b['P']
    if P.sum() < 2: continue
    Om = ~P
    k0, _ = kappa_fn(zeta, Phi, Om)
    g = np.zeros(n); h = 1e-8*np.abs(zeta).max()
    for k in range(n):
        zp = zeta.copy(); zm = zeta.copy(); zp[k] += h; zm[k] -= h
        g[k] = (kappa_fn(zp, Phi, Om)[0] - kappa_fn(zm, Phi, Om)[0])/(2*h)
    gp = g[P]*np.sign(zeta[P])        # = d kappa / d|zeta_c| for peaks
    worst = max(worst, gp.max() - gp.min()); cnt += 1; Xs.append(1 - gp.mean())
    # Euler check
    eul = (g*zeta).sum() - k0
    if abs(eul) > 1e-6*abs(k0): print('Euler fail', eul)
print(f"blocks with >=2 peaks: {cnt}; max spread of d kappa/d|zeta_c| over peaks of a block: {worst:.2e}; 1 - (common value) in [{min(Xs):.3f}, {max(Xs):.3f}]")
