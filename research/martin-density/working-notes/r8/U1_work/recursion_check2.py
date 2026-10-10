"""Toy check of U1 Lemmas 4.1-4.2, version 2: the later weights obey the (W4'') rule.

recursion_check.py (version 1) let later targets meet an earlier carrier kk's signature coordinate with a coefficient
1e-3 INDEPENDENT of delta_kk and of the signature index; this violates (W4'') (later weights must be
<= tau * 2^{-2s} * c_kk * delta_kk * T^3) and version 1 indeed found sign failures at such coordinates.
Here the weight lam[k] of a later carrier is chosen AFTER its contacts are known, as in the design:
    lam[k] <= lam[k-1] * 1e-6  and  lam[k] * |u_k(j)| <= tau * 2^{-2(idx+1)} * lam[kk] * delta_kk   for each contact j = S_kk[idx].
Checks as in version 1 plus: (3) a deliberately (W4'')-violating variant must fail (sanity of the test)."""
import numpy as np
rng = np.random.default_rng(11)


def build(K, nb, ncoord_target, w4, tau=1e-6):
    blocks = rng.integers(0, nb, size=K)
    sigsets = []
    sig_start = ncoord_target
    for k in range(K):
        sigsets.append(list(range(sig_start, sig_start + 6)))
        sig_start += 6
    ncoord = sig_start
    U = np.zeros((K, ncoord))
    lam = np.empty(K)
    delta = np.array([2.0 ** (-(k + 1)) * 0.2 for k in range(K)])
    for k in range(K):
        u = U[k]
        supp = rng.choice(ncoord_target, size=rng.integers(1, 4), replace=False)
        u[supp] = rng.choice([-1, 1], size=len(supp)) * rng.uniform(0.3, 1.0, size=len(supp))
        contacts = []
        for kk in range(k):
            if rng.random() < 0.05:
                idx = rng.integers(0, 6)
                j = sigsets[kk][idx]
                u[j] = rng.choice([-1, 1]) * 1e-3
                contacts.append((kk, idx, j))
        for idx, j in enumerate(sigsets[k]):
            u[j] = delta[k] * 2.0 ** (-(idx + 1))
        if k == 0:
            lam[k] = 1e-2
        else:
            lam[k] = lam[k - 1] * 10.0 ** (-rng.uniform(6, 8))
            if w4:
                for (kk, idx, j) in contacts:
                    cap = tau * 2.0 ** (-2 * (idx + 1)) * lam[kk] * delta[kk] / abs(u[j])
                    lam[k] = min(lam[k], cap)
    return blocks, lam, U, ncoord


def run(K=40, nb=3, ncoord_target=60, rmin=1e-3, w4=True):
    blocks, lam, U, ncoord = build(K, nb, ncoord_target, w4)
    owner = -np.ones(ncoord, dtype=int)
    for j in range(ncoord):
        meets = np.nonzero(U[:, j])[0]
        if len(meets):
            owner[j] = meets.min()
    z = np.zeros(ncoord)
    vs = np.zeros(K)
    robust_ok = True
    for k in range(K):
        own = np.nonzero(owner == k)[0]
        nonown = np.nonzero((U[k] != 0) & (owner != k))[0]
        Y = np.dot(U[k, nonown], z[nonown])
        vs[k] = np.sign(Y) if Y != 0 else 1.0
        z[own] = vs[k] * np.sign(U[k, own])
        val = np.dot(U[k], z)
        ownmass = np.abs(U[k, own]).sum()
        if not (np.sign(val) == vs[k] and abs(val) >= ownmass - 1e-15):
            robust_ok = False
    adm_ok = True
    worst = np.inf
    for trial in range(50):
        Delta = -rng.uniform(rmin, 1.0, size=nb)
        coef = -Delta[blocks] * lam * vs
        V = coef @ U
        mask = np.abs(V) > 0
        prod = V[mask] * z[mask]
        if prod.size and prod.min() <= 0:
            adm_ok = False
        if prod.size:
            worst = min(worst, (prod / np.abs(V[mask])).min())
    return robust_ok, adm_ok, worst


for w4 in (True, False):
    res = [run(w4=w4) for _ in range(200)]
    print("(W4'') enforced:" if w4 else "(W4'') violated (version-1 toy):")
    print('  instances', len(res))
    print('  all carriers robust self-aligned peaks:', all(r[0] for r in res))
    print('  V z-signed at every coordinate, all 50 shift vectors per instance:', all(r[1] for r in res))
    print('  fraction of instances with full admissibility:', np.mean([r[1] for r in res]))
    print('  min over instances of min_j sgn(V_j z_j):', min(r[2] for r in res))
