"""K2 numerics: Lemma K2.5 and the dichotomy step of Theorem K2.6 in an exact one-block Martin-type model
(threshold equation for the block norm; diagonal base).  Model adapted from r10/Q2_refa_work/smass_jacobian.py.
Checks:
 (a) Psi_y(zhat_0) = 0 for random y (Psi_y := sum_l y_l eps_l u_l - beta R^* w^0, beta := y^T p);
 (b) for every elementary move delta (mass at a support coordinate, bank at a contact, z-move at a free coordinate), the finite-difference
     column c(delta) of F satisfies y^T c(delta) = l_delta(Psi_y)  (l_delta from Lemma K2.4);
 (c) Lemma K2.3 with u = Psi_y at the base row (gamma = <U^* Psi_y, e> made >= 0 by the sign of y).
"""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(2026)

def block(zeta, Phi):
    nu = np.abs(zeta) / Phi**2
    def G(th):
        P = nu >= th
        A = (Phi[P]**2 * (nu[P] - th)).sum()
        return A**2 - th**2 * (Phi[P]**2).sum() - (nu[~P]**2 * Phi[~P]**2).sum()
    hi = nu.max()
    th = brentq(G, 1e-14 * hi, hi * (1 - 1e-15), xtol=1e-17 * hi, rtol=1e-15, maxiter=1000)
    P = nu >= th
    A = (Phi[P]**2 * (nu[P] - th)).sum()
    M = th / (A + th); C = A / (A + th)
    w = np.where(P, np.sign(zeta) * M, C * zeta / (Phi**2 * A))
    return w, A, P

def qstar(A, mu): return np.abs(A).sum() + np.linalg.norm(mu * A)

def make_model(K, nsig):
    n = 2 + K * nsig
    S = [list(range(2 + k * nsig, 2 + (k + 1) * nsig)) for k in range(K)]
    U = np.zeros((K, n))
    for k in range(K):
        U[k, 0], U[k, 1] = 1.0, rng.uniform(-1, 1)
        for i, j in enumerate(S[k]): U[k, j] = rng.uniform(0.2, 0.6) * 2.0**(-i - 1) * (1 if i % 3 else -1)
        U[k] /= np.abs(U[k]).sum() * 1.2
    mu = np.concatenate([[0.45, 0.4], 0.35 * rng.uniform(0.5, 1.0, K * nsig)])
    Phi = np.sort(rng.uniform(0.02, 0.25, K))[::-1]
    return n, S, U, mu, Phi

def state(A_un, z, U, mu, Phi):
    a = A_un / qstar(A_un, mu)
    nu = np.linalg.norm(mu * a); e = mu * a / nu
    zhat = z + mu * e
    val = U @ zhat
    w, A, P = block(Phi * val, Phi)      # lambda = Phi (one block, m = 1)
    return dict(a=a, nu=nu, e=e, zhat=zhat, val=val, w=w, A=A, P=P)

errs_a, errs_b, viol_c, ntests = [], [], 0, 0
for trial in range(400):
    K, nsig = 8, 4
    n, S, U, mu, Phi = make_model(K, nsig)
    z = np.zeros(n); A1 = np.zeros(n)
    A1[0], A1[1] = 1.0, 0.5 * rng.uniform(-1, 1); z[0], z[1] = 1.0, np.sign(A1[1])
    for k in range(K):
        for j in S[k]:
            r = rng.random()
            if r < 0.35:   A1[j] = rng.uniform(-0.3, 0.3); z[j] = np.sign(A1[j])      # support
            elif r < 0.7:  z[j] = rng.choice([-1.0, 1.0])                              # contact
            else:          z[j] = rng.uniform(-0.8, 0.8)                               # free
    st0 = state(A1, z, U, mu, Phi)
    Om = [k for k in range(K) if not st0['P'][k]]
    if len(Om) < 2: continue
    eps = np.array([np.sign(st0['val'][k]) if st0['val'][k] != 0 else 1.0 for k in range(K)])
    p = np.array([eps[l] * st0['val'][l] / st0['A'] for l in Om])
    def Fmap(A_un, zz):
        st = state(A_un, zz, U, mu, Phi)
        return np.array([eps[l] * (st['val'][l] - (st['A'] / st0['A']) * st0['val'][l]) for l in Om]), st
    F0, _ = Fmap(A1, z)
    for rep in range(3):
        y = rng.normal(size=len(Om)); y /= np.linalg.norm(y)
        beta = y @ p
        Psi = sum(y[i] * eps[l] * U[l] for i, l in enumerate(Om)) - beta * (Phi * st0['w']) @ U     # R^* w = sum_k lambda_k w(k) u_k
        errs_a.append(abs(Psi @ st0['zhat']))
        gam = (mu * Psi) @ st0['e']
        if gam < 0: y, Psi, gam = -y, -Psi, -gam
        # (b) elementary moves
        a_n = st0['a']; nu = st0['nu']
        for s in range(n):
            h = 1e-7
            if a_n[s] != 0:      # support mass move (unnormalized A1 scaled consistently)
                A2 = A1.copy(); A2[s] += h * np.sign(A1[s]) * qstar(A1, mu)
                dm = h * np.sign(A1[s])
                kap = gam / nu
                pred = (mu[s]**2 / nu) * (Psi[s] - kap * a_n[s]) * dm
                z2 = z
            elif abs(z[s]) == 1.0:   # bank at a contact
                A2 = A1.copy(); A2[s] = z[s] * h * qstar(A1, mu); dm = h
                pred = (mu[s]**2 / nu) * Psi[s] * z[s] * dm; z2 = z
            else:                     # z-move at a free coordinate
                A2 = A1; z2 = z.copy(); z2[s] += h
                pred = Psi[s] * h
            F2, _ = Fmap(A2, z2)
            col = F2 - F0
            act = y @ col
            scale = abs(pred) + 1e-3 * h * (mu[s]**2 / nu + 1)
            errs_b.append(abs(act - pred) / scale); ntests += 1
        # (c) resource bound (Lemma K2.3) with u = Psi at the base row
        Fset = a_n != 0
        for D in range(2, n + 1):
            res = np.abs((Psi - gam / nu * a_n)[:D][Fset[:D]]).sum() + np.abs(Psi[:D][~Fset[:D]]).sum()
            bound = gam - Psi @ st0['zhat'] - np.abs(Psi[D:]).sum()
            if bound - res > 1e-10: viol_c += 1
print("(a) max |Psi_y(zhat_0)| over random y:", max(errs_a))
print("(b) elementary columns: max |y^T c - l(Psi_y)| / scale over", ntests, "moves:", max(errs_b), " (finite differences, step 1e-7)")
print("(c) violations of the resource bound:", viol_c)
