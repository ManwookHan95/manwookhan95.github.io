import numpy as np
from scipy.optimize import brentq
exec(open('lemma14_check.py').read().split('worst14 = -1e9')[0])
rng = np.random.default_rng(1)
viol = []; viol0=[]
for trial in range(4000):
    K = rng.integers(5, 30)
    Ph = 0.4*2.0**(-np.arange(1, K+1)*rng.uniform(0.5, 1.5))
    zeta = rng.normal(size=K)*Ph*rng.uniform(0, 3, size=K)
    sig, w, M, C, th = blocknorm(zeta, Ph)
    P = np.abs(np.abs(w)-M) < 1e-12
    alpha = zeta/sig - Ph**2*w/C
    eta = rng.normal(size=K)*Ph*rng.uniform(0, 2, size=K)
    t = 10**rng.uniform(-4, -0.5)
    room = sig*np.abs(alpha)
    A_ = P & (np.abs(alpha) > 1e-14) & ((np.sign(eta) == np.sign(alpha)) | (t*np.abs(eta) <= room))
    if not A_.any(): continue
    s_A = (np.sign(alpha[A_])*eta[A_]).sum(); target = (w*eta).sum()
    base = np.sign(alpha)*Ph**2*A_
    kappa = (target - s_A)/(np.abs(base)).sum(); r = kappa*base
    eta1 = eta*A_ + r
    opp = (np.sign(eta1) == -np.sign(alpha)) & A_
    if np.any(t*np.abs(eta1[opp]) > room[opp] + 1e-15): continue
    eta2 = eta - eta1
    lhs = blocknorm(zeta + t*eta, Ph)[0] - (w*(zeta + t*eta)).sum()
    Dinv = eta2/Ph
    bound = t**2*(Dinv**2).sum()/(2*sig)
    e = Ph*w/C; perp = Dinv - (e@Dinv)*e
    den = sig + t*(w*eta).sum()
    boundr = t**2*(perp**2).sum()/(2*den)
    viol.append((lhs - boundr, lhs, boundr, bound, sig, t))
    viol0.append(lhs-bound)
viol = np.array(viol)
i = np.argmax(viol[:,0]); print('max abs violation refined:', viol[i])
print('max abs violation Lemma1.4:', max(viol0))
print('fraction with lhs-boundr > 1e-12:', np.mean(viol[:,0] > 1e-12))
