# Check the balanced relevant-carrier bound (referee Lemma 1.4''):
# excess <= t^2 (||D^{-1} eta 1_R|| + |kappa|/M ||D w 1_{N \ A0}||)^2 / (2 (sigma + t w(eta))),
# kappa = (sum_R w eta - C s_A)/F_{A0}, A = absorbable peaks (same sign or half room), A0 subset A with room for kappa.
import numpy as np
from scipy.optimize import brentq
def blocknorm(x, Ph):
    v = np.abs(x)/Ph**2
    A = lambda s: np.maximum(np.abs(x)-s*Ph**2, 0).sum()
    B = lambda s: (Ph**2*np.minimum(s, v)**2).sum()
    th = brentq(lambda s: A(s)**2 - B(s), 1e-300, v.max()*(1-1e-15)+1e-300)
    a = A(th); M = th/(th+a); C = a/(th+a)
    return a, np.sign(x)*M*np.minimum(1, v/th), M, C, th
rng = np.random.default_rng(7); worst = -1; n = 0; tight = 0
for trial in range(6000):
    K = rng.integers(4, 25)
    Ph = 0.4*2.0**(-np.arange(1, K+1)*rng.uniform(0.5, 1.5))
    zeta = rng.normal(size=K)*Ph*rng.uniform(0, 3, size=K)
    sig, w, M, C, th = blocknorm(zeta, Ph)
    P = np.abs(np.abs(w)-M) < 1e-12
    alpha = zeta/sig - Ph**2*w/C
    s = np.sign(w)
    eta = rng.normal(size=K)*Ph*rng.uniform(0, 2, size=K)
    t = 10**rng.uniform(-4, -0.5)
    room = sig*np.abs(alpha)
    A_ = P & (np.abs(alpha) > 1e-14) & ((np.sign(eta) == s) | (t*np.abs(eta) <= room/2))
    R = ~A_
    sA = (s*eta)[A_].sum()
    kap0 = ((w*eta)[R].sum() - C*sA)
    # A0: absorbable peaks with room for the balancing vector; try A0 = A first, else shrink to the most robust ones
    order = np.argsort(-(room/np.maximum(Ph**2, 1e-300))*A_)
    A0 = np.zeros(K, bool); ok = False
    for j in order:
        if not A_[j]: break
        A0[j] = True
        F = (Ph[A0]**2).sum(); kap = kap0/F
        if np.all(t*abs(kap)*Ph[A0]**2 <= room[A0]/2): ok = True; Abest = A0.copy(); kbest = kap
    if not ok: continue
    A0 = Abest; kap = kbest
    den = sig + t*(w*eta).sum()
    if den <= 0: continue
    lhs = blocknorm(zeta + t*eta, Ph)[0] - (w*(zeta + t*eta)).sum()
    term = np.linalg.norm((eta/Ph)[R]) + abs(kap)/M*np.linalg.norm((Ph*w)[~A0])
    bound = t**2*term**2/(2*den)
    worst = max(worst, lhs - bound); n += 1
    if lhs > 0.5*bound: tight += 1
print('cases:', n, ' max(lhs - bound) =', worst, '  cases with lhs > bound/2:', tight)
