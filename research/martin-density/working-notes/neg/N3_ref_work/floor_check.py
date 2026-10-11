"""
N3-ref sanity check (finite-dimensional model; NOT a statement about Martin's space).
Purpose: N3's sqrt(mu) law (Osc_S <= 2 sqrt(2 A mu_S)) was tested only in a model with EXACT visibility (only one
carrier sees S u {j_f}).  For admissible T exact visibility is impossible (every coordinate is seen by infinitely many
carriers; only finitely many peaks have alpha >= alpha_0).  Here we add ONE extra low-weight carrier k6 that sees S and
compare:
  (a) k6 a STRICT NON-PEAK (u6(xhat) = 0): genuine two-sided freedom on S -> Osc at m = 0 should be > 0;
  (b) k6 a low-weight PEAK with robust margin (u6(xhat) != 0): exact theory (Prop 1.7(c)-type locking) predicts no
      freedom, while Theorem 2.3 has the floor 2 sqrt(15 A H) > 0 with H >= lambda6 (|u6(1)| + |u6(2)|).
Model as in N3_work/sqrt_mu_check.py: coordinates 0..6; 0 support, 1,2 = S (aligned, banks of mass m), 3 = j_f free.
"""
import numpy as np, cvxpy as cp

n = 7
mu = np.array([0.5, 0.3, 0.3, 0.3, 0.2, 0.2, 0.2])
def qstar_np(a): return np.abs(a).sum() + np.linalg.norm(mu * a)

raw_base = [
    np.array([1.0, 0.6, 0.4, 0.5, 0.0, 0.0, 0.0]),
    np.array([1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]),
    np.array([1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.3]),
    np.array([0.2, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]),
    np.array([0.0, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0]),
    np.array([1.0, 0.0, 0.0, 0.0, 0.0, -0.5, 0.5]),
]
Phi_base = np.array([0.12, 0.06, 0.03, 0.015, 0.008, 0.004])

def model(extra_raw=None, extra_phi=None):
    raws = list(raw_base); Phi = list(Phi_base)
    if extra_raw is not None:
        raws.append(extra_raw); Phi.append(extra_phi)
    u = np.array([r / qstar_np(r) for r in raws]); Phi = np.array(Phi)
    lam = Phi.copy(); Rstar = (lam[:, None] * u).T
    return u, Phi, lam, Rstar

def build_row(u, Phi, lam, Rstar, m, z3=0.0):
    a = np.array([1.0, m, m, 0, 0, 0, 0], dtype=float); a = a / qstar_np(a)
    z = np.array([1.0, 1.0, 1.0, z3, 1.0, 0.3, -0.2])
    e = mu * a / np.linalg.norm(mu * a); xhat = z + mu * e
    zeta = lam * (u @ xhat)
    nb = len(Phi); w = cp.Variable(nb)
    cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(Phi, w), 2) <= 1]).solve(solver=cp.CLARABEL)
    w = w.value; psi = Rstar @ w; f = a + psi
    return a, z, xhat, w, f, psi, zeta

tgrid = np.logspace(-5, 0.5, 70); tgrid = np.concatenate([tgrid, -tgrid])

def max_osc(Phi, Rstar, f, psi, s1=1, s2=2):
    nb = len(Phi); g = cp.Variable(n); cons = []
    for t in tgrid:
        A = cp.Variable(n); W = cp.Variable(nb); st = np.sqrt(1 + t * t)
        cons += [A + Rstar @ W == f + t * g,
                 cp.norm(A, 1) + cp.norm(cp.multiply(mu, A), 2) <= st,
                 cp.norm(W, 'inf') + cp.norm(cp.multiply(Phi, W), 2) <= st]
    obj = g[s1] * psi[s2] - g[s2] * psi[s1]
    prob = cp.Problem(cp.Maximize(obj), cons); prob.solve(solver=cp.CLARABEL)
    return prob.value / max(abs(psi[s1]), abs(psi[s2])), prob.status

if __name__ == "__main__":
    print("baseline (exact visibility, N3 model):")
    u, Phi, lam, Rs = model()
    for m in [0.0, 1e-4]:
        a, z, xh, w, f, psi, zeta = build_row(u, Phi, lam, Rs, m)
        o, st = max_osc(Phi, Rs, f, psi); print(f"  m={m:7.1e}  Osc_max={o:10.3e} [{st}]")
    for label, raw6 in [("(a) strict non-peak u6 ~ e1 - e2", np.array([0.0, 1.0, -1.0, 0, 0, 0, 0])),
                        ("(b) low-weight peak u6 ~ e1 - 0.5 e2", np.array([0.0, 1.0, -0.5, 0, 0, 0, 0]))]:
        print(label)
        for phi6 in [2e-3, 5e-4, 1e-4]:
            u, Phi, lam, Rs = model(raw6, phi6)
            for m in [0.0, 1e-4]:
                a, z, xh, w, f, psi, zeta = build_row(u, Phi, lam, Rs, m)
                M_ = np.max(np.abs(w)); C_ = np.linalg.norm(Phi * w)
                peak6 = abs(abs(w[6]) - M_) < 1e-7
                o, st = max_osc(Phi, Rs, f, psi)
                H6 = lam[6] * (abs(u[6][1]) + abs(u[6][2]))
                print(f"  phi6={phi6:7.1e} m={m:7.1e} k6 {'PEAK' if peak6 else 'non-peak'} |w6|={abs(w[6]):.4f} M={M_:.4f}"
                      f"  H6={H6:9.2e}  Osc_max={o:10.3e}  Osc/sqrt(H6)={o/np.sqrt(H6):7.3f} [{st}]")
