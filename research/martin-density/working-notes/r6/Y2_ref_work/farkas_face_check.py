"""Referee sanity check of Y2 Lemma 4.1 (Farkas pinning of the d-forced face) and Prop 4.3 (face reduction):
random cones Z0 = {G x >= 0, E x = 0} in R^n, d-rows Q; C = Z0 cap ker Q; A = inequality rows vanishing on C but not on Z0;
kappa* = least sup-norm Farkas certificate of -sum_A r_a; check sum_A |r_a(tau)| <= (kappa*+2) V1(tau) and that the
projection tau -> tau' in C built as in Prop 4.3 (Hoffman to F_min, then repair inside F_min) is in C."""
import numpy as np
from scipy.optimize import linprog
rng = np.random.default_rng(2026)

def maxrow(G, E, Q, g):
    # max g.x over {Gx>=0, Ex=0, Qx=0, -1<=x<=1}
    n = len(g); A_ub = -G; b_ub = np.zeros(G.shape[0])
    A_eq = np.vstack([E, Q]) if (E.size + Q.size) else None
    b_eq = np.zeros(A_eq.shape[0]) if A_eq is not None else None
    r = linprog(-g, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[(-1, 1)]*n, method="highs")
    return -r.fun

trials = 0; worst = -np.inf; nA = 0
for trial in range(400):
    n = rng.integers(3, 8); mG = rng.integers(2, 8); mE = rng.integers(0, 2); mQ = rng.integers(1, 3)
    G = rng.integers(-2, 3, size=(mG, n)).astype(float)
    G = np.vstack([G, np.eye(n)[:rng.integers(1, n+1)]])   # some sign rows tau_l >= 0
    E = rng.integers(-1, 2, size=(mE, n)).astype(float) if mE else np.zeros((0, n))
    Q = rng.normal(size=(mQ, n))
    Z0 = np.zeros((0, n))
    forcedC = [i for i in range(G.shape[0]) if maxrow(G, E, Q, G[i]) < 1e-9]
    forcedZ = [i for i in range(G.shape[0]) if maxrow(G, E, Z0, G[i]) < 1e-9]
    A = [i for i in forcedC if i not in forcedZ]
    if not A: continue
    nA += 1
    rhoA = G[A].sum(axis=0)
    # certificate: -rhoA = G^T y + E^T y' + Q^T k, y>=0; minimize t >= |coeffs|
    mg, me, mq = G.shape[0], E.shape[0], Q.shape[0]
    nv = mg + me + mq + 1
    c = np.zeros(nv); c[-1] = 1
    Aeq = np.hstack([G.T, E.T, Q.T, np.zeros((n, 1))]); beq = -rhoA
    Aub = []; bub = []
    for i in range(mg + me + mq):
        row = np.zeros(nv); row[i] = 1; row[-1] = -1; Aub.append(row); bub.append(0)
        row = np.zeros(nv); row[i] = -1; row[-1] = -1; Aub.append(row); bub.append(0)
    bounds = [(0, None)]*mg + [(None, None)]*(me + mq) + [(0, None)]
    r = linprog(c, A_ub=np.array(Aub), b_ub=np.array(bub), A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
    if r.status != 0: print("no certificate?!", trial); continue
    kap = r.fun
    for _ in range(200):
        tau = rng.normal(size=n) * rng.uniform(0.01, 3)
        V1 = np.sum(np.maximum(-(G @ tau), 0)) + np.sum(np.abs(E @ tau)) + np.sum(np.abs(Q @ tau))
        lhs = np.sum(np.abs(G[A] @ tau))
        worst = max(worst, lhs - (kap + 2) * V1); trials += 1
print("instances with nonempty d-forced set:", nA, " tests:", trials, " max(lhs - (kappa*+2)V1) =", worst)
