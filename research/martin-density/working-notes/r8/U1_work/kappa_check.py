"""Sanity check of the kappa-reduction (U1 Lemma 1.3/1.4).

One block, finitely many carriers.  zeta in R^n (zeta(k) = lambda_k u_k(zhat)), weights Phi_k.
Norm |.|_Phi with unit ball B_l1 + D_Phi(B_l2); dual N(w) = ||w||_inf + ||Phi w||_2.
A := |zeta|_Phi, w := norming functional, M := ||w||_inf, C := ||Phi w||_2, theta := A M / C,
nu_k := |zeta(k)|/Phi_k^2, peaks P = {nu >= theta}, Q = complement.
Claims:
 (E1) sum_P Phi^2 (nu - theta) = A,   (E2) A^2 = theta^2 Phi_P^2 + sum_Q nu^2 Phi^2
 (K)  data identity coefficient:  kappa_Omega := [A(A+theta) - sum_Omega nu^2 Phi^2]/theta
                                   = A + theta Phi_P^2 + (1/theta) sum_{Q\Omega} nu^2 Phi^2
 (D1) peak push |zeta(c)| += s:  d kappa/ds = 1 - X,  X := C sum_{Q\Omega} nu^2 Phi^2/(theta^2 Phi_P^2)
 (D2) push of a dropped strict non-peak d in Q\Omega: d kappa/ds = rho_d (2 + M X / C),  rho_d = nu_d/theta
 (I)  data identity: for omega^+-, Delta := d(omega^-) - d(omega^+), c_k := lambda_k[(omega^- - omega^+)(k) - Delta w(k)],
      Delta*M * kappa_Omega = sum_{Omega} u_k c_k   (u_k = zeta(k)/lambda_k), lambda_k = m Phi_k.
"""
import numpy as np

rng = np.random.default_rng(1)

def dual_norm(w, Phi):
    return np.max(np.abs(w)) + np.linalg.norm(Phi * w)

def norming(zeta, Phi, tol=1e-14):
    """Clamp formula: Phi_k w(k) = sgn(zeta_k) min(Phi_k M, C v_k), v_k = |zeta_k|/(Phi_k A).
    Solve for (A, C) by nested bisection: given A, C is the root of F(c) = sum min(Phi(1-c)/c, v)^2 = 1;
    A is then fixed by <w, zeta> = A."""
    def C_of_A(A):
        v = np.abs(zeta) / (Phi * A)
        F = lambda c: np.sum(np.minimum(Phi * (1 - c) / c, v) ** 2) - 1.0
        lo, hi = 1e-15, 1 - 1e-15
        # F decreasing in c
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if F(mid) > 0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    def w_of(A):
        C = C_of_A(A)
        M = 1 - C
        v = np.abs(zeta) / (Phi * A)
        w = np.sign(zeta) * np.minimum(Phi * M, C * v) / Phi
        return w, M, C
    # A solves <w(A), zeta> = A; g(A) = <w(A),zeta> - A is decreasing
    lo, hi = 1e-12, np.sum(np.abs(zeta)) + 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        w, M, C = w_of(mid)
        if np.dot(w, zeta) - mid > 0:
            lo = mid
        else:
            hi = mid
    A = 0.5 * (lo + hi)
    w, M, C = w_of(A)
    return A, w, M, C

def block_data(zeta, Phi, Omega):
    A, w, M, C = norming(zeta, Phi)
    theta = A * M / C
    nu = np.abs(zeta) / Phi ** 2
    P = nu >= theta * (1 - 1e-12)
    Q = ~P
    PhiP2 = np.sum(Phi[P] ** 2)
    QmO = Q & ~Omega
    kappa1 = (A * (A + theta) - np.sum((nu[Omega] * Phi[Omega]) ** 2)) / theta
    kappa2 = A + theta * PhiP2 + np.sum((nu[QmO] * Phi[QmO]) ** 2) / theta
    X = C * np.sum((nu[QmO] * Phi[QmO]) ** 2) / (theta ** 2 * PhiP2)
    E1 = np.sum(Phi[P] ** 2 * (nu[P] - theta)) - A
    E2 = A ** 2 - theta ** 2 * PhiP2 - np.sum((nu[Q] * Phi[Q]) ** 2)
    return dict(A=A, w=w, M=M, C=C, theta=theta, nu=nu, P=P, Q=Q, PhiP2=PhiP2,
                kappa1=kappa1, kappa2=kappa2, X=X, E1=E1, E2=E2,
                dual=dual_norm(w, Phi), pair=np.dot(w, zeta))

