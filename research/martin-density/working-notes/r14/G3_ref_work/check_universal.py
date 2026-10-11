"""Referee check of G3's universal inequalities on random multi-block instances and random feasible decompositions.

Checked (all are claimed to hold for EVERY pair of decompositions of f +- t g with norms <= s(t) and g(xi) = 0):
  L1.4(a),(b),(c) pointwise; Cor 1.3 budget; (CL0); (CL1),(CL2) for random thick sets T; Lemma 1.7 Step 1 (levels);
  block threshold structure (alpha on peaks, ||alpha||_1 = 1); Lemma 1.7(i) d-row bound; Theorem 2.10 for random G, J_c;
  Lemma 1.7(ii) for random pairs and contacts.
Reports the worst normalized slack (LHS - RHS)/(1 + |RHS|) per inequality (must be <= ~1e-6).
"""
import numpy as np, sys, warnings
warnings.filterwarnings('ignore')
from refmodel import MRow, qstar

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
NINST = int(sys.argv[2]) if len(sys.argv) > 2 else 40


def rand_instance():
    n = 16
    mu = 0.3 * 0.7 ** np.arange(n)
    a = np.zeros(n)
    F = rng.choice(n, size=rng.integers(3, 7), replace=False)
    for j in F:
        a[j] = rng.choice([-1, 1]) * (10 ** rng.uniform(-3.5, -0.3))
    z = np.zeros(n)
    z[F] = np.sign(a[F])
    off = [j for j in range(n) if j not in F]
    for j in off:
        z[j] = rng.choice([-1, 1]) if rng.random() < 0.6 else rng.uniform(-0.9, 0.9)
    Us, Phis = [], []
    for m in range(2):
        K = 5
        U = np.zeros((K, n))
        for k in range(K):
            supp = rng.choice(n, size=rng.integers(3, 7), replace=False)
            U[k, supp] = rng.normal(size=len(supp))
            U[k] /= qstar(U[k], mu)
        Us.append(U)
        Phis.append(rng.uniform(0.05, 0.5, size=K))
    return MRow(a, z, Us, Phis, mu)


worst = {}


def rec(name, lhs, rhs):
    v = (lhs - rhs) / (1 + abs(rhs))
    worst[name] = max(worst.get(name, -np.inf), v)


