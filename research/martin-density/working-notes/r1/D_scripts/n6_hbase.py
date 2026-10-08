# N6: Lemma 11.3 test.  a with long decaying support, b = b0 + beta*a (b0 supported in first 5 coords),
# beta = -b0(xi).  kappa = sup_{|t|<=tau} 2(q*(a+tb)-1)/t^2.  Approximants a_N = P_N a / q*(P_N a),
# x_N = P_N z + G^T(h_N/|h_N|), b' = b0 - b0(x_N) a_N.  Check a_N(x_N)=1, q(x_N)<=1 implicitly, and
# kappa'_N = sup_{|t|<=tau_b} 2(q*(a_N + t b')-1)/t^2 -> kappa (uniform radius tau_b).
import numpy as np
rng = np.random.default_rng(21)
def qs(G, x): return np.abs(x).sum() + np.linalg.norm(G @ x)
worst = 0.0
for trial in range(40):
    n, h = 80, 5
    G = rng.normal(size=(h, n)) / np.sqrt(n)
    a = rng.normal(size=n) * 0.85 ** np.arange(n); a /= qs(G, a)
    z = np.sign(a); h0 = G @ a / np.linalg.norm(G @ a); xi = z + G.T @ h0
    b0 = np.zeros(n); b0[:5] = rng.normal(size=5) * 0.3
    beta = -(b0 @ xi); b = b0 + beta * a
    s0 = np.min(np.abs(a[:5]) / (2*np.abs(b0[:5]) + 1e-300))
    tau = min(0.5, s0)
    ts = np.concatenate([np.linspace(-tau, -tau/200, 100), np.linspace(tau/200, tau, 100)])
    kap = max(2*(qs(G, a + t*b) - 1)/t**2 for t in ts)
    tau_b = tau/3
    tsb = [t for t in ts if abs(t) <= tau_b]
    row = []
    for N in [8, 15, 30, 60, 80]:
        aN = a.copy(); aN[N:] = 0; aN /= qs(G, aN)
        hN = G @ aN; xN = np.where(np.arange(n) < N, z, 0.0) + G.T @ (hN/np.linalg.norm(hN))
        assert abs(aN @ xN - 1) < 1e-12
        bp = b0 - (b0 @ xN) * aN
        kapN = max(2*(qs(G, aN + t*bp) - 1)/t**2 for t in tsb)
        row.append(kapN)
    worst = max(worst, row[-2] - kap)
    if trial < 5:
        print("kappa=%.4f  kappa'_N (N=8,15,30,60,80) =" % kap, " ".join("%.4f" % k for k in row))
print("max over trials of kappa'_{60} - kappa:", worst)