if __name__ == "__main__":
  pass
worst = dict(E1=0, E2=0, K=0, D1=0, D2=0, I=0, dual=0)
ntest = 0
for trial in range(400):
    n = rng.integers(6, 14)
    m = rng.integers(1, 4)
    Phi = 2.0 ** (-(m + np.arange(1, n + 1))) * rng.uniform(0.3, 1.0, n)
    lam = m * Phi
    u = rng.normal(size=n) * rng.choice([1.0, 1e-2, 1e-3], size=n)
    zeta = lam * u
    d0 = block_data(zeta, Phi, np.zeros(n, bool))
    Q = d0['Q']; P = d0['P']
    if Q.sum() < 2 or P.sum() < 1:
        continue
    # choose Omega = random subset of Q
    Omega = Q & (rng.random(n) < 0.5)
    d = block_data(zeta, Phi, Omega)
    if not np.array_equal(d['P'], P):
        continue
    ntest += 1
    worst['E1'] = max(worst['E1'], abs(d['E1']) / d['A'])
    worst['E2'] = max(worst['E2'], abs(d['E2']) / d['A'] ** 2)
    worst['K'] = max(worst['K'], abs(d['kappa1'] - d['kappa2']) / abs(d['kappa1']))
    worst['dual'] = max(worst['dual'], abs(d['dual'] - 1))
    # (D1): peak push at the peak with the largest margin
    cands = np.where(P)[0]
    c = cands[np.argmax(d['nu'][cands] - d['theta'])]
    h = 1e-7 * abs(zeta[c])
    z2 = zeta.copy(); z2[c] += np.sign(zeta[c]) * h
    dp = block_data(z2, Phi, Omega)
    if np.array_equal(dp['P'], P):
        fd = (dp['kappa1'] - d['kappa1']) / h
        pred = 1 - d['X']
        worst['D1'] = max(worst['D1'], abs(fd - pred) / max(1, abs(pred)))
    # (D2): push of a dropped strict non-peak
    QmO = np.where(Q & ~Omega)[0]
    if len(QmO) > 0:
        dd = QmO[np.argmax(d['nu'][QmO])]
        if abs(zeta[dd]) > 0:
            h = 1e-7 * abs(zeta[dd])
            z3 = zeta.copy(); z3[dd] += np.sign(zeta[dd]) * h
            dq = block_data(z3, Phi, Omega)
            if np.array_equal(dq['P'], P):
                fd = (dq['kappa1'] - d['kappa1']) / h
                rho = d['nu'][dd] / d['theta']
                pred = rho * (2 + d['M'] * d['X'] / d['C'])
                worst['D2'] = max(worst['D2'], abs(fd - pred) / max(1, abs(pred)))
    # (I): data identity with random omega^+- on Omega
    if Omega.sum() > 0:
        om_p = np.zeros(n); om_m = np.zeros(n)
        om_p[Omega] = rng.normal(size=Omega.sum())
        om_m[Omega] = rng.normal(size=Omega.sum())
        dfun = lambda om: np.dot(Phi ** 2 * d['w'], om) / d['C']
        Delta = dfun(om_m) - dfun(om_p)
        ck = lam * ((om_m - om_p) - Delta * d['w'])
        lhs = Delta * d['M'] * d['kappa1']
        rhs = np.sum(u[Omega] * ck[Omega])
        worst['I'] = max(worst['I'], abs(lhs - rhs) / max(1e-12, abs(rhs) + abs(lhs)))
print('tests', ntest)
for k, v in worst.items():
    print(f'{k:5s} max relative error {v:.3e}')
