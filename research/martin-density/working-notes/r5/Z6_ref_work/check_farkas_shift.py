"""Referee sanity checks for Z6:
(1) Proposition P (Farkas pinning): for random small cones C = {nu >= 0, z_j L_j(nu) >= 0 (contacts), L_j(nu) = 0 (rooms),
    nu_l = 0 (anti peaks), Q_m(nu) = 0}, if nu_{l0} = 0 on C, find a certificate minimizing ||(y,y',kappa)||_inf by LP and test
    (1 + y_{l0}) tau_{l0} <= ||cert||_inf * [sum_{l != l0} (tau_l)_- + sum (z L)_- + sum |L_room| + sum_anti |tau| + sum_m |Q_m|]
    on random tau.
(2) Shift trick (Theorem C step 5): one block, coordinate k a near-threshold strict non-peak with sgn w(k) = +1, gap tiny;
    data omega^pm with P <= a, Q >= -a - e, Q - P in [0, A2/t]; after the shift, check ||W||_inf = (1 - r d) M and the excess
    bound N(W) - 1 <= (r^2/2) H(omega) (1 + 2|r d| M / C) for 0 < r <= c t (+ side) and -c t <= r < 0 (- side).
"""
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(7)


def farkas_test(trials=300):
    found = 0; worst = -np.inf
    for _ in range(trials):
        nL = rng.integers(3, 7); nJ = rng.integers(2, 6)
        Lmat = rng.normal(size=(nJ, nL)) * (rng.random((nJ, nL)) < 0.6)
        z = rng.choice([-1.0, 1.0], size=nJ); room = rng.random(nJ) < 0.3
        anti = rng.random(nL) < 0.2
        q = rng.normal(size=nL); blocks = rng.integers(0, 2, size=nL)
        # inequality rows G nu >= 0 ; equality rows E nu = 0
        G = [np.eye(nL)[l] for l in range(nL)] + [z[j] * Lmat[j] for j in range(nJ) if not room[j]]
        E = [Lmat[j] for j in range(nJ) if room[j]] + [np.eye(nL)[l] for l in range(nL) if anti[l]]
        for mb in (0, 1):
            E.append(q * (blocks == mb))
        G = np.array(G); E = np.array(E) if len(E) else np.zeros((0, nL))
        for l0 in range(nL):
            # rigid iff max nu_{l0} s.t. G nu >= 0, E nu = 0, nu_{l0} <= 1 is 0
            res = linprog(-np.eye(nL)[l0], A_ub=-G, b_ub=np.zeros(len(G)), A_eq=E if len(E) else None,
                          b_eq=np.zeros(len(E)) if len(E) else None, bounds=[(None, 1)] * nL, method='highs')
            if res.status != 0 or -res.fun > 1e-9:
                continue  # not rigid
            # certificate: -e_{l0} = G^T y + E^T y2, y >= 0, minimize s = max(|y|,|y2|)
            nG, nE = len(G), len(E)
            # variables y (nG), y2p, y2m (nE), s
            c = np.zeros(nG + 2 * nE + 1); c[-1] = 1
            Aeq = np.hstack([G.T, E.T, -E.T, np.zeros((nL, 1))]); beq = -np.eye(nL)[l0]
            Aub = np.zeros((nG + 2 * nE, nG + 2 * nE + 1))
            for i in range(nG + 2 * nE):
                Aub[i, i] = 1; Aub[i, -1] = -1
            r2 = linprog(c, A_ub=Aub, b_ub=np.zeros(nG + 2 * nE), A_eq=Aeq, b_eq=beq,
                         bounds=[(0, None)] * (nG + 2 * nE + 1), method='highs')
            if r2.status != 0:
                print('certificate LP failed although rigid'); continue
            y = r2.x[:nG]; y2 = r2.x[nG:nG + nE] - r2.x[nG + nE:nG + 2 * nE]
            S = max(np.abs(y).max(), np.abs(y2).max() if nE else 0)
            found += 1
            for _ in range(200):
                tau = rng.normal(size=nL) * rng.choice([0.01, 1, 10], size=nL)
                Lt = Lmat @ tau
                br = sum(max(-tau[l], 0) for l in range(nL) if l != l0)
                br += sum(max(-z[j] * Lt[j], 0) for j in range(nJ) if not room[j])
                br += sum(abs(Lt[j]) for j in range(nJ) if room[j])
                br += sum(abs(tau[l]) for l in range(nL) if anti[l])
                br += sum(abs(q[blocks == mb] @ tau[blocks == mb]) for mb in (0, 1))
                lhs = (1 + y[l0]) * tau[l0]
                worst = max(worst, lhs - S * br)
    print('rigid instances tested:', found, ' max (lhs - rhs) =', worst)


def shift_test(trials=2000):
    worst_sup = -np.inf; worst_exc = -np.inf
    for _ in range(trials):
        K = 8
        Phi = np.sort(rng.random(K))[::-1] * 0.05
        w = rng.uniform(-0.5, 0.5, K)
        M = 0.9
        w[0] = M; w[1] = -M  # peaks
        k = 2
        gap = 10 ** rng.uniform(-8, -1)
        w[k] = M - gap  # near-threshold, sgn +1
        C = 1 - M
        # rescale D so that ||D w|| = C
        Phi = Phi * C / np.linalg.norm(Phi * w)
        t = 10 ** rng.uniform(-4, -1); A2 = 10.0; a = 1.5 * gap / t
        e = rng.uniform(0, 5) / t
        P = rng.uniform(-3, 1) * a if a > 0 else 0
        P = min(P, a)
        Q = P + rng.uniform(0, A2 / t)
        Q = max(Q, -a - e)
        if Q - P < 0:
            continue
        x = max(-a - Q, 0.0)  # vs x with vs = +1
        Pt, Qt = P + x, Q + x
        # other non-peak coordinates: clamped data |omega| <= 2 gap_k / t when gap_k >= t^2
        om_p = np.zeros(K); om_m = np.zeros(K)
        for j in range(3, K):
            gj = M - abs(w[j])
            if gj >= t * t:
                v = rng.uniform(-2, 2) * gj / t
                om_p[j] = v; om_m[j] = v + rng.uniform(-1, 1) * 0  # equal on good coordinates (d-neutral data)
        om_p[k] = Pt; om_m[k] = Qt
        cflat = min(0.25, C / (2 * (A2 + 6)), 1 / (4 * (1.5 + A2 + 6)))
        for side, om in ((+1, om_p), (-1, om_m)):
            d = (Phi * w) @ (Phi * om) / C
            for frac in (0.1, 0.5, 1.0):
                r = side * frac * cflat * t
                W = (1 - d * r) * w + r * om
                sup = np.abs(W).max()
                worst_sup = max(worst_sup, sup - (1 - d * r) * M)
                N = sup + np.linalg.norm(Phi * W)
                h2 = np.linalg.norm(Phi * om) ** 2 - d * d
                H = h2 / C
                exc = N - 1 - 0.5 * r * r * H * (1 + 2 * abs(d * r) * M / C)
                worst_exc = max(worst_exc, exc)
    print('shift trick: max(||W||_inf - (1-rd)M) =', worst_sup, '  max(excess - bound) =', worst_exc)


if __name__ == '__main__':
    farkas_test()
    shift_test()
