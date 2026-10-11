"""
N3 sanity check (finite-dimensional model; NOT a statement about Martin's space).
Theorem 2.3 (Part 2) predicts: at a row f' with a visible free coordinate j_f and an aligned set S carrying banks of
total mass mu_S, every mate g' satisfies Osc_S(g'; psi') <= A t + 2 mu_S / t for all t, hence <= 2 sqrt(2 A mu_S)
(exact visibility, H = 0).  We compute, by SOCP, the maximum of the NL functional
    Lambda(g) = g_{s1} psi'_{s2} - g_{s2} psi'_{s1}  (Osc_S = |Lambda| / max(psi'_{s1}, psi'_{s2}))
over the t-discretized fibre {g : p*(f' + t g) <= s(t), t in grid} and look at its dependence on the bank mass m.
Model: coordinates 0..6; 0 = support, 1,2 = S (aligned, banks of mass m each), 3 = j_f (free), 4 contact, 5,6 free.
Diagonal base U* = diag(mu).  One block, 6 carriers; only carrier 0 sees {1,2,3} (exact visibility).
"""
import numpy as np, cvxpy as cp, sys

n = 7
mu = np.array([0.5, 0.3, 0.3, 0.3, 0.2, 0.2, 0.2])
def qstar_np(a): return np.abs(a).sum() + np.linalg.norm(mu * a)

raw = [
    np.array([1.0, 0.6, 0.4, 0.5, 0.0, 0.0, 0.0]),   # k0: robust peak, sees S and j_f
    np.array([1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]),   # k1
    np.array([1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.3]),  # k2
    np.array([0.2, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]),   # k3
    np.array([0.0, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0]),  # k4
    np.array([1.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.5]),  # k5
]
u = np.array([r / qstar_np(r) for r in raw])          # rows u_k, q*(u_k) = 1
Phi = np.array([0.12, 0.06, 0.03, 0.015, 0.008, 0.004])
lam = Phi.copy()                                      # block m = 1: lambda_k = Phi(k)
Rstar = (lam[:, None] * u).T                          # R* W = sum_k lam_k W_k u_k  (n x nb)
nb = len(Phi)

def build_row(m, z3=0.0, a0=1.0):
    a = np.array([a0, m, m, 0, 0, 0, 0], dtype=float)
    a = a / qstar_np(a)
    z = np.array([1.0, 1.0, 1.0, z3, 1.0, 0.3, -0.2])
    e = mu * a / np.linalg.norm(mu * a)
    xhat = z + mu * e
    assert abs(a @ xhat - 1) < 1e-12
    zeta = lam * (u @ xhat)
    w = cp.Variable(nb)
    prob = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(Phi, w), 2) <= 1])
    prob.solve(solver=cp.CLARABEL)
    w = w.value
    f = a + Rstar @ w
    psi = Rstar @ w
    return a, z, xhat, w, f, psi, zeta

def pstar(h):
    A = cp.Variable(n); W = cp.Variable(nb); s = cp.Variable()
    cons = [A + Rstar @ W == h,
            cp.norm(A, 1) + cp.norm(cp.multiply(mu, A), 2) <= s,
            cp.norm(W, 'inf') + cp.norm(cp.multiply(Phi, W), 2) <= s]
    cp.Problem(cp.Minimize(s), cons).solve(solver=cp.CLARABEL)
    return s.value

tgrid = np.concatenate([np.logspace(-5, 0.5, 70)])
tgrid = np.concatenate([tgrid, -tgrid])

def max_lambda(f, psi, s1=1, s2=2):
    g = cp.Variable(n)
    cons = []
    for t in tgrid:
        A = cp.Variable(n); W = cp.Variable(nb)
        st = np.sqrt(1 + t * t)
        cons += [A + Rstar @ W == f + t * g,
                 cp.norm(A, 1) + cp.norm(cp.multiply(mu, A), 2) <= st,
                 cp.norm(W, 'inf') + cp.norm(cp.multiply(Phi, W), 2) <= st]
    obj = g[s1] * psi[s2] - g[s2] * psi[s1]
    prob = cp.Problem(cp.Maximize(obj), cons)
    prob.solve(solver=cp.CLARABEL)
    return prob.value, prob.status

if __name__ == "__main__":
    print("check p*(f') = 1 and peaks:")
    for m in [0.0, 1e-3]:
        a, z, xhat, w, f, psi, zeta = build_row(m)
        sig = zeta @ w
        M = np.max(np.abs(w)); C = np.linalg.norm(Phi * w)
        print(f" m={m:g}: p*(f')={pstar(f):.8f}, M={M:.4f}, C={C:.4f}, |w|={np.round(np.abs(w),4)}, psi[1:4]={np.round(psi[1:4],5)}")
    print()
    print("free j_f (z'_3 = 0): max Lambda over discretized fibre vs bank mass m (per S-coordinate)")
    res = []
    for m in [0.0, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2]:
        a, z, xhat, w, f, psi, zeta = build_row(m)
        val, st = max_lambda(f, psi)
        muS = a[1] + a[2]
        osc = val / max(psi[1], psi[2])
        res.append((m, muS, val, osc))
        print(f" m={m:8.1e} mu_S={muS:9.2e}  maxLambda={val:10.3e}  Osc={osc:10.3e}  Osc/sqrt(mu_S)={osc/np.sqrt(muS) if muS>0 else float('nan'):8.3f} [{st}]")
    print()
    print("comparison: j_f made an aligned contact (z'_3 = 1): no visible free coordinate")
    for m in [0.0, 1e-5, 1e-3]:
        a, z, xhat, w, f, psi, zeta = build_row(m, z3=1.0)
        val, st = max_lambda(f, psi)
        print(f" m={m:8.1e} maxLambda={val:10.3e}  Osc={val/max(psi[1],psi[2]):10.3e} [{st}]")