for inst in range(NINST):
    row = rand_instance()
    pchk = row.pstar(row.f)
    rec('p*(f)=1', abs(pchk - 1), 1e-6)
    peaks, Ms, Cs = [], [], []
    for m in range(row.B):
        w = row.ws[m]; M = np.abs(w).max(); C = np.linalg.norm(row.Phis[m] * w)
        P = np.where(np.abs(w) >= M - 1e-6)[0]
        peaks.append(P); Ms.append(M); Cs.append(C)
        alpha = row.zetas[m] / row.sigmas[m] - row.Phis[m] ** 2 * w / C
        offP = np.setdiff1d(np.arange(len(w)), P)
        rec('alpha off peaks = 0', np.abs(alpha[offP]).max() if len(offP) else 0.0, 1e-6)
        rec('||alpha||_1 = 1', abs(np.abs(alpha[P]).sum() - 1), 1e-6)
        rec('alpha sign = sgn w on P', -(np.sign(alpha[P]) * np.sign(w[P]) * (np.abs(alpha[P]) > 1e-9)).min(), 1e-6)
        rec('M + C = 1', abs(M + C - 1), 1e-6)
    for rep in range(4):
        t = float(rng.choice([0.3, 0.1, 0.03]))
        s1 = np.sqrt(1 + t * t) - 1
        c_g = [rng.normal(size=len(row.Phis[m])) for m in range(row.B)]
        def obj(V, c_g=c_g, t=t):
            expr = 0
            for m in range(row.B):
                lam = row.lams[m]
                expr = expr + (c_g[m] * lam) @ ((row.ws[m] - V['Wm'][m]) / t - (V['Wp'][m] - row.ws[m]) / t)
            return expr
        d = row.decomp(t, obj)
        if d['status'] not in ('optimal',):
            continue
        D = row.derived(t, d)
        V, ep, em = D['V'], D['ep'], D['em']
        rec('V = L*(dTheta)', np.abs(V - D['Vrec']).max(), 1e-6)
        F = row.F
        z, a = row.z, row.a
        # Cor 1.3
        rec('Cor1.3 budget', (ep + em).sum(), 2 * s1 / row.q0)
        # Lemma 1.4
        for j in range(row.n):
            if not F[j]:
                rec('L1.4(a)', -z[j] * V[j], (ep[j] + em[j]) / (2 * t))
                rec('L1.4(c)', (1 - abs(z[j])) * abs(V[j]), (ep[j] + em[j]) / t)
            else:
                sj = np.sign(a[j])
                rec('L1.4(b)', -sj * V[j], (2 * abs(a[j]) + (ep[j] + em[j]) / 2) / t)
        # CL0
        rec('CL0 B+', abs(D['Bp'] @ row.zhat), s1 / (row.q0 * t))
        rec('CL0 B-', abs(D['Bm'] @ row.zhat), s1 / (row.q0 * t))
        # CL1, CL2 for random T subset F
        Fidx = np.where(F)[0]
        for _ in range(3):
            T = np.zeros(row.n, bool)
            T[rng.choice(Fidx, size=rng.integers(0, len(Fidx) + 1), replace=False)] = True
            N = ~T
            alphaNF = np.abs(a[N & F]).sum()
            hN = abs(V[N] @ row.h[N])
            thick = V[T] @ row.zhat[T]
            rec('CL1', thick, hN + 3 * t / (2 * row.q0) + 2 * alphaNF / t)
            rec('CL2', np.abs(V[N]).sum(), -thick + hN + 3 * t / row.q0 + 4 * alphaNF / t)
        # Lemma 1.7 step 1 and (i), Theorem 2.10, Lemma 1.7(ii)
        for m in range(row.B):
            Thp, Thm = D['Thp'][m], D['Thm'][m]
            rec('L1.7 step1 (+)', abs(Thp @ row.zetas[m]), s1 / t)
            rec('L1.7 step1 (-)', abs(Thm @ row.zetas[m]), s1 / t)
            P = peaks[m]
            Q = np.setdiff1d(np.arange(len(row.ws[m])), P)
            dTh = Thm - Thp
            etaP = np.abs(dTh[P]).max() if len(P) else 0.0
            PhiP2 = (row.Phis[m][P] ** 2).sum()
            S1 = t / row.q0 + (row.sigmas[m] / row.q0) * etaP * (1 + Ms[m] * PhiP2 / Cs[m])
            uz = row.Us[m] @ row.zhat
            gam = D['gam'][m]
            rec('L1.7(i) d-row', abs(uz[Q] @ gam[Q]), S1)
            # Theorem 2.10: random G subset Q, random J_c (any coordinates)
            for _ in range(3):
                if len(Q) == 0:
                    break
                G = rng.choice(Q, size=rng.integers(1, len(Q) + 1), replace=False)
                QmG = np.setdiff1d(Q, G)
                rQ = abs(uz[QmG] @ gam[QmG])
                Jc = rng.choice(row.n, size=rng.integers(0, 6), replace=False)
                Rt = uz[G] - row.Us[m][G][:, Jc] @ z[Jc]
                psi = V - gam[G] @ row.Us[m][G]
                PsiJ = np.abs(psi[Jc]).sum()
                alphaJ = np.abs(a[Jc]).sum()
                E = S1 + rQ + t / (2 * row.q0) + 2 * alphaJ / t + PsiJ
                rec('Thm2.10', gam[G] @ Rt, E)
            # Lemma 1.7(ii) for pairs of strict non-peaks and contacts j
            contacts = [j for j in range(row.n) if (not F[j]) and abs(abs(z[j]) - 1) < 1e-12]
            if len(Q) >= 2 and contacts:
                for _ in range(3):
                    k1, k2 = rng.choice(Q, size=2, replace=False)
                    j = int(rng.choice(contacts))
                    u1, u2 = row.Us[m][k1], row.Us[m][k2]
                    if abs(uz[k2]) < 1e-3:
                        continue
                    QmG = np.setdiff1d(Q, [k1, k2])
                    rQ = abs(uz[QmG] @ gam[QmG])
                    S0 = S1 + rQ
                    Mj = u1[j] * uz[k2] - u2[j] * uz[k1]
                    psij = V[j] - gam[k1] * u1[j] - gam[k2] * u2[j]
                    lhs = -z[j] * gam[k1] * Mj / uz[k2]
                    rhs = (ep[j] + em[j]) / (2 * t) + abs(psij) + abs(u2[j] / uz[k2]) * S0
                    rec('L1.7(ii)', lhs, rhs)
    print(f'inst {inst}: done', flush=True) if inst % 10 == 9 else None

print('\nworst normalized slack (LHS - RHS)/(1+|RHS|); must be <= ~1e-6:')
for k, v in worst.items():
    print(f'  {k:28s} {v: .3e}   {"OK" if v <= 1e-5 else "VIOLATED"}')
