"""Toy check of U1 Lemmas 4.1-4.2 (robust recursion in configuration (i); owner dominance).

Finite ladder of carriers k = 0..K-1 (stage order), each in a block m(k); active blocks A carry a negative shift Delta_m < 0.
Carrier k has vector u_k = target part (random sparse, coefficients >= eta) + signature part on its own set S_k
(geometric weights delta_k 2^{-j}), weights lambda_k super-decreasing (lambda_{k+1} <= lambda_k * eps).
Allowedness: a later target may meet S_k only with weight <= 2^{-2j} * c_k * (tiny factor)  (W4'').
Coefficient of k in V: -Delta_m lambda_k w(k), w(k) = varsigma_k M (peak).  Recursion: owner = first active carrier meeting j;
varsigma_k := sgn(Y_k) where Y_k is the value of u_k on non-owned coordinates; z_j := varsigma_k sgn u_k(j) on owned coordinates.
Checks: (1) |u_k(zhat)| >= own mass (robust peak, self-aligned); (2) for several shift vectors with the SAME signs and arbitrary
ratios within [rmin, 1], V(j) z_j > 0 at every coordinate with V(j) != 0 (admissibility), i.e. the owner dominates."""
import numpy as np
rng = np.random.default_rng(11)

def run(K=40, nb=3, ncoord_target=60, rmin=1e-3):
    blocks = rng.integers(0, nb, size=K)
    active = set(range(nb))
    lam = np.empty(K); lam[0] = 1e-2
    for k in range(1, K):
        lam[k] = lam[k - 1] * 10.0 ** (-rng.uniform(6, 8))     # super-decreasing (ratio <= 1e-6)
    # coordinates: target coordinates 0..ncoord_target-1, signature coordinates allocated per carrier
    vecs = []
    sig_start = ncoord_target
    sigsets = []
    for k in range(K):
        sig = list(range(sig_start, sig_start + 6)); sig_start += 6
        sigsets.append(sig)
    ncoord = sig_start
    for k in range(K):
        u = np.zeros(ncoord)
        supp = rng.choice(ncoord_target, size=rng.integers(1, 4), replace=False)
        u[supp] = rng.choice([-1, 1], size=len(supp)) * rng.uniform(0.3, 1.0, size=len(supp))
        # some targets also meet EARLIER carriers' signature coordinates, with tiny coefficients (allowedness)
        for kk in range(k):
            if rng.random() < 0.05:
                j_idx = rng.integers(0, 6)
                j = sigsets[kk][j_idx]
                # (W4''): own weight lam[k] * |u_k(j)| must be << lam[kk] * v_kk(j) * T, T tiny; here coefficient chosen
                u[j] = rng.choice([-1, 1]) * 1e-3
        delta = 2.0 ** (-(k + 1)) * 0.2
        for idx, j in enumerate(sigsets[k]):
            u[j] = delta * 2.0 ** (-(idx + 1))
        vecs.append(u)
    U = np.array(vecs)
    # recursion
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
    # admissibility for several shift vectors with negative signs and ratios in [rmin, 1]
    adm_ok = True; worst = np.inf
    for trial in range(50):
        Delta = -rng.uniform(rmin, 1.0, size=nb)
        coef = -Delta[blocks] * lam * vs          # w(k) = vs_k M with M = 1
        V = coef @ U
        mask = np.abs(V) > 0
        prod = V[mask] * z[mask]
        if prod.size and prod.min() <= 0:
            adm_ok = False
        if prod.size:
            worst = min(worst, (prod / np.abs(V[mask])).min())
    return robust_ok, adm_ok, worst

res = [run() for _ in range(200)]
print('instances', len(res))
print('all fine carriers robust self-aligned peaks:', all(r[0] for r in res))
print('V z-signed at every coordinate for all shift vectors of the class:', all(r[1] for r in res))
print('min over instances of min_j sgn(V_j z_j) (1 = all correct):', min(r[2] for r in res))
