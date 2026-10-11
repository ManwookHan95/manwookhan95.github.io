"""N2: Proposition EX and the margin-lever mechanism of Theorem ML in a finite linear model of one (U)-block.

Rows: P (one-sided kind-(iv), generator +e_l only), Q (two-sided kind (i), +-e_q).  Block peak resource: +-rt (two-sided).
Pinned group = all rows; tiny minors C r = 0 (k x n, homogeneous), start rc ON Z (exact resonance), one-signed form mu with
(mu^T C)_P >= 0 (not all 0), (mu^T C)_Q = 0.  Targets rt in Z.  A-regularity: the l_inf ball of radius rho0 around b(rt) =
kappa (rt - rc) is contained in R = {sum t_g g, 0 <= t_g <= cap_g} (checked at all 2^n vertices by LP; sufficient for the
Euclidean ball).  Cases: (A) restricted model, no capped resource; (B) + capped downward margin levers -e_l (l in P) of
capacity cap; (C) restricted model replaced by two extra random SHARED two-sided generators (not orthogonal to C^T mu).
"""
import itertools
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(3)

def in_R(G, caps, pt):
    # feasibility of G t = pt, 0 <= t <= caps
    res = linprog(np.zeros(G.shape[1]), A_eq=G, b_eq=pt, bounds=list(zip(np.zeros(G.shape[1]), caps)), method="highs")
    return res.status == 0

def a_regular(G, caps, b, rho0):
    n = len(b)
    for s in itertools.product((-1.0, 1.0), repeat=n):
        if not in_R(G, caps, b + rho0 * np.array(s)):
            return False
    return True

stats = {"A_nonreg": 0, "B_reg": 0, "C_reg": 0, "trials": 0}
for trial in range(300):
    nP, nQ = rng.integers(2, 4), rng.integers(0, 3)
    n = nP + nQ
    # one minor, one-signed on P, blind to Q: c_P > 0, c_Q = 0 ; Z = {c . r = 0}
    c = np.zeros(n); c[:nP] = rng.uniform(0.5, 2.0, size=nP)
    # start rc on Z with P-entries of both signs
    rc = rng.normal(size=n)
    rc[:nP] -= c[:nP] * (c @ rc) / (c[:nP] @ c[:nP])
    assert abs(c @ rc) < 1e-12
    kappa, W, rho0 = 1.0, 10.0, 1e-3
    cols, caps = [], []
    for l in range(nP):
        e = np.zeros(n); e[l] = 1.0; cols.append(e); caps.append(W / 2)          # one-sided bank
    for q in range(nP, n):
        e = np.zeros(n); e[q] = 1.0; cols += [e, -e]; caps += [W / 2, W / 2]       # two-sided tune
    cols += [rc.copy(), -rc.copy()]; caps += [W / 2, W / 2]                          # peak resource (block scaling)
    GA, capA = np.array(cols).T, np.array(caps)
    # target: rt on Z near rc: rc + tangent move (keeps c.r = 0)
    tdir = rng.normal(size=n); tdir -= c * (c @ tdir) / (c @ c)
    rt = rc + 0.01 * tdir / np.linalg.norm(tdir)
    b = kappa * (rt - rc)
    stats["trials"] += 1
    # (A) restricted model: never A-regular (Proposition EX)
    if not a_regular(GA, capA, b, rho0):
        stats["A_nonreg"] += 1
    # (B) margin levers of capacity cap >= 4(rho0 + max|b_P|)
    capm = 4 * (rho0 + np.max(np.abs(b[:nP])))
    colsB, capsB = [GA[:, j] for j in range(GA.shape[1])], list(capA)
    for l in range(nP):
        e = np.zeros(n); e[l] = -1.0; colsB.append(e); capsB.append(capm)
    if a_regular(np.array(colsB).T, np.array(capsB), b, rho0):
        stats["B_reg"] += 1
    # (C) two random shared two-sided generators
    colsC, capsC = [GA[:, j] for j in range(GA.shape[1])], list(capA)
    for k in range(2):
        g = rng.normal(size=n); colsC += [g, -g]; capsC += [W / 2, W / 2]
    if a_regular(np.array(colsC).T, np.array(capsC), b, rho0):
        stats["C_reg"] += 1

print("trials %d" % stats["trials"])
print("(A) restricted model, exact one-signed resonance, no capped resource: NOT A-regular in %d / %d" % (stats["A_nonreg"], stats["trials"]))
print("(B) + margin levers of capacity 4(rho0 + max|b_P|): A-regular in %d / %d" % (stats["B_reg"], stats["trials"]))
print("(C) + two random shared two-sided generators (hypothesis of Prop. EX violated): A-regular in %d / %d" % (stats["C_reg"], stats["trials"]))
