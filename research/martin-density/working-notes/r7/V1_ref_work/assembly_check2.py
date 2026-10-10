"""End-to-end finite-model check of the V1 companion moves (C3) bank donor + (C4) exact tuning in ONE block, diagonal base.
Block carriers u_k (k=0..K-1), lambda_k = Phi_k; each carrier has a private signature set (bounded gaps) beyond a cutoff,
exactly swallowed there (z = eps_k) for tuned carriers; random 'target' parts below the cutoff and on F.
Steps: pick donor c = argmax rho (rho_c > 1); make carrier k4 near-threshold (rho in [1-b,1+b]) by adjusting its target entry;
pick a 2-carrier 'ray' r on {k4, k1} and make its component sum r val tiny (<= b) by adjusting k1's target entry;
(C3) case (b): close z at s_c to vs, bank mass 2 nu Lam/(lambda_c s^2 v) there; (C4) at f^(2): x = -R^+ V on L0 = {k4, k1}
via pulls + banks (explicit scalar fixed point).  Check: component exactly 0 at f^#, theta^# - theta >= c Lam, rho^#_{k4} < 1."""
import numpy as np
rng = np.random.default_rng(5)

def theta_of(zeta, Phi):
    a = np.abs(zeta); nu = a / Phi**2
    def psi(x):
        return np.sum(np.maximum(a - x * Phi**2, 0.0))**2 - np.sum(Phi**2 * np.minimum(x, nu)**2)
    lo, hi = 0.0, max(nu.max(), 1.0)
    while psi(hi) > 0: hi *= 2
    for _ in range(300):
        mid = 0.5*(lo+hi)
        if psi(mid) > 0: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)

def zhat(A, z, s):
    nu = np.linalg.norm(s*A); return z + s**2*A/nu

