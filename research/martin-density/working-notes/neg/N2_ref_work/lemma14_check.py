# Check N2 Lemma 1.4 (primal splitting bound) and the refined version 1.4' on random finite block data.
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(1)
def blocknorm(x, Ph):
    # |x| for the norm with unit ball B_l1 + D B_l2 (Part II Lemma T): |x| = A(theta), theta root of A^2 - B
    v = np.abs(x)/Ph**2
    A = lambda s: np.maximum(np.abs(x)-s*Ph**2, 0).sum()
    B = lambda s: (Ph**2*np.minimum(s, v)**2).sum()
    th = brentq(lambda s: A(s)**2 - B(s), 1e-300, v.max()*(1-1e-15)+1e-300)
    a = A(th); M = th/(th+a); C = a/(th+a)
    w = np.sign(x)*M*np.minimum(1, v/th)
    return a, w, M, C, th
worst14 = -1e9; worst14r = -1e9; cnt = 0
for trial in range(4000):
    K = rng.integers(5, 30)
    Ph = 0.4*2.0**(-np.arange(1, K+1)*rng.uniform(0.5, 1.5))
    zeta = rng.normal(size=K)*Ph*rng.uniform(0, 3, size=K)
    sig, w, M, C, th = blocknorm(zeta, Ph)
    P = np.abs(np.abs(w)-M) < 1e-12
    alpha = zeta/sig - Ph**2*w/C            # supported on P
    eta = rng.normal(size=K)*Ph*rng.uniform(0, 2, size=K)
    t = 10**rng.uniform(-4, -0.5)
    # absorbable set: peaks with alpha != 0 where same sign or room
    room = sig*np.abs(alpha)
    A_ = P & (np.abs(alpha) > 1e-14) & ((np.sign(eta) == np.sign(alpha)) | (t*np.abs(eta) <= room))
    if not A_.any(): continue
    # balancing: eta_1 = eta*1_A + r, r = kappa*sgn(alpha)*Phi^2 on A (small), solve w'(eta_1) = M w'(eta)
    s_A = (np.sign(alpha[A_])*eta[A_]).sum()
    target = (w*eta).sum()          # need sum sgn(alpha) eta_1 = w(eta)
    base = np.sign(alpha)*Ph**2*A_
    kappa = (target - s_A)/ (np.abs(base)).sum()
    r = kappa*base
    eta1 = eta*A_ + r
    # check room condition (i) for eta1
    opp = (np.sign(eta1) == -np.sign(alpha)) & A_
    if np.any(t*np.abs(eta1[opp]) > room[opp] + 1e-15): continue
    eta2 = eta - eta1
    lhs = blocknorm(zeta + t*eta, Ph)[0] - (w*(zeta + t*eta)).sum()
    Dinv = eta2/Ph
    bound = t**2*(Dinv**2).sum()/(2*sig)
    e = Ph*w/C                      # unit vector D w / C
    perp = Dinv - (e@Dinv)*e
    den = sig + t*(w*eta).sum()
    boundr = t**2*(perp**2).sum()/(2*den) if den > 0 else np.inf
    worst14 = max(worst14, (lhs - bound)/max(abs(bound), 1e-30))
    worst14r = max(worst14r, (lhs - boundr)/max(abs(boundr), 1e-30))
    cnt += 1
print('valid splits tested:', cnt)
print('max relative violation of Lemma 1.4 bound (should be <= ~0):', worst14)
print("max relative violation of refined bound 1.4' (should be <= ~0):", worst14r)