import collections; rej = collections.Counter(); ok = 0; tot = 0; worstcomp = 0.0; minraise = np.inf; maxrho4 = -np.inf
for trial in range(300):
    K = int(rng.integers(5, 9)); alpha = 0.08; G = 2; cutoff = 15
    n = cutoff + K*G*120 + 10
    s = 2.0**(-alpha*np.arange(1, n+1))
    F = [0, 1, 2]; A = np.zeros(n); A[F] = rng.normal(size=3)
    z = rng.uniform(-1, 1, n); z[F] = np.sign(A[F])
    Phi = 2.0**(-np.arange(1, K+1)*0.7) * rng.uniform(0.5, 1.0, K); lam = Phi.copy()
    S = [cutoff + k + K*G*np.arange(0, 120) for k in range(K)]
    eps = rng.choice([-1, 1], size=K)
    U = np.zeros((K, n))
    for k in range(K):
        U[k, F] = rng.normal(size=3)*0.2
        tg = rng.choice(np.arange(3, cutoff), size=3, replace=False); U[k, tg] = rng.normal(size=3)*0.2
        U[k, S[k]] = rng.uniform(0.2, 0.5) * 2.0**(-alpha*S[k])
        z[S[k]] = eps[k]
    def vals(A, z):
        return U @ zhat(A, z, s)
    v = vals(A, z); zeta = lam*v; th = theta_of(zeta, Phi); rho = np.abs(zeta)/(Phi**2*th)
    c = int(np.argmax(rho))
    if rho[c] < 1.2:
        rej['donor']+=1; continue
    others = [k for k in range(K) if k != c]
    k4, k1 = others[0], others[1]
    # make k4 near-threshold: adjust its value via a private target coordinate (coordinate 3+k4 reserved)
    b = 1e-10; Lam = 1e-6
    j4 = 3 + (k4 % (cutoff-3)); j1 = 3 + ((k4+1+ (k1 % 5)) % (cutoff-3))
    if j4 == j1: continue
    # private target coordinates: zero other carriers there
    U[:, j4] = 0.0; U[:, j1] = 0.0; U[k4, j4] = 0.3; U[k1, j1] = 0.3
    b = 1e-9; Lam = 1e-5
    if abs(U[k4,F] @ np.zeros(3)) > 1: pass
    tgt1_noise = 0.5*b*rng.uniform(-1,1)
    for it in range(200):
        v = vals(A, z); zeta = lam*v; th = theta_of(zeta, Phi)
        sg = np.sign(v[k4]) if v[k4] != 0 else 1.0
        target4 = sg*th*Phi[k4]**2*(1+0.3*b)/lam[k4]
        z[j4] = np.clip(z[j4] + (target4 - v[k4])/0.3, -1, 1)
        v = vals(A, z)
        tgt1 = -eps[k4]*v[k4]*eps[k1] + tgt1_noise
        z[j1] = np.clip(z[j1] + (tgt1 - v[k1])/0.3, -1, 1)
    v = vals(A, z); zeta = lam*v; th = theta_of(zeta, Phi); rho = np.abs(zeta)/(Phi**2*th)
    D0 = 0.5*(eps[k4]*v[k4] + eps[k1]*v[k1])
    if abs(D0) > b or abs(rho[k4]-1) > b or rho[c] < 1.2:
        rej['D0/k4/c']+=1; continue
    nu0 = np.linalg.norm(s*A)
    # (C3) case (b) at s_c = first far signature coordinate of c
    sc = S[c][0]; vs = np.sign(v[c])
    z2 = z.copy(); z2[sc] = vs; A2 = A.copy()
    muD = 2*nu0*Lam/(lam[c]*s[sc]**2*U[c, sc]); A2[sc] += vs*muD
    v2 = vals(A2, z2)
    # (C4) tuning x = -R^+ V on L0 = [k4, k1]
    R = np.array([[0.5*1.0, 0.5*1.0]])  # rows act on eps*val
    val2 = np.array([eps[k4]*v2[k4], eps[k1]*v2[k1]])
    V2 = R @ val2
    x = -np.linalg.pinv(R) @ V2
    eta = np.max(np.abs(x))
    L0 = [k4, k1]
    Ap = A2.copy(); zp = z2.copy(); jb = []
    for i, k in enumerate(L0):
        jb.append(S[k][0]); vS = U[k, S[k]]
        cand = [j for j, vv in zip(S[k][1:], vS[1:]) if eta <= vv <= 2**(alpha*K*G)*eta*1.0000001]
        j = cand[0] if cand else S[k][1]
        mu = 24*lam[k]*U[k, j]; Ap[j] += -eps[k]*mu; zp[j] = -eps[k]
    nup = np.linalg.norm(s*Ap); vp = vals(Ap, zp)
    valp = np.array([eps[k]*vp[k] for k in L0]); ep = s*Ap/nup
    beta = np.array([eps[k]*np.dot(s*U[k], ep) for k in L0])
    Delta = x + val2 - valp
    sp = s[jb]; vb = np.array([U[k, jb[i]] for i, k in enumerate(L0)])
    mf = lambda y: (Delta*y + beta*(y-nup))/(sp**2*vb)
    Ph = lambda y: np.sqrt(nup**2 + np.sum(sp**2*mf(y)**2))
    y = nup
    for it in range(300): y = Ph(y)
    m = mf(y)
    if np.min(m) <= 0:
        rej['mass']+=1; continue
    Ah = Ap.copy()
    for i, k in enumerate(L0): Ah[jb[i]] += m[i]*eps[k]
    vh = vals(Ah, zp); zh_ = lam*vh; thh = theta_of(zh_, Phi); rhoh = np.abs(zh_)/(Phi**2*thh)
    Dh = 0.5*(eps[k4]*vh[k4] + eps[k1]*vh[k1])
    tot += 1
    worstcomp = max(worstcomp, abs(Dh))
    minraise = min(minraise, (thh - th)/(th*Lam))
    maxrho4 = max(maxrho4, (rhoh[k4] - 1)/Lam)
    if abs(Dh) < 1e-14 and thh > th and rhoh[k4] < 1: ok += 1
print(dict((k,v) for k,v in rej.items() if v)); print("assembled companions:", tot, "all checks passed:", ok)
print("max |component at f^#| =", worstcomp, " min (theta^#-theta)/(theta Lam) =", minraise, " max (rho^#_k4 - 1)/Lam =", maxrho4)
